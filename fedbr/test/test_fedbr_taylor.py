"""Tests for FedBRTaylor: FedBR plus the soft-label and first-order Taylor
terms of FedMix, computed on FedBR's fixed pseudo-data.

CPU-only, so they run without a GPU:
    uv run python -m unittest fedbr.test.test_fedbr_taylor
"""

import copy
import unittest

import torch
import torch.nn.functional as F
from torch.utils.data import TensorDataset

from fedbr import algorithms
from fedbr import hparams_registry


INPUT_SHAPE = (3, 28, 28)   # MNIST_CNN featurizer, 128-d features
NUM_CLASSES = 2
BATCH = 8


def make_hparams(algorithm, **overrides):
    hparams = hparams_registry.default_hparams(algorithm, 'Debug28')
    # train_fed.py injects these two from the command line.
    hparams['use_Mixup'] = False
    hparams['use_Mixture'] = False
    hparams.update(overrides)
    return hparams


def make_batch(seed):
    g = torch.Generator().manual_seed(seed)
    x = torch.randn(BATCH, *INPUT_SHAPE, generator=g)
    y = torch.randint(0, NUM_CLASSES, (BATCH,), generator=g)
    return [(x, y)]


def make_pseudo(seed, with_labels):
    """FedBR receives a list of (1,C,H,W) images; FedBRTaylor a list of
    ((1,C,H,W) image, (num_classes,) soft label) pairs, as
    train_fed.get_augmentation_fedmix_data returns them."""
    g = torch.Generator().manual_seed(seed)
    # Images first, labels after, so both variants get identical images.
    imgs = [torch.randn(1, *INPUT_SHAPE, generator=g) for _ in range(BATCH)]
    if not with_labels:
        return imgs
    labs = [torch.rand(NUM_CLASSES, generator=g) for _ in range(BATCH)]
    return [(img, lab / lab.sum()) for img, lab in zip(imgs, labs)]


def build(algorithm, hparams, seed=0):
    torch.manual_seed(seed)
    cls = algorithms.get_algorithm_class(algorithm)
    return cls(INPUT_SHAPE, NUM_CLASSES, 3, hparams)


def params_of(algo):
    return {k: v.detach().clone() for k, v in algo.state_dict().items()
            if v.dtype.is_floating_point}


def assert_params_close(test, a, b, atol=1e-6):
    test.assertEqual(set(a), set(b))
    for k in a:
        test.assertTrue(torch.allclose(a[k], b[k], atol=atol, rtol=0),
                        'parameter %s differs (max abs diff %g)'
                        % (k, (a[k] - b[k]).abs().max().item()))


class TestRegistration(unittest.TestCase):

    def test_algorithm_is_registered(self):
        self.assertIn('FedBRTaylor', algorithms.ALGORITHMS)
        self.assertTrue(issubclass(
            algorithms.get_algorithm_class('FedBRTaylor'), algorithms.FedBR))

    def test_default_hparams(self):
        hp = hparams_registry.default_hparams('FedBRTaylor', 'RotatedCIFAR10')
        self.assertEqual(hp['fedbrt_lambda'], 0.1)
        self.assertEqual(hp['fedbrt_taylor'], 1)
        self.assertEqual(hp['fedbrt_label'], 'soft')
        # inherited from FedBR
        self.assertEqual(hp['fedbr_mu'], 0.5)
        self.assertEqual(hp['fedbr_lambda'], 1.0)
        self.assertEqual(hp['fedbr_tau1'], 2.0)
        self.assertEqual(hp['fedbr_tau2'], 2.0)
        # needed by the projection MLP, like FedBR
        self.assertIn('mlp_depth', hp)
        self.assertIn('mlp_dropout', hp)


