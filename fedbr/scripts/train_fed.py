# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

import argparse
import collections
from copy import deepcopy
import json
import os
import random
import sys
import time
import uuid

import numpy as np
import PIL
import torch
import torchvision
import torch.utils.data
import torch.nn.functional as F
import copy

from torch.utils.data import Subset

from fedbr import datasets
from fedbr import hparams_registry
from fedbr import algorithms
from fedbr.lib import misc
from fedbr.lib.fast_data_loader import InfiniteDataLoader, FastDataLoader
from fedbr.algorithms_fed import FedAvg, FedGroupDRO
import matplotlib.pyplot as plt
from torchvision.datasets import CIFAR100, CIFAR10
from torchvision import transforms
from fedbr.generative.datasets import GenerativeDataset, data_transforms_generative

def get_augmentation_mean_data(envs, device, weights, bs=32):

    augmentation_data = []
    
    for i in range(bs):
        chosen_env = torch.randint(0, len(envs), (1,))
        env, env_weights = envs[chosen_env]
        indexs = torch.randint(0, len(env), (10,))
        current_aug_data = torch.zeros_like(env[0][0])
        current_aug_data = current_aug_data.unsqueeze(0)
        for index in indexs:
            current_aug_data += env[index][0] / len(indexs)
        augmentation_data.append(current_aug_data.to(device))

    return augmentation_data

def get_augmentation_proxy_data(env, bs=32):
    augmentation_data = []
    for i in range(bs):
        indexs = torch.randint(0, len(env), (10,))
        current_aug_data = torch.zeros_like(env[0][0])
        current_aug_data = current_aug_data.unsqueeze(0)
        for index in indexs:
            current_aug_data += env[index][0] / len(indexs)
        augmentation_data.append(current_aug_data.to(device))
    return augmentation_data


def get_augmentation_fedmix_data(envs, device, batchsize, M = 10, class_num = 10):
    augmentation_data = []
    envs_lens = batchsize
    for m in range(envs_lens):
        env = envs[torch.randint(0, len(envs), (1,))][0]
        indexs = torch.randint(0, len(env), (M,))
        current_aug_data = torch.zeros_like(env[0][0])
        current_aug_label = torch.zeros((class_num,))
        current_aug_data = current_aug_data.unsqueeze(0)
        for index in indexs:
            current_aug_data += 1.0 * env[index][0] / len(indexs)
            current_aug_label[env[index][1]] += 1.0 / len(indexs)
        augmentation_data.append((current_aug_data.to(device), current_aug_label.to(device)))
    return augmentation_data






