"""Summarize FedBR runs the way the paper's tables do.

For every run directory containing a `results.jsonl`, this computes

  * Acc (%)          - the mean of the maximum 5 accuracies over communication
                       rounds (Table 1 / 2 / 4 / 5 / 8 / 9 of the paper).
  * Rounds for X%    - the first communication round whose accuracy reaches the
                       threshold X, plus the speed-up relative to the baseline
                       run (FedAvg by default), printed as "(1.3X)".

Two accuracies are tracked, selected with --metric:

  local   (default)  the 20% held-out split of every *training* client, i.e.
                     data with that client's own label skew and rotation mix.
                     This is the paper's "mean accuracy on all local test
                     datasets" (Figure 5) and what Table 1 reports.
  global             the in-split of every held-out *test* environment: ten
                     copies of the CIFAR10 test set, each rotated by one fixed
                     angle. Balanced and covering every angle -- the "balanced
                     global test datasets" of the paper's Table 6, where the
                     same FedAvg scores 46.37 instead of Table 1's 58.99.

Whichever is primary, the other is shown as a secondary column when the run
logged it (train_fed.py --eval_envs local+global).

Usage:
    python -m fedbr.scripts.summarize output/cifar10 --threshold 55 60
"""

import argparse
import json
import os
import sys
from collections import OrderedDict

METRICS = OrderedDict([
    ('local', "20% held-out split of each training client "
              "(the paper's 'local test datasets')"),
    ('global', "in-split of each held-out test environment "
               "(balanced, one rotation angle each)"),
])


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


def metric_keys(record, metric):
    args = record.get('args', {})
    n_train = args.get('train_envs', 10)
    if metric == 'local':
        envs = range(n_train)
        split = 'out'
    else:
        envs = args.get('test_envs') or range(n_train, n_train + 10)
        split = 'in'
    return ['env{0}_{1}_acc'.format(str(i).zfill(2), split) for i in envs]


def accuracy_curve(records, metric, local_steps):
    """[(round, acc%)] -- only rounds where every env of the metric is logged,
    so a partially evaluated run never averages over fewer environments."""
    curve = []
    for r in records:
        keys = metric_keys(r, metric)
        if not keys or any(k not in r for k in keys):
            continue
        acc = sum(r[k] for k in keys) / len(keys)
        curve.append((r['step'] / float(local_steps), 100.0 * acc))
    return curve


def top_k_mean(curve, k):
    accs = sorted((a for _, a in curve), reverse=True)[:k]
    return sum(accs) / len(accs) if accs else None


def summarize_run(run_dir, metric, top_k, thresholds):
    records = load_records(run_dir)
    if not records:
        return None

    args = records[0].get('args', {})
    local_steps = args.get('local_steps', 1) or 1
    other = 'global' if metric == 'local' else 'local'

    curve = accuracy_curve(records, metric, local_steps)
    other_curve = accuracy_curve(records, other, local_steps)

    # train_fed.py logs the mean seconds/step over each checkpoint interval
    # (training only, evaluation excluded). Projected to 1000 rounds this is
    # the number to compare GPUs on.
    step_times = [r['step_time'] for r in records if 'step_time' in r]
    hours_per_1000r = None
    if step_times:
        hours_per_1000r = (sum(step_times) / len(step_times)
                           * local_steps * 1000 / 3600.0)
    peak_mem = max([r.get('mem_gb', 0.0) for r in records] or [0.0])

    result = {
        'name': os.path.basename(os.path.normpath(run_dir)),
        'dir': run_dir,
        'algorithm': args.get('algorithm', '?'),
        'seed': args.get('seed', '?'),
        'done': os.path.exists(os.path.join(run_dir, 'done')),
        'hours_per_1000r': hours_per_1000r,
        'peak_mem': peak_mem,
        'curve': curve,
        'other_curve': other_curve,
        'other_acc': top_k_mean(other_curve, top_k),
        'rounds_done': records[-1]['step'] / float(local_steps),
        'has_metric': bool(curve),
    }
    if not curve:
        return result

    result['acc'] = top_k_mean(curve, top_k)
    result['best'] = max(a for _, a in curve)
    result['rounds_to'] = OrderedDict(
        (t, next((rnd for rnd, a in curve if a >= t), None))
        for t in thresholds)
    return result