class TestReducesToFedBR(unittest.TestCase):
    """With lambda = 0 both added terms vanish and one update must move the
    parameters exactly as FedBR does, on the same batch and pseudo-data."""

    def _one_step(self, algorithm, hparams, pseudo):
        # float64: the FedBRTaylor forward asks for the input gradient, which
        # can route conv backward through a different kernel; in float32 that
        # alone moves the weights by ~1e-6. In double a real difference in
        # the objective is orders of magnitude above that noise.
        algo = build(algorithm, hparams, seed=0).double()
        algo.train()
        (x, y), = make_batch(1)
        pseudo = [(p[0].double(), p[1].double()) if isinstance(p, tuple)
                  else p.double() for p in pseudo]
        algo.update([(x.double(), y)], pseudo)
        return params_of(algo)

    def test_lambda_zero_matches_fedbr(self):
        ref = self._one_step('FedBR', make_hparams('FedBR'),
                             make_pseudo(2, with_labels=False))
        for taylor in (0, 1):
            got = self._one_step(
                'FedBRTaylor',
                make_hparams('FedBRTaylor', fedbrt_lambda=0.0,
                             fedbrt_taylor=taylor),
                make_pseudo(2, with_labels=True))
            assert_params_close(self, ref, got, atol=1e-10)

    def test_lambda_positive_differs_from_fedbr(self):
        ref = self._one_step('FedBR', make_hparams('FedBR'),
                             make_pseudo(2, with_labels=False))
        got = self._one_step(
            'FedBRTaylor', make_hparams('FedBRTaylor', fedbrt_lambda=0.1),
            make_pseudo(2, with_labels=True))
        diff = max((ref[k] - got[k]).abs().max().item() for k in ref)
        self.assertGreater(diff, 1e-6)


class TestTaylorTerm(unittest.TestCase):
    """Term (III) of (3.15) with the batch normalisation of the formula:
    lambda (1 - lambda) * mean_k < grad_x CE(f(x_k), y_k), u_k >."""

    def setUp(self):
        self.lam = 0.1
        self.algo = build('FedBRTaylor',
                          make_hparams('FedBRTaylor', fedbrt_lambda=self.lam))
        self.algo.eval()
        (self.x, self.y), = make_batch(3)
        self.u = torch.cat([img for img, _ in make_pseudo(4, True)])

    def _per_sample_expected(self):
        acc = 0.0
        for k in range(BATCH):
            xk = self.x[k:k + 1].clone().requires_grad_()
            ce = F.cross_entropy(self.algo.predict(xk), self.y[k:k + 1])
            g, = torch.autograd.grad(ce, xk)
            acc = acc + (g * self.u[k:k + 1]).sum()
        return self.lam * (1 - self.lam) * acc / BATCH

    def test_matches_per_sample_definition(self):
        got = self.algo.taylor_term(self.x, self.y, self.u, self.lam)
        self.assertTrue(torch.allclose(got, self._per_sample_expected(),
                                       atol=1e-6, rtol=1e-4),
                        (got.item(), self._per_sample_expected().item()))

    def test_is_batch_size_times_the_released_fedmix_normalisation(self):
        """The released FedMix divides the term by the batch size a second
        time (INDEX F1). The formula term must be exactly B times that."""
        x = self.x.clone().requires_grad_()
        loss1 = (1 - self.lam) * F.cross_entropy(self.algo.predict(x), self.y)
        grad = torch.autograd.grad(loss1, x)[0]
        released = torch.sum(self.lam * grad * self.u) / BATCH
        got = self.algo.taylor_term(self.x, self.y, self.u, self.lam)
        self.assertTrue(torch.allclose(got, BATCH * released,
                                       atol=1e-6, rtol=1e-4),
                        (got.item(), (BATCH * released).item()))

    def test_term_carries_gradient_to_the_model(self):
        got = self.algo.taylor_term(self.x, self.y, self.u, self.lam)
        self.assertTrue(got.requires_grad)
        got.backward()
        grads = [p.grad for p in self.algo.featurizer.parameters()
                 if p.grad is not None]
        self.assertTrue(any(g.abs().sum() > 0 for g in grads))


