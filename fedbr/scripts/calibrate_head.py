"""Post-hoc classifier calibration on mean samples (thesis probe).

Takes a finished run's model.pkl, freezes its feature extractor, and retrains
only the classifier on the features of *mean samples*: each is the average of
M images drawn from one training client, with the label histogram of those
images as a soft label. This is the mean-sample channel of the thesis
framework used one more way -- as calibration data for the classifier after
federated training -- and it is the same post-hoc step that CCVR / an LDA head
apply to Gaussian virtual features.

For every (M, method) the script reports the mean accuracy on the training
clients' held-out splits (env00..09_out, the paper's metric) and on the
fixed-angle test environments (env10..19_in), before and after calibration.
Evaluation features are computed once per checkpoint, so sweeping M costs
only the head fits.

    uv run python -m fedbr.scripts.calibrate_head output/cifar10/02_attempt_20260916/*/model.pkl
    uv run python -m fedbr.scripts.calibrate_head output/.../fedbr/model.pkl --M 1 2 5 10 --n_per_client 200

M = 1 shares raw images and is the ceiling: it tells how much the averaging
costs. Results go to <out_dir>/<run-name>.json.
"""

import argparse
import glob
import json
import os
import sys
import time

import numpy as np
import torch
import torch.nn.functional as F

from fedbr import algorithms
from fedbr.lib import misc
from fedbr.scripts.eval_checkpoint import load_dataset


# --------------------------------------------------------------------- core

def build_mean_samples(env, n, M, num_classes, generator):
    """n mean samples from one client's dataset `env`: each averages M images
    drawn with replacement; the label is the histogram of their labels.
    Returns (X [n, ...], Y [n, num_classes])."""
    idx = torch.randint(0, len(env), (n, M), generator=generator)
    xs, ys = [], []
    for p in range(n):
        x_acc = None
        y_acc = torch.zeros(num_classes)
        for m in range(M):
            x, y = env[int(idx[p, m])]
            x_acc = x.clone() if x_acc is None else x_acc + x
            y_acc[int(y)] += 1.0
        xs.append(x_acc / M)
        ys.append(y_acc / M)
    return torch.stack(xs), torch.stack(ys)


def featurize(feature_fn, X, device, batch_size=256):
    """Apply the frozen feature extractor batch-wise; returns CPU features."""
    out = []
    with torch.no_grad():
        for i in range(0, len(X), batch_size):
            out.append(feature_fn(X[i:i + batch_size].to(device)).float().cpu())
    return torch.cat(out)


def head_params(linear):
    return (linear.weight.detach().clone().cpu(),
            linear.bias.detach().clone().cpu())


def set_head_params(linear, W, b):
    with torch.no_grad():
        linear.weight.copy_(W.to(linear.weight.device))
        linear.bias.copy_(b.to(linear.bias.device))


def soft_cross_entropy(logits, Y):
    return -(Y * F.log_softmax(logits, 1)).sum(1).mean()


def head_accuracy(W, b, Z, y):
    pred = (Z @ W.t() + b).argmax(1)
    return (pred == y).float().mean().item()


def lda_head(Z, Y, shrinkage=0.01, prior='uniform'):
    """Closed-form LDA classifier from features Z [N, d] and soft labels
    Y [N, C]: class means weighted by Y, one shared covariance shrunk towards
    (tr/d) I, as in the thesis's Flower head_methods.py. Returns (W, b)."""
    Z = Z.double()
    Y = Y.double()
    N, d = Z.shape
    counts = Y.sum(0)
    if (counts <= 0).any():
        raise ValueError('a class receives no label mass')
    mu = (Y.t() @ Z) / counts[:, None]                      # [C, d]
    if torch.cdist(mu, mu).max() < 1e-8:
        raise ValueError('labels carry no class information: all class means coincide')
    diff = Z[:, None, :] - mu[None, :, :]                   # [N, C, d]
    sigma = torch.einsum('nc,ncd,nce->de', Y, diff, diff) / N
    sigma = (1 - shrinkage) * sigma + shrinkage * (torch.trace(sigma) / d) * torch.eye(d, dtype=Z.dtype)
    W = torch.linalg.solve(sigma, mu.t()).t()               # mu Sigma^{-1}
    b = -0.5 * (W * mu).sum(1)
    if prior == 'empirical':
        b = b + torch.log(counts / N)
    elif prior != 'uniform':
        raise ValueError('prior must be uniform or empirical')
    return W.float(), b.float()


