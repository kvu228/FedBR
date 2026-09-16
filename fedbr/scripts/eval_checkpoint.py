"""Re-evaluate a saved model.pkl on every environment / split.

train_fed.py evaluates two kinds of held-out data and it is not obvious which
one the paper's tables report:

  * train-client out-splits  (env00..09 _out)  - each training client's own 20%
    held-out data, with that client's label skew and rotation mix. The natural
    reading of the paper's "mean accuracy on all local test datasets".
  * test environments        (env10..19 _in)   - ten copies of the CIFAR10 test
    set, each rotated by one fixed angle. Balanced and covering every angle,
    i.e. a "balanced global test set" in the paper's Table 6 wording.

`--eval_test_only` drops the first group from results.jsonl, so this script
rebuilds the exact same splits from the cached dataset and scores a checkpoint
on both. It reports the final-round model, not the top-5-rounds mean.

Usage:
    python -m fedbr.scripts.eval_checkpoint output/cifar10/fedavg/model.pkl
"""

import argparse
import os
import random
import sys

import numpy as np
import torch

from fedbr import algorithms, datasets
from fedbr.lib import misc
from fedbr.lib.fast_data_loader import FastDataLoader


def load_dataset(args, cache_dir, data_dir):
    cache = os.path.join(cache_dir, '{}_envs{}_seed{}.pt'.format(
        args['dataset'], args['train_envs'], args['seed']))
    if os.path.exists(cache):
        print('dataset: {}'.format(cache))
        return torch.load(cache, weights_only=False)
    # Same seeding as train_fed.py, so the split is reproduced exactly.
    print('dataset: rebuilding (no cache at {})'.format(cache))
    random.seed(args['seed'])
    np.random.seed(args['seed'])
    torch.manual_seed(args['seed'])
    return vars(datasets)[args['dataset']](data_dir, args['train_envs'], {})


def main():
    p = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('checkpoint', nargs='+', help='one or more model.pkl')
    p.add_argument('--cache_dir', default='./cache')
    p.add_argument('--data_dir', default='./fedbr/data/CIFAR10')
    p.add_argument('--device', type=int, default=0)
    p.add_argument('--n_workers', type=int, default=0)
    opt = p.parse_args()

    device = opt.device if torch.cuda.is_available() else 'cpu'
    dataset = None

    for ck_path in opt.checkpoint:
        ck = torch.load(ck_path, weights_only=False)
        args, hp = ck['args'], ck['model_hparams']
        print('\n=== {}  ({}, seed {})'.format(ck_path, args['algorithm'],
                                               args['seed']))

        if dataset is None:
            dataset = load_dataset(args, opt.cache_dir, opt.data_dir)
            n_train = args['train_envs']
            test_envs = list(range(n_train, len(dataset)))

            # identical to train_fed.py's split
            splits = {}
            for i, env in enumerate(dataset):
                out, in_ = misc.split_dataset(
                    env, int(len(env) * args['holdout_fraction']),
                    misc.seed_hash(args['trial_seed'], i))
                splits[i] = {'in': in_, 'out': out}

        cls = algorithms.get_algorithm_class(args['algorithm'])
        model = cls(ck['model_input_shape'], ck['model_num_classes'],
                    ck['model_num_domains'], hp)
        model.load_state_dict(ck['model_dict'])
        model.to(device).eval()

        groups = [
            ('train-client out (local test)', range(n_train), 'out'),
            ('train-client in  (train data)', range(n_train), 'in'),
            ('test env in  (what summarize reports)', test_envs, 'in'),
            ('test env out', test_envs, 'out'),
        ]
        for label, envs, split in groups:
            accs = []
            for i in envs:
                loader = FastDataLoader(splits[i][split], 64, opt.n_workers)
                accs.append(100.0 * misc.accuracy(model, loader, None, device))
            per_env = ' '.join('{:5.1f}'.format(a) for a in accs)
            print('{:40s} mean {:6.2f}   [{}]'.format(label, np.mean(accs),
                                                       per_env))
    return 0


if __name__ == '__main__':
    sys.exit(main())