class TestTaylorNormalisation(unittest.TestCase):
    """hparam fedbrt_taylor_norm: 'formula' (default) keeps term (III) at the
    magnitude of (3.15); 'released' divides it by the batch size once more,
    reproducing the magnitude the released FedMix trains with (INDEX F1).
    Used as the control run that isolates the magnitude of (III)."""

    def _term(self, norm):
        algo = build('FedBRTaylor',
                     make_hparams('FedBRTaylor', fedbrt_lambda=0.1,
                                  fedbrt_taylor_norm=norm))
        algo.eval()
        (x, y), = make_batch(3)
        u = torch.cat([img for img, _ in make_pseudo(4, True)])
        return algo.taylor_term(x, y, u, 0.1)

    def test_default_is_formula(self):
        hp = hparams_registry.default_hparams('FedBRTaylor', 'RotatedCIFAR10')
        self.assertEqual(hp['fedbrt_taylor_norm'], 'formula')

    def test_released_is_formula_over_batch_size(self):
        formula = self._term('formula')
        released = self._term('released')
        self.assertTrue(torch.allclose(released * BATCH, formula,
                                       atol=1e-7, rtol=1e-5),
                        (released.item(), formula.item()))

    def test_released_changes_the_update(self):
        params = {}
        for norm in ('formula', 'released'):
            algo = build('FedBRTaylor',
                         make_hparams('FedBRTaylor', fedbrt_lambda=0.1,
                                      fedbrt_taylor_norm=norm))
            algo.train()
            algo.update(make_batch(1), make_pseudo(2, True))
            params[norm] = params_of(algo)
        diff = max((params['formula'][k] - params['released'][k]).abs().max().item()
                   for k in params['formula'])
        self.assertGreater(diff, 1e-7)

    def test_unknown_norm_is_rejected(self):
        algo = build('FedBRTaylor',
                     make_hparams('FedBRTaylor', fedbrt_taylor_norm='bogus'))
        with self.assertRaises(ValueError):
            algo.update(make_batch(1), make_pseudo(2, True))


class TestLabelChoice(unittest.TestCase):

    def _step_with_labels(self, label_mode, label_seed):
        algo = build('FedBRTaylor',
                     make_hparams('FedBRTaylor', fedbrt_lambda=0.1,
                                  fedbrt_label=label_mode))
        algo.train()
        imgs = [img for img, _ in make_pseudo(2, True)]
        labs = [lab for _, lab in make_pseudo(label_seed, True)]
        algo.update(make_batch(1), list(zip(imgs, labs)))
        return params_of(algo)

    def test_uniform_ignores_the_soft_labels(self):
        a = self._step_with_labels('uniform', label_seed=10)
        b = self._step_with_labels('uniform', label_seed=11)
        assert_params_close(self, a, b, atol=0.0)

    def test_soft_uses_the_soft_labels(self):
        a = self._step_with_labels('soft', label_seed=10)
        b = self._step_with_labels('soft', label_seed=11)
        diff = max((a[k] - b[k]).abs().max().item() for k in a)
        self.assertGreater(diff, 1e-7)

    def test_unknown_label_mode_is_rejected(self):
        algo = build('FedBRTaylor',
                     make_hparams('FedBRTaylor', fedbrt_label='bogus'))
        with self.assertRaises(ValueError):
            algo.update(make_batch(1), make_pseudo(2, True))


class TestUnsupportedVariants(unittest.TestCase):

    def test_rejects_mixup(self):
        algo = build('FedBRTaylor', make_hparams('FedBRTaylor', use_Mixup=True))
        with self.assertRaises(NotImplementedError):
            algo.update(make_batch(1), make_pseudo(2, True))

    def test_rejects_mixture(self):
        algo = build('FedBRTaylor',
                     make_hparams('FedBRTaylor', use_Mixture=True))
        with self.assertRaises(NotImplementedError):
            algo.update(make_batch(1), make_pseudo(2, True))


class TestPseudoDataParity(unittest.TestCase):
    """FedBRTaylor builds its pseudo-data once with
    get_augmentation_fedmix_data. That function draws the client and the
    ten images in the same order as get_augmentation_mean_data (FedBR's
    builder), so at equal seed the images are identical and only the soft
    label is new. Guards the design assumption; it passes on the released
    code."""

    def test_same_images_plus_labels(self):
        from fedbr.scripts.train_fed import (
            get_augmentation_mean_data, get_augmentation_fedmix_data)
        envs = []
        for e in range(3):
            g = torch.Generator().manual_seed(100 + e)
            envs.append((TensorDataset(torch.randn(20, *INPUT_SHAPE, generator=g),
                                       torch.randint(0, NUM_CLASSES, (20,),
                                                     generator=g)),
                         None))
        torch.manual_seed(7)
        a = get_augmentation_mean_data(envs, 'cpu', None, bs=5)
        torch.manual_seed(7)
        b = get_augmentation_fedmix_data(envs, 'cpu', 5, class_num=NUM_CLASSES)
        self.assertEqual(len(a), len(b))
        for img_a, (img_b, lab_b) in zip(a, b):
            self.assertTrue(torch.equal(img_a, img_b))
            self.assertEqual(lab_b.shape, (NUM_CLASSES,))
            self.assertAlmostEqual(lab_b.sum().item(), 1.0, places=5)


if __name__ == '__main__':
    unittest.main()