#!/usr/bin/env bash
# Launch FedBR experiments with the flags the repository actually expects.
#
#   ./run.sh smoke                     quick end-to-end check (~5 min)
#   ./run.sh FedBR cifar10             the paper's main experiment
#   ./run.sh ERM cifar100
#   ./run.sh Moon mnist
#   ./run.sh gen-virtual               virtual data, required before VHL
#   ./run.sh results <output_dir>      summarise a finished run
#
# Anything after the preset is passed straight through to train_fed.py:
#
#   ./run.sh FedBR cifar10 --steps 20000 --hparams '{"batch_size": 16}'
#
# Overridable via the environment:
#   FEDBR_DEVICE (0)  FEDBR_SEED (12345)  FEDBR_TRAIN_ENVS  FEDBR_STEPS
#   FEDBR_LOCAL_STEPS (50)  FEDBR_OUT  FEDBR_NUM_WORKERS (2)
set -euo pipefail

cd "$(dirname "$0")"

DEVICE="${FEDBR_DEVICE:-0}"
SEED="${FEDBR_SEED:-12345}"
# One DataLoader per environment means workers multiply fast; vast.ai boxes are
# usually CPU-limited, so stay low unless told otherwise.
export FEDBR_NUM_WORKERS="${FEDBR_NUM_WORKERS:-2}"

if [ -d /workspace ]; then OUT_ROOT="${FEDBR_OUT:-/workspace/output}"; else OUT_ROOT="${FEDBR_OUT:-./output}"; fi

die() { printf '\033[31merror: %s\033[0m\n' "$1" >&2; exit 1; }

# torch lives outside the lockfile (see pyproject.toml), so a bare `uv sync`
# can remove it. Fail with something readable instead of a stray traceback.
uv run python -c "import torch" 2>/dev/null \
    || die "PyTorch is missing from the environment. Run ./setup.sh"

# --- subcommands ---------------------------------------------------------

if [ "${1:-}" = gen-virtual ]; then
    # VHL trains against images from a randomly initialised StyleGAN2; no
    # pretrained checkpoint is involved. generate.sh is not used because it
    # hardcodes a conda interpreter path.
    shift
    uv run python ./fedbr/generative/generate.py \
        --gpu_index "$DEVICE" \
        --root_path ./fedbr/data/generative \
        --model style_GAN_v2_G \
        --generate_dataset style_GAN_init_32_c10_200 \
        --batch_size 10 --sample 20 --noise_num 10 --image_resolution 32 \
        --style_gan_style_dim 64 --style_gan_n_mlp 1 --style_gan_cmul 1 "$@"
    echo "Virtual data written to ./fedbr/data/generative/style_GAN_init_32_c10_200"
    exit 0
fi

if [ "${1:-}" = results ]; then
    [ -n "${2:-}" ] || die "usage: ./run.sh results <output_dir>"
    uv run python - "$2" <<'EOF'
import json
import sys

import numpy as np

path = f"{sys.argv[1].rstrip('/')}/results.jsonl"
records = [json.loads(line) for line in open(path)]
if not records:
    sys.exit("no records yet")

args = records[0]["args"]
print(f"{args['algorithm']} on {args['dataset']}  "
      f"({args['train_envs']} clients, local_steps={args['local_steps']})")
print(f"{'step':>8}  {'round':>6}  {'loss':>8}  {'test acc':>9}")
for r in records:
    accs = [r[f"env{i:02d}_in_acc"] for i in args["test_envs"]]
    print(f"{r['step']:>8}  {r['step'] // args['local_steps']:>6}  "
          f"{r['loss']:>8.4f}  {np.mean(accs):>9.4f}")

best = max(np.mean([r[f"env{i:02d}_in_acc"] for i in args["test_envs"]]) for r in records)
print(f"\nbest test acc: {best:.4f}")
EOF
    exit 0
fi

# --- presets -------------------------------------------------------------

ALGO="${1:-}"
[ -n "$ALGO" ] || die "usage: ./run.sh <algorithm> [cifar10|cifar100|mnist]  (or: smoke, gen-virtual, results)"

shift
if [ "$ALGO" = smoke ]; then
    PRESET=smoke
    ALGO=ERM
else
    # A second positional argument is the preset; a flag means the caller took
    # the default preset and went straight to train_fed.py options.
    PRESET=cifar10
    if [ $# -ge 1 ]; then
        case "$1" in
            -*) ;;
            *) PRESET="$1"; shift ;;
        esac
    fi
fi

LOCAL_STEPS=50
case "$PRESET" in
    smoke)
        DATA=./fedbr/data/CIFAR10/; DATASET=RotatedCIFAR10; ENVS=10
        STEPS=50; LOCAL_STEPS=10; EXTRA=(--checkpoint_freq 10 --skip_model_save)
        ;;
    cifar10)
        DATA=./fedbr/data/CIFAR10/; DATASET=RotatedCIFAR10; ENVS=10
        STEPS=50000; EXTRA=(--save_model_every_checkpoint)
        ;;
    cifar100)
        DATA=./fedbr/data/CIFAR100/; DATASET=RotatedCIFAR100; ENVS=10
        STEPS=50000; EXTRA=(--save_model_every_checkpoint)
        ;;
    mnist)
        DATA=./fedbr/data/MNIST/; DATASET=RotatedMNIST; ENVS=10
        STEPS=50000; EXTRA=(--save_model_every_checkpoint)
        ;;
    *)
        die "unknown preset '$PRESET' (expected cifar10, cifar100 or mnist)"
        ;;
esac

STEPS="${FEDBR_STEPS:-$STEPS}"
ENVS="${FEDBR_TRAIN_ENVS:-$ENVS}"
LOCAL_STEPS="${FEDBR_LOCAL_STEPS:-$LOCAL_STEPS}"

# RotatedMNIST and ColoredMNIST hardcode their environment list and ignore
# --train_envs; anything but 10 makes train_fed.py treat test environments as
# training clients.
if [ "$DATASET" = RotatedMNIST ] && [ "$ENVS" != 10 ]; then
    die "$DATASET only supports --train_envs 10 (the environment list is hardcoded in datasets.py)"
fi

# FedBR generates its pseudo-data by Mixture, per the paper's default.
[ "$ALGO" = FedBR ] && EXTRA+=(--use_Mixture)

# The --virtual_set default in train_fed.py is a 28x28 set, which does not
# match what gen-virtual produces for CIFAR.
if [ "$ALGO" = VHL ]; then
    VSET=style_GAN_init_32_c10_200
    [ -d "./fedbr/data/generative/$VSET" ] || die "VHL needs virtual data first: ./run.sh gen-virtual"
    EXTRA+=(--virtual_set "$VSET")
fi

OUT="$OUT_ROOT/$PRESET/$ALGO"
mkdir -p "$OUT"

echo "algorithm  $ALGO"
echo "dataset    $DATASET ($ENVS clients, $((STEPS / LOCAL_STEPS)) rounds)"
echo "output     $OUT"
echo "workers    $FEDBR_NUM_WORKERS per environment"
echo

# The first few minutes are spent decoding and rotating every image in memory
# before step 0 runs. That is normal, not a hang.
exec uv run python -m fedbr.scripts.train_fed \
    --data_dir "$DATA" \
    --dataset "$DATASET" \
    --algorithm "$ALGO" \
    --train_envs "$ENVS" \
    --steps "$STEPS" \
    --local_steps "$LOCAL_STEPS" \
    --output_dir "$OUT" \
    --device "$DEVICE" \
    --seed "$SEED" \
    "${EXTRA[@]}" "$@"