if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Domain generalization')
    parser.add_argument('--data_dir', type=str)
    parser.add_argument('--dataset', type=str, default="RotatedMNIST")
    parser.add_argument('--algorithm', type=str, default="ERM")
    parser.add_argument('--task', type=str, default="domain_generalization",
        choices=["domain_generalization", "domain_adaptation"])
    parser.add_argument('--hparams', type=str,
        help='JSON-serialized hparams dict')
    parser.add_argument('--hparams_seed', type=int, default=0,
        help='Seed for random hparams (0 means "default hparams")')
    parser.add_argument('--trial_seed', type=int, default=0,
        help='Trial number (used for seeding split_dataset and '
        'random_hparams).')
    parser.add_argument('--seed', type=int, default=0,
        help='Seed for everything else')
    parser.add_argument('--steps', type=int, default=None,
        help='Number of steps. Default is dataset-dependent.')
    parser.add_argument('--checkpoint_freq', type=int, default=None,
        help='Checkpoint every N steps. Default is dataset-dependent.')
    parser.add_argument('--train_envs', type=int, default=10)
    parser.add_argument('--output_dir', type=str, default="train_output")
    parser.add_argument('--holdout_fraction', type=float, default=0.2)
    parser.add_argument('--uda_holdout_fraction', type=float, default=0,
        help="For domain adaptation, % of test to use unlabeled for training.")
    parser.add_argument('--skip_model_save', action='store_true')
    parser.add_argument('--save_model_every_checkpoint', action='store_true')
    parser.add_argument('--local_steps', type=int, default=20)
    parser.add_argument('--device', type=int, default=0)
    parser.add_argument('--fedmix_lambda', type=float, default=0.1)
    parser.add_argument('--use_Mixture', action='store_true')
    parser.add_argument('--use_Mixup', action='store_true')
    parser.add_argument('--virtual_set', type=str, default='style_GAN_init_28_c100_200')
    parser.add_argument('--cache_dir', type=str, default=None,
        help='Cache the (slow) non-iid split + rotation of the dataset here '
             'and reuse it across runs with the same dataset/clients/seed.')
    parser.add_argument('--n_workers', type=int, default=None,
        help='DataLoader workers per loader. The default (8) spawns 8 workers '
             'for each of the ~30 loaders, which exhausts /dev/shm in most '
             'containers; the datasets are in-memory tensors, so 0 is both '
             'safe and usually fastest.')
    parser.add_argument('--eval_subsample', type=int, default=0,
        help='Cap every evaluation loader at N evenly-spaced samples. 0 (the '
             'default) evaluates the full splits, which is what the paper '
             'reports; a small value makes a smoke test finish in seconds.')
    parser.add_argument('--eval_test_only', action='store_true',
        help='Only evaluate the held-out client environments. The paper only '
             'reports accuracy on the local test datasets, and evaluating the '
             'training environments as well roughly triples the eval cost.')
    args = parser.parse_args()

    # If we ever want to implement checkpointing, just persist these values
    # every once in a while, and then load them from disk here.
    # start_step = 30600
    # algorithm_dict = torch.load('output-cifar10-rotate/vhl-200/model.pkl')['model_dict']
    start_step = 0
    algorithm_dict = None

    os.makedirs(args.output_dir, exist_ok=True)
    sys.stdout = misc.Tee(os.path.join(args.output_dir, 'out.txt'))
    sys.stderr = misc.Tee(os.path.join(args.output_dir, 'err.txt'))

    print("Environment:")
    print("\tPython: {}".format(sys.version.split(" ")[0]))
    print("\tPyTorch: {}".format(torch.__version__))
    print("\tTorchvision: {}".format(torchvision.__version__))
    print("\tCUDA: {}".format(torch.version.cuda))
    print("\tCUDNN: {}".format(torch.backends.cudnn.version()))
    print("\tNumPy: {}".format(np.__version__))
    print("\tPIL: {}".format(PIL.__version__))

    print('Args:')
    for k, v in sorted(vars(args).items()):
        print('\t{}: {}'.format(k, v))

    if args.hparams_seed == 0:
        hparams = hparams_registry.default_hparams(args.algorithm, args.dataset)
    else:
        hparams = hparams_registry.random_hparams(args.algorithm, args.dataset,
            misc.seed_hash(args.hparams_seed, args.trial_seed))
    if args.hparams:
        hparams.update(json.loads(args.hparams))

    print('HParams:')
    for k, v in sorted(hparams.items()):
        print('\t{}: {}'.format(k, v))

    hparams['use_Mixture'] = args.use_Mixture
    hparams['use_Mixup'] = args.use_Mixup
    # print(hparams['use_Mixture'])

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

    if torch.cuda.is_available():
        device = args.device
    else:
        device = "cpu"
    
    print('device: {}'.format(device))

    if args.dataset in vars(datasets):
        cache_path = None
        if args.cache_dir:
            os.makedirs(args.cache_dir, exist_ok=True)
            cache_path = os.path.join(args.cache_dir, '{}_envs{}_seed{}.pt'.format(
                args.dataset, args.train_envs, args.seed))
        if cache_path is not None and os.path.exists(cache_path):
            print('Loading cached dataset from {}'.format(cache_path))
            dataset = torch.load(cache_path, weights_only=False)
        else:
            dataset = vars(datasets)[args.dataset](args.data_dir,
                args.train_envs, hparams)
            if cache_path is not None:
                print('Caching dataset to {}'.format(cache_path))
                torch.save(dataset, cache_path)
        if cache_path is not None:
            # Building the dataset consumes RNG draws, so re-seed here to make
            # a cached run and a freshly-built run follow the same stream.
            random.seed(args.seed)
            np.random.seed(args.seed)
            torch.manual_seed(args.seed)
        args.test_envs = [i for i in range(args.train_envs, len(dataset))]
        if args.n_workers is not None:
            dataset.N_WORKERS = args.n_workers
    else:
        raise NotImplementedError
    
    if 'FedBR' in args.algorithm and args.use_Mixture:
        # proxy_mean = [0.5070751592371323, 0.48654887331495095, 0.4409178433670343]
        # proxy_std = [0.2673342858792401, 0.2564384629170883, 0.27615047132568404]
        if 'CIFAR100' in args.dataset:
            proxy_mean = [0.48836562, 0.48134598, 0.4451678]
            proxy_std = [0.24833508, 0.24547848, 0.26617324]
            transform_proxy = transforms.Compose([
                    transforms.ToTensor(),
                    # transforms.Resize((28, 28)),
                    transforms.Normalize(proxy_mean, proxy_std)
                ])
            proxy_dataset = CIFAR10(args.data_dir, train=True, download=True, transform=transform_proxy)
        elif 'CIFAR10' in args.dataset:
            proxy_mean = [0.5070751592371323, 0.48654887331495095, 0.4409178433670343]
            proxy_std = [0.2673342858792401, 0.2564384629170883, 0.27615047132568404]
            transform_proxy = transforms.Compose([
                    transforms.ToTensor(),
                    # transforms.Resize((28, 28)),
                    transforms.Normalize(proxy_mean, proxy_std)
                ])
            proxy_dataset = CIFAR100(args.data_dir, train=True, download=True, transform=transform_proxy)
        else:
            raise NotImplementedError
    elif 'VHL' in args.algorithm:
        if 'MNIST' in args.dataset:
            GENERETIVE_MEAN, GENERETIVE_STD, proxy_train_transform, proxy_test_transform = data_transforms_generative((28, 28))
            proxy_dataset = GenerativeDataset(None, args.virtual_set, transform=proxy_train_transform, image_resolution=28)
            # print(proxy_dataset[0][0].shape)
            proxy_loader = InfiniteDataLoader(proxy_dataset, None, 32, num_workers=8)
            proxy_iter = iter(proxy_loader)
        else:
            GENERETIVE_MEAN, GENERETIVE_STD, proxy_train_transform, proxy_test_transform = data_transforms_generative((32, 32))
            proxy_dataset = GenerativeDataset(None, args.virtual_set, transform=proxy_train_transform, image_resolution=32)
            # print(proxy_dataset[0][0].shape)
            proxy_loader = InfiniteDataLoader(proxy_dataset, None, 32, num_workers=8)
            proxy_iter = iter(proxy_loader)

    # Split each env into an 'in-split' and an 'out-split'. We'll train on
    # each in-split except the test envs, and evaluate on all splits.

    # To allow unsupervised domain adaptation experiments, we split each test
    # env into 'in-split', 'uda-split' and 'out-split'. The 'in-split' is used
    # by collect_results.py to compute classification accuracies.  The
    # 'out-split' is used by the Oracle model selectino method. The unlabeled
    # samples in 'uda-split' are passed to the algorithm at training time if
    # args.task == "domain_adaptation". If we are interested in comparing
    # domain generalization and domain adaptation results, then domain
    # generalization algorithms should create the same 'uda-splits', which will
    # be discared at training.
    in_splits = []
    out_splits = []
    uda_splits = []
    for env_i, env in enumerate(dataset):
        uda = []

        out, in_ = misc.split_dataset(env,
            int(len(env)*args.holdout_fraction),
            misc.seed_hash(args.trial_seed, env_i))


        if env_i in args.test_envs:
            uda, in_ = misc.split_dataset(in_,
                int(len(in_)*args.uda_holdout_fraction),
                misc.seed_hash(args.trial_seed, env_i))

        if hparams['class_balanced']:
            in_weights = misc.make_weights_for_balanced_classes(in_)
            out_weights = misc.make_weights_for_balanced_classes(out)
            if uda is not None:
                uda_weights = misc.make_weights_for_balanced_classes(uda)
        else:
            in_weights, out_weights, uda_weights = None, None, None
        in_splits.append((in_, in_weights))
        out_splits.append((out, out_weights))
        if len(uda):
            uda_splits.append((uda, uda_weights))

    if args.task == "domain_adaptation" and len(uda_splits) == 0:
        raise ValueError("Not enough unlabeled samples for domain adaptation.")

    # print(args.test_envs, len(in_splits))

    train_loaders = [InfiniteDataLoader(
        dataset=env,
        weights=env_weights,
        batch_size=hparams['batch_size'],
        num_workers=dataset.N_WORKERS)
        for i, (env, env_weights) in enumerate(in_splits)
        if i not in args.test_envs]

    def _subsample(env):
        if not args.eval_subsample or len(env) <= args.eval_subsample:
            return env
        stride = max(1, len(env) // args.eval_subsample)
        return Subset(env, list(range(0, len(env), stride))[:args.eval_subsample])

    train_loaders_fast = [FastDataLoader(
        dataset=_subsample(env),
        batch_size=hparams['batch_size'],
        num_workers=dataset.N_WORKERS)
        for i, (env, env_weights) in enumerate(in_splits)
        if i not in args.test_envs]

    # uda_loaders = [InfiniteDataLoader(
    #     dataset=env,
    #     weights=env_weights,
    #     batch_size=hparams['batch_size'],
    #     num_workers=dataset.N_WORKERS)
    #     for i, (env, env_weights) in enumerate(uda_splits)
    #     if i in args.test_envs]

    def _keep_env(i):
        return (not args.eval_test_only) or (i in args.test_envs)

    eval_specs = []
    eval_specs += [('env{0}_in'.format(str(i).zfill(2)), env)
        for i, (env, _) in enumerate(in_splits) if _keep_env(i)]
    eval_specs += [('env{0}_out'.format(str(i).zfill(2)), env)
        for i, (env, _) in enumerate(out_splits) if _keep_env(i)]
    eval_specs += [('env{0}_uda'.format(str(i).zfill(2)), env)
        for i, (env, _) in enumerate(uda_splits)]

    eval_specs = [(name, _subsample(env)) for name, env in eval_specs]

    eval_loader_names = [name for name, _ in eval_specs]
    eval_loaders = [FastDataLoader(
        dataset=env,
        batch_size=64,
        num_workers=dataset.N_WORKERS)
        for _, env in eval_specs]
    eval_weights = [None for _ in eval_specs]

    algorithm_class = algorithms.get_algorithm_class(args.algorithm)
    algorithm = algorithm_class(dataset.input_shape, dataset.num_classes,
        len(dataset) - len(args.test_envs), hparams)
    
    algorithm.to(device)

    if args.algorithm == 'GroupDRO':

        algorithm = FedGroupDRO(algorithm)
        local_algorithms = [FedGroupDRO(algorithm_class(dataset.input_shape, dataset.num_classes, len(dataset) - len(args.test_envs), hparams).to(device)) for _ in range(10)]
    else:

        algorithm = FedAvg(algorithm)

        local_algorithms = [FedAvg(algorithm_class(dataset.input_shape, dataset.num_classes, len(dataset) - len(args.test_envs), hparams).to(device)) for _ in range(min(10, args.train_envs))]

    if algorithm_dict is not None:
        algorithm.load_state_dict(algorithm_dict)

    for local_algorithm in local_algorithms:
        local_algorithm = copy.deepcopy(algorithm)

    if args.algorithm == 'DANN' or args.algorithm == 'CDANN':
        for i, local_algorithm in enumerate(local_algorithms):
            local_algorithm.algorithm.set_disc_label(i) 


    train_minibatches_iterators = [iter(train_loader) for train_loader in train_loaders]
    checkpoint_vals = collections.defaultdict(lambda: [])

    steps_per_epoch = min([len(env)/hparams['batch_size'] for env,_ in in_splits])
    print([len(env) for env,_ in in_splits])
    print(steps_per_epoch)

    n_steps = args.steps or dataset.N_STEPS
    checkpoint_freq = args.checkpoint_freq or dataset.CHECKPOINT_FREQ

    def save_checkpoint(filename):
        if args.skip_model_save:
            return
        save_dict = {
            "args": vars(args),
            "model_input_shape": dataset.input_shape,
            "model_num_classes": dataset.num_classes,
            "model_num_domains": len(dataset) - len(args.test_envs),
            "model_hparams": hparams,
            "model_dict": algorithm.state_dict()
        }
        torch.save(save_dict, os.path.join(args.output_dir, filename))


    last_results_keys = None
    uda_device = None
    train_losses = []
    if args.algorithm.startswith('FedBR'):
        if args.use_Mixture:
            uda_device = get_augmentation_proxy_data(proxy_dataset, hparams['batch_size'])
        else:
            weights = [1.0 / args.train_envs] * args.train_envs            
            uda_device = get_augmentation_mean_data([ (env, env_weights)
            for i, (env, env_weights) in enumerate(in_splits)
            if i not in args.test_envs], device, weights, hparams['batch_size'])
        # uda_device = get_augmentation_proxy_data(proxy_dataset, hparams['batch_size'])
    elif args.algorithm == 'VHL':
        uda_device = next(proxy_iter)
        

    N = min(10, args.train_envs)
    chosen_clients = torch.multinomial(torch.ones((args.train_envs, )) / args.train_envs, min(10, args.train_envs))
    # chosen_clients = [i for i in range(10)]

    for step in range(start_step, n_steps):
        step_start_time = time.time()
        if args.algorithm == 'VHL':
            uda_device = next(proxy_iter)
        minibatches_devices = [[[x.to(device) for x in next(train_minibatches_iterators[chosen_clients[i]])]] for i in range(N)]

        step_vals = {'loss': 0, 'penalty': 0}
        if args.algorithm == 'FedMix' or args.algorithm == 'NaiveMix':
            uda_device = get_augmentation_fedmix_data([ (env, env_weights)
                for i, (env, env_weights) in enumerate(in_splits)
                if i not in args.test_envs], device, hparams['batch_size'], class_num=dataset.num_classes)

        for local_algorithm_i, local_algorithm in enumerate(local_algorithms):
            local_algorithm.algorithm.to(device)
            step_val = local_algorithm.update(minibatches_devices[local_algorithm_i], uda_device)
            for k, v in step_vals.items():
                if k in step_val:
                    step_vals[k] += step_val[k] / len(local_algorithms)
            if len(train_losses) < len(local_algorithms):
                train_losses.append(step_val['loss'])


        if step % args.local_steps == 0:

            chosen_clients = torch.multinomial(torch.ones((args.train_envs, )) / args.train_envs, min(10, args.train_envs))
            # chosen_clients = [i for i in range(10)]

            algorithm.algorithm.to(device)

            weights = np.array([local_algorithm.p for local_algorithm in local_algorithms])
            weights = weights / sum(weights)
            

            if args.algorithm == 'Moon':
                old_features = []
                old_projection_heads = []
                for i, local_algorithm in enumerate(local_algorithms):
                    old_features.append(deepcopy(local_algorithm.algorithm.featurizer))
                    old_projection_heads.append(deepcopy(local_algorithm.algorithm.projection_head))
            if args.algorithm == 'FedCM_algo':
                Delta = [torch.zeros_like(p).to('cpu') for p in algorithm.algorithm.parameters()]
                algorithm_copy = copy.deepcopy(algorithm.algorithm)
            # for FedBR + FedCM
            # elif args.algorithm == 'FedBR':
            #     Delta_disc = [torch.zeros_like(p).to('cpu') for p in algorithm.algorithm.discriminator.parameters()]
            #     Delta_gen = [torch.zeros_like(p).to('cpu') for p in (list(algorithm.algorithm.featurizer.parameters()) +
            #     list(algorithm.algorithm.classifier.parameters()))]
            #     algorithm_copy = copy.deepcopy(algorithm.algorithm)


            algorithm.global_update([local_algorithm.gradients for local_algorithm in local_algorithms], weights, {'global_lr': 1.0})
            
            for i, local_algorithm in enumerate(local_algorithms):
                local_algorithm.copy_from(algorithm)
                
                if args.algorithm.startswith('FedBR') or args.algorithm == 'Moon' or args.algorithm == 'FedNTD':
                    local_algorithm.algorithm.if_updated = True
                if args.algorithm == 'FedProx_algo':
                    local_algorithm.algorithm.reset_optimizer()
            if args.algorithm == 'FedCM_algo':
                for i, (p, g) in enumerate(zip(algorithm.algorithm.parameters(), algorithm_copy.parameters())):
                    Delta[i] = (g.to('cpu') - p.to('cpu')) / (hparams['lr'] * args.local_steps)
                for local_algorithm in local_algorithms:
                    for i, p in enumerate(Delta):
                        local_algorithm.algorithm.Delta[i].data = Delta[i].data
            # for FedBR + FedCM
            # elif args.algorithm == 'FedBR':
            #     for i, (p, g) in enumerate(zip(algorithm.algorithm.discriminator.parameters(), algorithm_copy.discriminator.parameters())):
            #         Delta_disc[i] = (g.to('cpu') - p.to('cpu')) / (hparams['lr'] * args.local_steps)
            #     for i, (p, g) in enumerate(zip((list(algorithm.algorithm.featurizer.parameters()) +
            #             list(algorithm.algorithm.classifier.parameters())), (list(algorithm_copy.featurizer.parameters()) +
            #             list(algorithm_copy.classifier.parameters())))):
            #         Delta_gen[i] = (g.to('cpu') - p.to('cpu')) / (hparams['lr'] * args.local_steps)
            #     for local_algorithm in local_algorithms:
            #         for i, p in enumerate(Delta_disc):
            #             local_algorithm.algorithm.Delta_disc[i].data = Delta_disc[i].data
            #         for i, p in enumerate(Delta_gen):
            #             local_algorithm.algorithm.Delta_gen[i].data = Delta_gen[i].data
            
            if args.algorithm == 'Moon':
                for i, local_algorithm in enumerate(local_algorithms):
                    local_algorithm.algorithm.previous_featurizer = old_features[i]
                    local_algorithm.algorithm.previous_projection_head = old_projection_heads[i]

            if args.algorithm == 'DANN' or args.algorithm == 'CDANN':
                for i, local_algorithm in enumerate(local_algorithms):
                    local_algorithm.algorithm.set_disc_label(i) 

            # if args.algorithm.startswith('FedBR'):
            #     if args.use_Mixture:
            #         uda_device = get_augmentation_proxy_data(proxy_dataset, hparams['batch_size'])
            #     else:
            #         weights = [1.0 / args.train_envs] * args.train_envs            
            #         uda_device = get_augmentation_mean_data([ (env, env_weights)
            #         for i, (env, env_weights) in enumerate(in_splits)
            #         if i not in args.test_envs], device, weights, hparams['batch_size'])

        checkpoint_vals['step_time'].append(time.time() - step_start_time)


        if (step % checkpoint_freq == 0) or (step == n_steps - 1):
            algorithm.algorithm.to(device)
            losses = [misc.loss(algorithm, loader, device) for loader in train_loaders_fast]
            step_vals['loss'] = sum(losses) / len(losses)

            for key, val in step_vals.items():
                checkpoint_vals[key].append(val)

            results = {
                'step': step,
                'epoch': step / steps_per_epoch,
            }

            for key, val in checkpoint_vals.items():
                results[key] = np.mean(val)

            evals = zip(eval_loader_names, eval_loaders, eval_weights)
            for name, loader, weights in evals:
                acc = misc.accuracy(algorithm, loader, weights, device)
                results[name+'_acc'] = acc

            results['mem_gb'] = torch.cuda.max_memory_allocated() / (1024.*1024.*1024.)

            results_keys = sorted(results.keys())
            if results_keys != last_results_keys:
                misc.print_row(results_keys, colwidth=12)
                last_results_keys = results_keys
            misc.print_row([results[key] for key in results_keys],
                colwidth=12)

            results.update({
                'hparams': hparams,
                'args': vars(args)
            })

            epochs_path = os.path.join(args.output_dir, 'results.jsonl')
            with open(epochs_path, 'a') as f:
                f.write(json.dumps(results, sort_keys=True) + "\n")

            algorithm_dict = algorithm.state_dict()
            start_step = step + 1
            checkpoint_vals = collections.defaultdict(lambda: [])

            if args.save_model_every_checkpoint:
                save_checkpoint(f'model.pkl')

            train_losses = []




    save_checkpoint('model.pkl')

    with open(os.path.join(args.output_dir, 'done'), 'w') as f:
        f.write('done')

