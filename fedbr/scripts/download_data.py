"""Fetch CIFAR10 / CIFAR100 into the data directory.

Downloads from a Google Drive mirror by default, because the official
www.cs.toronto.edu host is slow or throttled from many networks. Whatever the
mirror returns is checked with torchvision's own integrity check; if it is
missing, incomplete or corrupt, the official host is used instead.

Usage:
    python -m fedbr.scripts.download_data --data_dir ./fedbr/data/CIFAR10
    python -m fedbr.scripts.download_data --no_drive      # official host only
"""

import argparse
import os
import shutil
import sys
import tempfile

from torchvision.datasets import CIFAR10, CIFAR100

# Public Drive folders, each holding the extracted dataset directory.
DEFAULT_DRIVE = {
    'CIFAR10': 'https://drive.google.com/drive/folders/1Lt0yWh5s2MGFWUZFGZM_5NWM85N7iyd1',
    'CIFAR100': 'https://drive.google.com/drive/folders/1FZ4eKRYLpKyn0R-KcoXoKderJpfJJh5G',
}

SPEC = {
    'CIFAR10': (CIFAR10, 'cifar-10-batches-py'),
    'CIFAR100': (CIFAR100, 'cifar-100-python'),
}


def is_valid(name, data_dir):
    """True when torchvision can open both splits without downloading."""
    cls = SPEC[name][0]
    try:
        cls(data_dir, train=True, download=False)
        cls(data_dir, train=False, download=False)
        return True
    except Exception:
        return False


def from_drive(name, data_dir, url):
    """Try the mirror. Returns True only if the result passes the checksum."""
    import gdown

    cls, dirname = SPEC[name]
    # A run killed mid-download leaves its scratch dir behind; sweep those.
    for stale in os.listdir(data_dir):
        if stale.startswith('.drive-'):
            shutil.rmtree(os.path.join(data_dir, stale), ignore_errors=True)

    tmp = tempfile.mkdtemp(prefix='.drive-', dir=data_dir)
    dest = os.path.join(data_dir, dirname)
    try:
        gdown.download_folder(url=url, output=tmp, quiet=False,
                              use_cookies=False)
        src = os.path.join(tmp, dirname)
        if not os.path.isdir(src):
            print('  mirror has no {}/'.format(dirname), file=sys.stderr)
            return False
        shutil.rmtree(dest, ignore_errors=True)
        shutil.move(src, dest)
    except Exception as exc:
        print('  mirror failed: {}: {}'.format(type(exc).__name__, exc),
              file=sys.stderr)
        return False
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if not is_valid(name, data_dir):
        print('  mirror content failed the checksum, discarding', file=sys.stderr)
        shutil.rmtree(dest, ignore_errors=True)
        return False
    return True


def fetch(name, data_dir, url, use_drive):
    cls = SPEC[name][0]
    print('== {} -> {}'.format(name, data_dir))
    if is_valid(name, data_dir):
        print('  already present, skipping')
        return True

    if use_drive and url:
        print('  trying the Google Drive mirror')
        if from_drive(name, data_dir, url):
            print('  OK (mirror)')
            return True
        print('  falling back to the official host')

    cls(data_dir, train=True, download=True)
    cls(data_dir, train=False, download=True)
    ok = is_valid(name, data_dir)
    print('  {}'.format('OK (official host)' if ok else 'FAILED'))
    return ok


def main():
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--data_dir', default='./fedbr/data/CIFAR10')
    parser.add_argument('--datasets', nargs='+', default=['CIFAR10', 'CIFAR100'],
        choices=sorted(SPEC), help='CIFAR100 is only needed by FedBR '
        '--use_Mixture.')
    parser.add_argument('--no_drive', action='store_true',
        help='Skip the mirror and use the official host directly.')
    parser.add_argument('--drive_cifar10', default=DEFAULT_DRIVE['CIFAR10'])
    parser.add_argument('--drive_cifar100', default=DEFAULT_DRIVE['CIFAR100'])
    args = parser.parse_args()

    os.makedirs(args.data_dir, exist_ok=True)
    urls = {'CIFAR10': args.drive_cifar10, 'CIFAR100': args.drive_cifar100}
    ok = True
    for name in args.datasets:
        ok &= fetch(name, args.data_dir, urls[name], not args.no_drive)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())