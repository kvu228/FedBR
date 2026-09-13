# Running FedBR

Packaged with [uv](https://docs.astral.sh/uv/). Tested on vast.ai instances.

## Quick start

```bash
git clone <this-repo> FedBR && cd FedBR
./setup.sh
./run.sh smoke        # ~5 minute end-to-end check
./run.sh FedBR cifar10
```

`setup.sh` installs uv if missing, points the uv cache at `/workspace` when it
exists, picks a PyTorch build that matches the installed NVIDIA driver, runs
`uv sync`, and verifies that CUDA and the `fedbr` import chain both work.

Long runs should live in tmux, since an SSH drop kills the process:

```bash
tmux new -s fedbr
./run.sh FedBR cifar10
# Ctrl-B then D to detach, `tmux attach -t fedbr` to come back
```

## run.sh

```bash
./run.sh smoke                    # quick check
./run.sh FedBR cifar10            # the paper's main experiment
./run.sh ERM cifar100
./run.sh Moon mnist
./run.sh gen-virtual              # virtual data; required before VHL
./run.sh VHL cifar10
./run.sh results /workspace/output/cifar10/FedBR
```

Presets are `cifar10`, `cifar100` and `mnist`; the default is `cifar10`.
Anything after the preset goes straight to `train_fed.py`:

```bash
./run.sh FedBR cifar10 --steps 20000 --hparams '{"batch_size": 16}'
```

Environment overrides: `FEDBR_DEVICE` (0), `FEDBR_SEED` (12345),
`FEDBR_TRAIN_ENVS`, `FEDBR_STEPS`, `FEDBR_LOCAL_STEPS` (50), `FEDBR_OUT`,
`FEDBR_NUM_WORKERS` (2).

Algorithms are listed in `ALGORITHMS` at the top of `fedbr/algorithms.py`. The
federated ones are `FedBR`, `ERM`, `FedProx_algo`, `Moon`, `VHL`, `FedNTD`,
`FedDeCorr`, `FedMix`, `NaiveMix`, `SCAFFOLD_algo` and `FedCM_algo`.

To sweep the baselines:

```bash
for a in ERM FedProx_algo Moon FedNTD FedDeCorr FedMix NaiveMix; do
    ./run.sh "$a" cifar10
done
```

## Choosing a PyTorch build

PyPI's default Linux wheels bundle the CUDA 13 runtime, which needs driver 580
or newer — older vast.ai images need a CUDA 12 build instead. `setup.sh` hands
that decision to `uv pip install --torch-backend=auto`, which reads the driver
and picks. Override it when the guess is wrong:

```bash
FEDBR_CUDA=cu126 ./setup.sh
FEDBR_CUDA=cpu ./setup.sh
```

You do not need a CUDA toolkit on the host — the wheels carry their own
runtime, only the driver has to be new enough.

Because the CUDA variant is host-specific, `torch` and `torchvision` are kept
out of `pyproject.toml` and installed on top of the synced environment. `uv run`
leaves them alone, but a bare `uv sync` removes them; `run.sh` detects that and
tells you to re-run `./setup.sh`.

## Data

CIFAR-10, CIFAR-100 and MNIST download themselves on first use. Nothing else is
needed for the experiments in the paper.

`fedbr/scripts/download.py`, which fetches the DomainBed image datasets (PACS,
VLCS, OfficeHome, TerraIncognita, DomainNet, SVIRO), **does not work as
shipped**: the `gdown.download` call in `download_and_extract` is commented out,
every dataset but PACS is commented out of `__main__`, and the `fedbr/misc/`
directory that `download_domain_net` and `download_vlcs` read file lists from is
absent. Those datasets are not part of the FedBR results.

The `WILDSCamelyon` and `WILDSFMoW` datasets need an extra, since `wilds` pulls
in ogb, pandas and scikit-learn that nothing else here uses:

```bash
uv sync --extra wilds
```

## Reading results

Each run writes `results.jsonl`, `out.txt`, `err.txt`, `model.pkl` and a `done`
marker to its output directory. The accuracies that matter are the test
environments — with `--train_envs 10` on CIFAR those are `env10_in_acc` through
`env19_in_acc`.

```bash
./run.sh results /workspace/output/cifar10/FedBR
```

`fedbr/scripts/collect_results.py` also works, but it inherits DomainBed's
model-selection logic and reports every test environment separately, which is
awkward for federated runs. Its `--input_dir` must be the *parent* of the run
directories.

## Things that are hardcoded

This is research code; a fair amount is not reachable from the command line.

| What | Where |
| --- | --- |
| Backbone is always CCT-7 for 32x32 inputs | `networks.py:245` |
| FedBR's `mu`, `lam`, `tau1`, `tau2` | `algorithms.py:1078` |
| Clients sampled per round: `min(10, train_envs)` | `train_fed.py:361` |
| Non-IID split fixed at Dirichlet(0.1) | `datasets.py:311` |
| `RotatedMNIST` / `ColoredMNIST` ignore `--train_envs` and always use 10 clients | `datasets.py:519` |

Two more worth knowing:

- `--steps` counts *local* steps, so rounds = `steps / local_steps`.
- `--device` is a GPU index, not a torch device string.

`fedbr/scripts/sweep.py` launches `fedbr.scripts.train`, the non-federated
entry point, so it is not useful for federated sweeps.

## Startup behaviour

`datasets.py` decodes every image to a float32 tensor and rotates them one at a
time with PIL, holding the result in memory. Expect several minutes and 2-3GB
of RAM before step 0 on RotatedCIFAR10, plus some raw arrays printed to stdout.
That is normal.