def find_runs(roots):
    """Run directories under `roots`, skipping scratch ones.

    `make smoke` / `make probe` / `make data` write throwaway runs to `_smoke`,
    `_probe` and `_warmup` inside the output tree. A directory named with a
    leading underscore is scratch and never belongs in a results table --
    unless it was named explicitly on the command line.
    """
    runs = []
    for root in roots:
        if os.path.exists(os.path.join(root, 'results.jsonl')):
            runs.append(root)
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if not d.startswith('_')]
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


def fmt(value, spec='{:.2f}'):
    return '-' if value is None else spec.format(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('roots', nargs='+',
        help='Run directories, or a parent directory to scan recursively.')
    parser.add_argument('--metric', choices=list(METRICS), default='local',
        help='Primary accuracy (default: local, as in the paper).')
    parser.add_argument('--threshold', type=float, nargs='+', default=[55.0],
        help='Target accuracies for the "rounds to reach" columns '
             '(paper uses 55 and 60 for CIFAR10).')
    parser.add_argument('--top_k', type=int, default=5,
        help='Average the top-K rounds (paper: 5).')
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

    all_rows = [r for r in (summarize_run(d, args.metric, args.top_k,
                                          args.threshold) for d in runs) if r]
    rows = [r for r in all_rows if r['has_metric']]
    missing = [r['name'] for r in all_rows if not r['has_metric']]
    if not rows:
        print("No run logged the '{}' metric. Runs found: {}. Older runs made "
              "with --eval_test_only only logged 'global'; re-score their "
              "model.pkl with fedbr.scripts.eval_checkpoint, or pass "
              "--metric global.".format(args.metric, ', '.join(missing)),
              file=sys.stderr)
        return 1

    other = 'global' if args.metric == 'local' else 'local'
    base = next((r for r in rows if r['name'] == args.baseline), None)

    header = ['Run', 'Algorithm', 'Acc (%)', 'Best (%)',
              '{} (%)'.format(other.capitalize()), 'Rounds run']
    header += ['Rounds for {:g}%'.format(t) for t in args.threshold]
    header += ['h/1000rd', 'VRAM (GB)', 'Finished']

    table = []
    for r in rows:
        row = [r['name'], r['algorithm'], fmt(r['acc']), fmt(r['best']),
               fmt(r['other_acc']), fmt(r['rounds_done'], '{:.0f}')]
        for t in args.threshold:
            base_rounds = base['rounds_to'][t] if base else None
            row.append(fmt_rounds(r['rounds_to'][t], base_rounds))
        row.append(fmt(r['hours_per_1000r'], '{:.1f}'))
        row.append(fmt(r['peak_mem'], '{:.1f}'))
        row.append('yes' if r['done'] else 'NO (partial)')
        table.append(row)

    widths = [max(len(h), *(len(row[i]) for row in table))
              for i, h in enumerate(header)]
    sep = '| ' + ' | '.join('-' * w for w in widths) + ' |'
    print('| ' + ' | '.join(h.ljust(w) for h, w in zip(header, widths)) + ' |')
    print(sep)
    for row in table:
        print('| ' + ' | '.join(c.ljust(w) for c, w in zip(row, widths)) + ' |')

    print('\nAcc (%) = mean of the top-{} rounds on the {}.'.format(
        args.top_k, METRICS[args.metric]))
    print('{} (%) = the same on the {}.'.format(other.capitalize(),
                                                 METRICS[other]))
    total = sum(r['hours_per_1000r'] for r in rows
                if r['hours_per_1000r'] is not None)
    if total:
        print('h/1000rd = projected training hours for a full 1000-round run '
              'on this GPU (evaluation not included).')
        print('These {} runs project to {:.0f} GPU-hours total, {:.0f} h per '
              'card if split over two GPUs.'.format(len(rows), total, total / 2))
    if missing:
        print("Not shown (no '{}' columns logged): {}".format(
            args.metric, ', '.join(missing)))
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