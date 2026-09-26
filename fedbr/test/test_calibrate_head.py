"""Tests for the core of scripts/calibrate_head.py (post-hoc classifier
calibration on mean samples).

    uv run python -m unittest fedbr.test.test_calibrate_head
"""

import unittest

import torch
import torch.nn.functional as F
from torch.utils.data import TensorDataset

from fedbr import algorithms, hparams_registry
from fedbr.lib import misc
from fedbr.lib.fast_data_loader import FastDataLoader
from fedbr.scripts import calibrate_head as ch


class TestBuildMeanSamples(unittest.TestCase):

    def setUp(self):
        g = torch.Generator().manual_seed(0)
        self.X = torch.randn(20, 3, 8, 8, generator=g)
        self.y = torch.randint(0, 4, (20,), generator=g)
        self.env = TensorDataset(self.X, self.y)

    def test_m1_is_a_raw_image_with_a_one_hot_label(self):
        Xm, Ym = ch.build_mean_samples(self.env, n=6, M=1, num_classes=4,
                                       generator=torch.Generator().manual_seed(1))
        self.assertEqual(Xm.shape, (6, 3, 8, 8))
        self.assertEqual(Ym.shape, (6, 4))
        for p in range(6):
            matches = [i for i in range(20) if torch.equal(self.X[i], Xm[p])]
            self.assertEqual(len(matches), 1)
            self.assertTrue(torch.equal(Ym[p], F.one_hot(self.y[matches[0]], 4).float()))

    def test_m4_labels_are_histograms(self):
        Xm, Ym = ch.build_mean_samples(self.env, n=5, M=4, num_classes=4,
                                       generator=torch.Generator().manual_seed(1))
        self.assertTrue(torch.allclose(Ym.sum(1), torch.ones(5)))
        self.assertTrue(torch.allclose(Ym * 4, (Ym * 4).round()))
        # a mean of 4 images has a smaller spread than one image
        self.assertLess(Xm.std().item(), self.X.std().item())

    def test_same_seed_same_draw(self):
        a = ch.build_mean_samples(self.env, 5, 3, 4, torch.Generator().manual_seed(9))
        b = ch.build_mean_samples(self.env, 5, 3, 4, torch.Generator().manual_seed(9))
        self.assertTrue(torch.equal(a[0], b[0]) and torch.equal(a[1], b[1]))


def two_gaussians(n=200, seed=0):
    g = torch.Generator().manual_seed(seed)
    z0 = torch.randn(n, 2, generator=g) + torch.tensor([3.0, 0.0])
    z1 = torch.randn(n, 2, generator=g) + torch.tensor([-3.0, 0.0])
    Z = torch.cat([z0, z1])
    y = torch.cat([torch.zeros(n), torch.ones(n)]).long()
    return Z, y


class TestLdaHead(unittest.TestCase):

    def test_separates_two_gaussians(self):
        Z, y = two_gaussians()
        W, b = ch.lda_head(Z, F.one_hot(y, 2).float())
        self.assertEqual(W.shape, (2, 2))
        self.assertGreater(ch.head_accuracy(W, b, Z, y), 0.99)

    def test_soft_labels_weight_the_class_means(self):
        Z, y = two_gaussians()
        hard = F.one_hot(y, 2).float()
        W1, b1 = ch.lda_head(Z, hard)
        # Mixing every label half-way with the uniform vector keeps the
        # ordering of the class means, so the boundary must not move much.
        W2, b2 = ch.lda_head(Z, 0.5 * hard + 0.25)
        self.assertGreater(ch.head_accuracy(W2, b2, Z, y), 0.99)
        # but a pure uniform label carries no class information
        with self.assertRaises(ValueError):
            ch.lda_head(Z, torch.full_like(hard, 0.5))


class TestRetrainHeadCe(unittest.TestCase):

    def test_lowers_the_soft_cross_entropy(self):
        Z, y = two_gaussians()
        Y = F.one_hot(y, 2).float()
        W0, b0 = torch.zeros(2, 2), torch.zeros(2)
        W, b = ch.retrain_head_ce(W0, b0, Z, Y, epochs=20, lr=0.1,
                                  batch_size=32, generator=torch.Generator().manual_seed(0))
        before = ch.soft_cross_entropy(Z @ W0.t() + b0, Y)
        after = ch.soft_cross_entropy(Z @ W.t() + b, Y)
        self.assertLess(after, before)
        self.assertGreater(ch.head_accuracy(W, b, Z, y), 0.99)
        # the inputs were not modified in place
        self.assertTrue(torch.equal(W0, torch.zeros(2, 2)))


class TestHeadAccuracyMatchesModel(unittest.TestCase):
    """Scoring cached features with (W, b) must equal scoring the full model
    with misc.accuracy, which is what train_fed.py and summarize.py report."""

    def test_equals_misc_accuracy(self):
        hp = hparams_registry.default_hparams('ERM', 'Debug28')
        torch.manual_seed(0)
        model = algorithms.ERM((3, 28, 28), 5, 3, hp).eval()
        g = torch.Generator().manual_seed(1)
        X = torch.randn(40, 3, 28, 28, generator=g)
        y = torch.randint(0, 5, (40,), generator=g)
        Z = ch.featurize(model.featurizer, X, 'cpu', batch_size=16)
        W, b = ch.head_params(model.classifier)
        got = ch.head_accuracy(W, b, Z, y)
        ref = misc.accuracy(model, FastDataLoader(TensorDataset(X, y), 16, 0),
                            None, 'cpu')
        self.assertAlmostEqual(got, ref, places=6)

    def test_set_head_params_round_trip(self):
        hp = hparams_registry.default_hparams('ERM', 'Debug28')
        model = algorithms.ERM((3, 28, 28), 5, 3, hp)
        W, b = torch.randn(5, 128), torch.randn(5)
        ch.set_head_params(model.classifier, W, b)
        W2, b2 = ch.head_params(model.classifier)
        self.assertTrue(torch.equal(W, W2) and torch.equal(b, b2))


class TestResolveCheckpoints(unittest.TestCase):
    """make on Windows does not expand `*/model.pkl`, so the script must
    accept a run directory or a glob pattern itself."""

    def test_directory_glob_and_file(self):
        import os
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            for run in ('fedavg', 'fedbr'):
                os.makedirs(os.path.join(d, run))
                open(os.path.join(d, run, 'model.pkl'), 'w').close()
            os.makedirs(os.path.join(d, 'no_model'))
            by_dir = ch.resolve_checkpoints([d])
            by_glob = ch.resolve_checkpoints([os.path.join(d, '*', 'model.pkl')])
            one = ch.resolve_checkpoints([os.path.join(d, 'fedbr', 'model.pkl')])
            self.assertEqual([os.path.basename(os.path.dirname(p)) for p in by_dir],
                             ['fedavg', 'fedbr'])
            self.assertEqual(by_dir, by_glob)
            self.assertEqual(len(one), 1)
            with self.assertRaises(SystemExit):
                ch.resolve_checkpoints([os.path.join(d, 'no_model')])


if __name__ == '__main__':
    unittest.main()