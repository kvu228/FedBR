"""Plot convergence curves (paper Figure 5(a) / Figure 9(b) for CIFAR10).

Accuracy per communication round on the held-out client test environments, one
line per run directory.

Usage:
    python -m fedbr.scripts.plot_curves output/cifar10 -o figures/cifar10.png
"""

import argparse
import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from fedbr.scripts.summarize import find_runs, summarize_run


def main():
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('roots', nargs='+',
        help='Run directories, or a parent directory to scan recursively.')
    parser.add_argument('-o', '--output', default='figures/convergence.png')
    parser.add_argument('--metric', choices=['local', 'global'], default='local',
        help="local = each training client's held-out split (the paper's "
             "metric); global = the fixed-angle test environments.")
    parser.add_argument('--title', default='CIFAR10 convergence')
    parser.add_argument('--max_rounds', type=float, default=None)
    parser.add_argument('--smooth', type=int, default=1,
        help='Moving-average window in rounds (1 = raw curve).')
    args = parser.parse_args()

    runs = find_runs(args.roots)
    rows = [r for r in (summarize_run(d, args.metric, 5, []) for d in runs)
            if r and r['has_metric']]
    if not rows:
        print('No usable results.jsonl found.', file=sys.stderr)
        return 1

    fig, ax = plt.subplots(figsize=(6, 4.2), dpi=150)
    for row in sorted(rows, key=lambda r: r['name']):
        xs = [x for x, _ in row['curve']]
        ys = [y for _, y in row['curve']]
        if args.max_rounds is not None:
            keep = [i for i, x in enumerate(xs) if x <= args.max_rounds]
            xs = [xs[i] for i in keep]
            ys = [ys[i] for i in keep]
        if args.smooth > 1:
            w = args.smooth
            ys = [sum(ys[max(0, i - w + 1):i + 1])
                  / len(ys[max(0, i - w + 1):i + 1]) for i in range(len(ys))]
        ax.plot(xs, ys, label=row['name'], linewidth=1.2)

    ax.set_xlabel('Communication rounds')
    ax.set_ylabel('Accuracy (%)')
    ax.set_title(args.title)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc='lower right')
    fig.tight_layout()

    out_dir = os.path.dirname(os.path.abspath(args.output))
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    fig.savefig(args.output)
    print('Wrote {}'.format(args.output))
    return 0


if __name__ == '__main__':
    sys.exit(main())
