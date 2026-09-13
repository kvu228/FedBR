#!/usr/bin/env bash
# Bootstrap the FedBR environment on a fresh machine (tested on vast.ai).
#
#   ./setup.sh                     # match the PyTorch build to the host driver
#   FEDBR_CUDA=cu126 ./setup.sh    # force a specific CUDA build
#   FEDBR_CUDA=cpu ./setup.sh      # CPU-only
set -euo pipefail

cd "$(dirname "$0")"

say() { printf '\n\033[1m==> %s\033[0m\n' "$1"; }
warn() { printf '\033[33m    %s\033[0m\n' "$1"; }

# --- uv -----------------------------------------------------------------
if ! command -v uv >/dev/null 2>&1; then
    say "Installing uv"
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi
say "uv $(uv --version | awk '{print $2}')"

# --- cache and link mode ------------------------------------------------
# vast.ai mounts /workspace on a separate, much larger volume than the root
# filesystem. Keeping the cache there avoids filling / with ~4GB of wheels,
# and copy mode avoids the cross-device hardlink warning.
if [ -d /workspace ] && [ -z "${UV_CACHE_DIR:-}" ]; then
    export UV_CACHE_DIR=/workspace/.uv-cache
    export UV_LINK_MODE=copy
    for f in "$HOME/.bashrc" "$HOME/.profile"; do
        [ -f "$f" ] || continue
        grep -q UV_CACHE_DIR "$f" || {
            printf 'export UV_CACHE_DIR=/workspace/.uv-cache\nexport UV_LINK_MODE=copy\n' >>"$f"
        }
    done
    say "Cache at $UV_CACHE_DIR"
fi

# --- install -------------------------------------------------------------
say "Syncing dependencies"
uv sync

# PyPI's default Linux wheels bundle the CUDA 13 runtime, which needs driver
# 580 or newer, so the right build depends on the host. `--torch-backend=auto`
# reads the driver and picks for us. Installing outside the lockfile keeps one
# CUDA variant from being baked into pyproject.toml; `uv run` does not remove
# these, though a bare `uv sync` would.
say "Installing PyTorch (backend: ${FEDBR_CUDA:-auto}; ~3-4GB the first time)"
GPU_INFO="$(nvidia-smi --query-gpu=driver_version,name --format=csv,noheader 2>/dev/null || true)"
if [ -n "$GPU_INFO" ]; then
    echo "$GPU_INFO" | sed 's/^/    driver /'
else
    warn "No NVIDIA driver detected; expect a CPU-only build."
fi
uv pip install --torch-backend="${FEDBR_CUDA:-auto}" torch torchvision

# --- data directories ----------------------------------------------------
mkdir -p fedbr/data/CIFAR10 fedbr/data/CIFAR100 fedbr/data/MNIST fedbr/data/generative

# --- verify --------------------------------------------------------------
say "Verifying"
uv run python - <<'EOF'
import sys

import torch

print(f"    python      {sys.version.split()[0]}")
print(f"    torch       {torch.__version__}  (cuda {torch.version.cuda})")
if torch.cuda.is_available():
    print(f"    gpu         {torch.cuda.get_device_name(0)}")
else:
    print("    gpu         NOT AVAILABLE")

import fedbr.scripts.train_fed  # noqa: F401  the import chain that used to break

print("    fedbr       imports cleanly")
EOF

cat <<EOF

Ready. Next:

    ./run.sh smoke              # ~5 minute end-to-end check
    ./run.sh FedBR cifar10      # the paper's main experiment

EOF