def retrain_head_ce(W0, b0, Z, Y, epochs, lr, batch_size, generator, momentum=0.9):
    """Fine-tune a linear head from (W0, b0) on features Z with soft labels Y
    by SGD on the soft cross-entropy. Returns new (W, b)."""
    W = torch.nn.Parameter(W0.clone())
    b = torch.nn.Parameter(b0.clone())
    opt = torch.optim.SGD([W, b], lr=lr, momentum=momentum)
    N = len(Z)
    for _ in range(epochs):
        perm = torch.randperm(N, generator=generator)
        for i in range(0, N, batch_size):
            j = perm[i:i + batch_size]
            opt.zero_grad()
            soft_cross_entropy(Z[j] @ W.t() + b, Y[j]).backward()
            opt.step()
    return W.detach(), b.detach()


# ------------------------------------------------------------------- script

def resolve_checkpoints(paths):
    """Each entry may be a model.pkl, a run directory (its */model.pkl are
    taken) or a glob pattern; make on Windows does not expand globs."""
    out = []
    for p in paths:
        if os.path.isdir(p):
            found = sorted(glob.glob(os.path.join(p, '*', 'model.pkl')))
        elif any(c in p for c in '*?['):
            found = sorted(glob.glob(p))
        else:
            found = [p]
        if not found:
            raise SystemExit('no model.pkl found for {}'.format(p))
        out += found
    return out


def feature_function(model, algorithm):
    """The map from images to classifier inputs, per algorithm."""
    if algorithm == 'Moon':
        return lambda x: model.projection_head(model.featurizer(x))
    return model.featurizer


