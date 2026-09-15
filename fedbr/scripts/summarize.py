"""Summarize FedBR runs the way the paper's tables do.

For every run directory containing a `results.jsonl`, this computes

  * Acc (%)          - the mean of the maximum 5 accuracies over communication
                       rounds, on the held-out client test environments
                       (Table 1 / 2 / 4 / 5 / 8 / 9 of the paper).
  * Rounds for X%    - the first communication round whose accuracy reaches the
                       threshold X, plus the speed-up relative to the baseline
                       run (FedAvg by default), printed as "(1.3X)".

Accuracy per round follows the DomainBed convention used by the repo's own
`model_selection.py`: the `in` split of each test environment. `--split full`
reweights `in`/`out` back into the complete test set instead.

Usage:
    python -m fedbr.scripts.summarize output/cifar10 --threshold 55
"""

import argparse
import json
import os
import sys
from collections import OrderedDict


def load_records(run_dir):
    path = os.path.join(run_dir, 'results.jsonl')
    if not os.path.exists(path):
        return []
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                # a run killed mid-write leaves a partial last line
                continue
    return records


def test_env_ids(record):
    """Environment indices held out as local test datasets."""
    args = record.get('args', {})
    if 'test_envs' in args and args['test_envs']:
        return list(args['test_envs'])
    # train_fed.py always holds out the environments after the training ones
    n_train = args.get('train_envs', 10)
    ids = []
    i = n_train
    while 'env{0}_in_acc'.format(str(i).zfill(2)) in record:
        ids.append(i)
        i += 1
    return ids


def record_accuracy(record, split, holdout_fraction):
    accs = []
    for i in test_env_ids(record):
        in_key = 'env{0}_in_acc'.format(str(i).zfill(2))
        out_key = 'env{0}_out_acc'.format(str(i).zfill(2))
        if in_key not in record:
            continue
        if split == 'full' and out_key in record:
            accs.append((1.0 - holdout_fraction) * record[in_key]
                        + holdout_fraction * record[out_key])
        else:
            accs.append(record[in_key])
    if not accs:
        return None
    return sum(accs) / len(accs)


def summarize_run(run_dir, split, top_k, thresholds):
    records = load_records(run_dir)
    if not records:
        return None

    local_steps = records[0].get('args', {}).get('local_steps', 1) or 1
    holdout_fraction = records[0].get('args', {}).get('holdout_fraction', 0.2)

    curve = []  # (round, acc)
    for r in records:
        acc = record_accuracy(r, split, holdout_fraction)
        if acc is None:
            continue
        curve.append((r['step'] / float(local_steps), 100.0 * acc))
    if not curve:
        return None

    accs = sorted((a for _, a in curve), reverse=True)
    top = accs[:top_k]

    rounds_to = OrderedDict()
    for t in thresholds:
        hit = next((rnd for rnd, a in curve if a >= t), None)
        rounds_to[t] = hit

    return {
        'name': os.path.basename(os.path.normpath(run_dir)),
        'dir': run_dir,
        'acc': sum(top) / len(top),
        'best': accs[0],
        'final': curve[-1][1],
        'rounds_done': curve[-1][0],
        'rounds_to': rounds_to,
        'curve': curve,
        'done': os.path.exists(os.path.join(run_dir, 'done')),
        'algorithm': records[0].get('args', {}).get('algorithm', '?'),
        'seed': records[0].get('args', {}).get('seed', '?'),
    }


def find_runs(roots):
    runs = []
    for root in roots:
        if os.path.exists(os.path.join(root, 'results.jsonl')):
            runs.append(root)
            continue
        for dirpath, _dirnames, filenames in os.walk(root):
            if 'results.jsonl' in filenames:
                runs.append(dirpath)
    return sorted(set(runs))


def fmt_rounds(value, baseline):
    if value is None:
        return '-'
    cell = '{:.0f}'.format(value)
    if baseline:
        cell += ' ({:.1f}X)'.format(baseline / value) if value else ''
    return cell


def main():
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('roots', nargs='+',
        help='Run directories, or a parent directory to scan recursively.')
    parser.add_argument('--threshold', type=float, nargs='+', default=[55.0],
        help='Target accuracies for the "rounds to reach" columns '
             '(paper uses 55 and 60 for CIFAR10).')
    parser.add_argument('--top_k', type=int, default=5,
        help='Average the top-K rounds (paper: 5).')
    parser.add_argument('--split', choices=['in', 'full'], default='in',
        help="'in' = DomainBed convention (in-split of each test env); "
             "'full' = reweighted in+out.")
    parser.add_argument('--baseline', type=str, default='fedavg',
        help='Run name used as the 1.0X reference for the speed-up column.')
    parser.add_argument('--csv', type=str, default=None,
        help='Also write the table as CSV to this path.')
    args = parser.parse_args()

    runs = find_runs(args.roots)
    if not runs:
        print('No results.jsonl found under: {}'.format(', '.join(args.roots)),
              file=sys.stderr)
        return 1

    rows = [r for r in (summarize_run(d, args.split, args.top_k, args.threshold)
                        for d in runs) if r]
    if not rows:
        print('No usable records found.', file=sys.stderr)
        return 1

    base = next((r for r in rows if r['name'] == args.baseline), None)

    header = ['Run', 'Algorithm', 'Acc (%)', 'Best (%)', 'Rounds run']
    header += ['Rounds for {:g}%'.format(t) for t in args.threshold]
    header += ['Finished']

    table = []
    for r in rows:
        row = [r['name'], r['algorithm'], '{:.2f}'.format(r['acc']),
               '{:.2f}'.format(r['best']), '{:.0f}'.format(r['rounds_done'])]
        for t in args.threshold:
            base_rounds = base['rounds_to'][t] if base else None
            row.append(fmt_rounds(r['rounds_to'][t], base_rounds))
        row.append('yes' if r['done'] else 'NO (partial)')
        table.append(row)

    widths = [max(len(h), *(len(row[i]) for row in table))
              for i, h in enumerate(header)]
    sep = '| ' + ' | '.join('-' * w for w in widths) + ' |'
    print('| ' + ' | '.join(h.ljust(w) for h, w in zip(header, widths)) + ' |')
    print(sep)
    for row in table:
        print('| ' + ' | '.join(c.ljust(w) for c, w in zip(row, widths)) + ' |')

    print('\nAcc (%) = mean of the top-{} rounds, {} split of the held-out '
          'client environments.'.format(args.top_k, args.split))
    if base is None and args.baseline:
        print('No run named "{}" found, so no speed-up column.'.format(
            args.baseline))

    if args.csv:
        import csv
        with open(args.csv, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(table)
        print('Wrote {}'.format(args.csv))
    return 0


if __name__ == '__main__':
    sys.exit(main())
