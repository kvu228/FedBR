#!/usr/bin/env bash
# One-shot bootstrap for a fresh vast.ai (or any Linux+CUDA) instance.
#
#   bash setup_vastai.sh
#
# Installs uv if missing, syncs the environment from pyproject.toml, downloads
# CIFAR10 and builds the non-iid split cache. Then: `make smoke`, `make table1`.
set -euo pipefail

cd "$(dirname "$0")"

echo "=== 1/4 uv ==="
if ! command -v uv >/dev/null 2>&1; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi
uv --version

echo
echo "=== 2/4 system packages ==="
# make is not in every vast.ai image; git is needed by nothing here but is
# almost always wanted. Skip silently when we are not root or apt is absent.
if ! command -v make >/dev/null 2>&1; then
    if command -v apt-get >/dev/null 2>&1 && [ "$(id -u)" = "0" ]; then
        apt-get update -qq && apt-get install -y -qq make
    else
        echo "WARNING: 'make' is missing and cannot be installed automatically."
        echo "         Install it, or run the python commands from the Makefile by hand."
    fi
fi

echo
echo "=== 3/4 python environment ==="
uv sync
uv run python - <<'PY'
import torch, torchvision
print("torch       ", torch.__version__)
print("torchvision ", torchvision.__version__)
print("cuda build  ", torch.version.cuda)
print("cuda avail  ", torch.cuda.is_available())
if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        print("  gpu %d: %s" % (i, torch.cuda.get_device_name(i)))
else:
    print("  no GPU visible - training will fall back to CPU and be unusably slow")
PY

echo
echo "=== 4/4 data + split cache ==="
if command -v make >/dev/null 2>&1; then
    make data
else
    # Google Drive mirror by default, official host as the fallback.
    uv run python -m fedbr.scripts.download_data --data_dir ./fedbr/data/CIFAR10
    echo "Split cache not pre-built (no make); the first run will build it."
fi

echo
echo "Done. Next:"
echo "  make smoke     # ~2 min end-to-end check"
echo "  make help      # all reproduction targets"
echo "  make table1    # the main CIFAR10 result (see REPRODUCE.md section 5 for cost)"