def main():
    p = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('checkpoint', nargs='+',
        help='model.pkl files, run directories (their */model.pkl) or glob patterns')
    p.add_argument('--M', type=int, nargs='+', default=[1, 2, 5, 10],
        help='images per mean sample; 1 = raw images (ceiling)')
    p.add_argument('--n_per_client', type=int, default=200,
        help='mean samples built per training client')
    p.add_argument('--method', choices=['ce', 'lda', 'both'], default='both')
    p.add_argument('--epochs', type=int, default=10, help='ce: epochs')
    p.add_argument('--lr', type=float, default=0.001, help='ce: learning rate')
    p.add_argument('--momentum', type=float, default=0.9, help='ce: SGD momentum')
    p.add_argument('--batch_size', type=int, default=64, help='ce: batch size')
    p.add_argument('--shrinkage', type=float, default=0.01, help='lda: covariance shrinkage')
    p.add_argument('--prior', choices=['uniform', 'empirical'], default='uniform',
        help='lda: class prior in the bias')
    p.add_argument('--seed', type=int, default=0, help='seed of the mean-sample draw')
    p.add_argument('--eval_envs', choices=['local', 'local+global'], default='local+global')
    p.add_argument('--eval_subsample', type=int, default=0,
        help='cap every evaluation split at N evenly spaced images (0 = all)')
    p.add_argument('--cache_dir', default='./'
                                          'cache')
    p.add_argument('--data_dir', default='./fedbr/data/CIFAR10')
    p.add_argument('--device', type=int, default=0)
    p.add_argument('--out_dir', default='./output/calibrate_head')
    opt = p.parse_args()

    device = opt.device if torch.cuda.is_available() else 'cpu'
    os.makedirs(opt.out_dir, exist_ok=True)
    dataset = None

    for ck_path in resolve_checkpoints(opt.checkpoint):
        t0 = time.time()
        ck = torch.load(ck_path, weights_only=False, map_location='cpu')
        args, hp = ck['args'], ck['model_hparams']
        run_name = os.path.basename(os.path.dirname(os.path.abspath(ck_path)))
        print('\n=== {}  ({}, seed {})'.format(ck_path, args['algorithm'], args['seed']))

        if dataset is None:
            dataset = load_dataset(args, opt.cache_dir, opt.data_dir)
            n_train = args['train_envs']
            test_envs = list(range(n_train, len(dataset)))
            splits = {}
            for i, env in enumerate(dataset):
                out, in_ = misc.split_dataset(
                    env, int(len(env) * args['holdout_fraction']),
                    misc.seed_hash(args['trial_seed'], i))
                splits[i] = {'in': in_, 'out': out}
            num_classes = ck['model_num_classes']

        cls = algorithms.get_algorithm_class(args['algorithm'])
        model = cls(ck['model_input_shape'], num_classes, ck['model_num_domains'], hp)
        model.load_state_dict(ck['model_dict'])
        model.to(device).eval()
        feat = feature_function(model, args['algorithm'])
        if not isinstance(model.classifier, torch.nn.Linear):
            raise NotImplementedError('only a linear classifier head is supported')
        W0, b0 = head_params(model.classifier)

        # Evaluation features, once per checkpoint.
        def _subsample(env):
            if not opt.eval_subsample or len(env) <= opt.eval_subsample:
                return env
            stride = max(1, len(env) // opt.eval_subsample)
            keys = list(range(0, len(env), stride))[:opt.eval_subsample]
            return torch.utils.data.Subset(env, keys)

        def _tensors(env):
            X = torch.stack([env[i][0] for i in range(len(env))])
            y = torch.tensor([int(env[i][1]) for i in range(len(env))])
            return X, y

        groups = {'local': [(i, 'out') for i in range(n_train)]}
        if opt.eval_envs == 'local+global':
            groups['global'] = [(i, 'in') for i in test_envs]
        eval_feats = {}
        for gname, specs in groups.items():
            eval_feats[gname] = []
            for i, split in specs:
                X, y = _tensors(_subsample(splits[i][split]))
                eval_feats[gname].append((featurize(feat, X, device), y))
        print('evaluation features: {} ({:.0f}s)'.format(
            {g: sum(len(y) for _, y in v) for g, v in eval_feats.items()}, time.time() - t0))

        def score(W, b):
            return {g: 100.0 * float(np.mean([head_accuracy(W, b, Z, y) for Z, y in v]))
                    for g, v in eval_feats.items()}

        baseline = score(W0, b0)
        result = {'checkpoint': ck_path, 'run': run_name, 'algorithm': args['algorithm'],
                  'seed': args['seed'], 'options': vars(opt), 'baseline': baseline, 'rows': []}
        header = '{:>4} {:>6} {:>6} | {:>9} {:>9} {:>7}'.format('M', 'n_V', 'method', 'local', 'global', 'd_local')
        print(header)
        print('{:>4} {:>6} {:>6} | {:>9.2f} {:>9.2f} {:>7}'.format(
            '-', '-', 'none', baseline['local'], baseline.get('global', float('nan')), ''))

        methods = ['ce', 'lda'] if opt.method == 'both' else [opt.method]
        for M in opt.M:
            g = torch.Generator().manual_seed(misc.seed_hash(opt.seed, M))
            Xs, Ys = [], []
            for i in range(n_train):
                X, Y = build_mean_samples(splits[i]['in'], opt.n_per_client, M, num_classes, g)
                Xs.append(X)
                Ys.append(Y)
            Zv = featurize(feat, torch.cat(Xs), device)
            Yv = torch.cat(Ys)
            for method in methods:
                if method == 'ce':
                    W, b = retrain_head_ce(W0, b0, Zv, Yv, opt.epochs, opt.lr, opt.batch_size,
                                           torch.Generator().manual_seed(opt.seed), opt.momentum)
                else:
                    try:
                        W, b = lda_head(Zv, Yv, opt.shrinkage, opt.prior)
                    except ValueError as e:
                        print('{:>4} {:>6} {:>6} | skipped: {}'.format(M, len(Zv), method, e))
                        continue
                acc = score(W, b)
                row = {'M': M, 'n_V': len(Zv), 'method': method, 'acc': acc,
                       'delta': {k: acc[k] - baseline[k] for k in acc}}
                result['rows'].append(row)
                print('{:>4} {:>6} {:>6} | {:>9.2f} {:>9.2f} {:>+7.2f}'.format(
                    M, len(Zv), method, acc['local'], acc.get('global', float('nan')), row['delta']['local']))

        out_path = os.path.join(opt.out_dir, '{}.json'.format(run_name))
        with open(out_path, 'w') as f:
            json.dump(result, f, indent=1)
        print('wrote {}  ({:.0f}s)'.format(out_path, time.time() - t0))
    return 0


if __name__ == '__main__':
    sys.exit(main())