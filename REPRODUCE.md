# Reproducing the CIFAR10 results of FedBR

This document covers the CIFAR10 half of Guo et al., *FedBR: Improving Federated
Learning on Heterogeneous Data via Local Learning Bias Reduction* (ICML 2023).
RotatedMNIST, CIFAR100 and PACS are out of scope here, though nothing below
prevents you from running them.

---

## 1. Runbook — the commands, in order

Rent an instance with CUDA 12.4+ drivers (`pytorch/pytorch` or `nvidia/cuda`
both work — nothing from the image is used except the driver). See §5 for how
to size it; the short version is that 2× RTX 3060 is fine and vCPU/RAM matter
more than the GPU tier.

### Step 1 — set up  (~10 min, once)

```bash
git clone <this repo> && cd FedBR
bash setup_vastai.sh
```

That installs `uv` and `make` if missing, runs `uv sync`, prints the GPU torch
can see, downloads CIFAR10/CIFAR100 and pre-builds the non-iid split cache.
If `uv` and `make` are already there, `make setup && make data` is the same
thing.

**Check the line it prints:** `cuda available: True` and your GPU name. If it
says `cpu only`, the driver or the container is wrong — stop here, training on
CPU is unusably slow.

The datasets come from a **Google Drive mirror by default**, because the
official `www.cs.toronto.edu` host is slow or throttled from many networks.
What the mirror returns is verified against torchvision's checksum; anything
that fails is discarded and re-fetched from the official host, so the mirror is
a speed-up and never a dependency. `make data NO_DRIVE=1` skips it; the mirror
URLs are `--drive_cifar10` / `--drive_cifar100` on
`python -m fedbr.scripts.download_data`.

### Step 2 — verify the install  (~2 min)

```bash
make smoke
```

Runs FedBR end-to-end for 4 rounds and prints a summary table. Do not skip it:
if anything is broken you find out in two minutes rather than six hours.

### Step 3 — measure what a full run costs *on this card*  (~10 min)

```bash
make probe
```

Prints `h/1000rd` (projected hours for one complete 1000-round run on the card
you just rented) and `VRAM (GB)`. **This is the decision point** — multiply
against the instance's hourly rate before committing. If it is too expensive,
destroy the instance now, having spent minutes.

### Step 4 — run the experiments

Always inside `tmux`; these run for many hours and an SSH drop would kill them.

**One GPU:**

```bash
tmux new -s fedbr
make table1
```

**Two GPUs** — one run occupies exactly one GPU (there is no DDP), so use two
shells, one per card. The dataset cache was already built in Step 1, so they
will not fight over it:

```bash
tmux new -s g0    # then inside:  make table1-gpu0     (FedBR-family runs)
tmux new -s g1    # then inside:  make table1-gpu1     (the rest)
```

Detach with `Ctrl-b d`, re-attach with `tmux attach -t g0`.
Do **not** use `make -j2 table1`: every job would inherit `DEVICE=0` and pile
onto one card.

### Step 5 — collect the results

`make table1` runs these itself when it finishes, so this step is only needed
if you ran individual targets, split across two GPUs, or want to look at
partial progress while training:

```bash
make summarize     # table + output/cifar10/summary.csv
make figures       # figures/cifar10_convergence.png
```

Both work on runs that are still in progress — `results.jsonl` is written every
`EVAL_EVERY` rounds, and unfinished runs are flagged `NO (partial)`.

### Step 6 — if something dies

Just re-run the same target. Each experiment writes a `done` marker and
finished ones are skipped, so `make table1` resumes at the run that failed
instead of retraining the earlier ones (which would also append duplicate rows
to their append-only `results.jsonl`). A run that died *part-way* has no
marker, so it is deleted and restarted cleanly. `FORCE=1` redoes a finished
experiment.

### Other tables

Same pattern, after Step 1:

```bash
make table5-100clients      # Table 5
make table8-errorbar        # Table 8 (3 seeds - 3x the cost)
make table9-resnet          # Table 9
make table11-tau            # Table 11
make table3-baselines       # Table 3, "w/o FedBR" column only
make setup-vhl && make vhl-data && make table2-vhl   # Table 2
```

`make help` lists everything with its knobs.

---

Everything runs through `uv`, so there is no `conda`, no `pip install -r`, and
no system Python to fight with. `uv sync` resolves from `pyproject.toml` and
uses the committed `uv.lock`, so every instance gets the same environment.

### Why the dependency versions changed

`requirements.txt` pins `torch==1.7.1` / `numpy==1.20.3` / `torchvision==0.8.2`.
Those have no wheels for Ampere or newer GPUs (anything you would actually rent)
and no wheels for Python ≥ 3.9. `pyproject.toml` therefore pins
`torch==2.6.0` + `torchvision==0.21.0`, pulled from the PyTorch cu124 index on
Linux and from PyPI elsewhere. The source changes this required are listed in
§6 — they are mechanical, not behavioural.

`wilds` and the StyleGAN stack are **optional extras** (`--extra wilds`,
`--extra vhl`), because CIFAR10 needs neither and `wilds` drags in a large
dependency tree.

---

## 2. The experimental setting

From Appendix A of the paper, for CIFAR10:

| Setting | Value |
| --- | --- |
| Split | LDA over labels, α = 0.1, into `--train_envs` clients |
| Inner-class shift | per client, sample q ~ Dir(1.0) over the 10 angles {0,15,…,135}; rotate each local image by an angle drawn from q |
| Test environments | 10 copies of the CIFAR10 test set, rotated by 0,15,…,135 |
| Clients per round | 10 (all of them when `CLIENTS=10`) |
| Local iterations | 50 |
| Communication rounds | 1000 |
| Optimizer | SGD, lr = 0.01, local batch size 32 |
| Model | VGG11 |
| FedBR | 32 pseudo-data from RSM, transferred once at the start; τ₁ = τ₂ = 2.0, μ = 0.5, λ = 1.0 |

The `Makefile` encodes all of this. `ROUNDS × LOCAL_STEPS` is passed as
`--steps`, so `make table1` runs 50 000 steps per algorithm.

**Reported metric** (paper: "mean of maximum 5 test accuracies over rounds",
"mean accuracy on all local test datasets"): `summarize.py` averages the top-5
rounds of the mean accuracy over each training client's **20% held-out split**
— data with that client's own label skew and rotation mix. Two things pin this
reading down: the paper's Table 6 reports the *same* FedAvg at 46.37 on
"balanced global test datasets" against 58.99 in Table 1, so Table 1 is not a
global-test number; and re-scoring finished checkpoints on both splits puts
FedProx/FedBR within 1–2 points of Table 1 on the client held-out split and
~18 points below it on the fixed-angle test environments.

The fixed-angle test environments (ten copies of the CIFAR10 test set, one
angle each — the Table 6 setting) are logged alongside and shown as the
`Global (%)` column; `--metric global` makes them primary. Expect FedAvg ≈ 40
there, not 59.

The first pass of this reproduction used the fixed-angle environments as the
metric and dropped the client held-out splits from the logs to save evaluation
time; that is why runs made before commit `9550587` cannot be summarized on the
paper's metric. `fedbr.scripts.eval_checkpoint` re-scores their `model.pkl`
(final round only).

---

## 3. What each Make target maps to

| Target | Paper | Notes |
| --- | --- | --- |
| `make table1` | Table 1 (CIFAR10 column), Figure 5(a), Figure 9(b) | FedAvg, FedProx, Moon, DANN, GroupDRO, FedBR, +Mixup, FedMix, FedBR+Mixup |
| `make run-local` | Table 1, "Local" row | degenerate baseline: aggregate only at step 0 |
| `make table2-vhl` | Table 2 | needs `make setup-vhl && make vhl-data` first |
| `make table3-baselines` | Table 3, "w/o FedBR" column only | see §4 |
| `make table5-100clients` | Table 5 | 100 clients, 10 sampled per round |
| `make table8-errorbar` | Table 8 | 3 seeds × 5 algorithms |
| `make table9-resnet` | Table 9 | clean (unrotated) CIFAR10 on a GN ResNet18 |
| `make table11-tau` | Table 11 | FedBR τ₂ ∈ {0, 0.5, 1, 2} at τ₁ = 2 |
| `make summarize` | — | accuracy + rounds-to-threshold table, also written to `summary.csv` |
| `make figures` | Figure 5(a) / 9(b) | convergence curves |

Useful knobs (all overridable on the command line):

```bash
make table1 ROUNDS=200          # shorter runs while you sanity-check
make run-fedbr DEVICE=1         # second GPU
make run-fedbr MOMENTUM=0.9     # see §4 on the momentum question
make run-fedbr EVAL_EVERY=10    # evaluate 5x less often
make table1 EVAL_ENVS=local     # paper's metric only, cheapest evaluation
make table1 EVAL_ENVS=all       # every split of every env, as released
make run-fedbr BACKBONE=cct     # the backbone the released code hardcoded
```

---

## 4. What is *not* reproducible from the released code

Be aware of these before you plan GPU hours. None of them are fixed here,
because fixing them would mean writing algorithms the authors did not release.

1. **Table 3, the "+ FedBR" column.** Combining FedBR with FedCM / FedDecorr /
   FedNTD needs algorithm classes that do not exist in `algorithms.py`.
   `hparams_registry.py` references names like `FedBR_Moon` and `FedBR_AugCA`,
   but no such classes were released. Only the "w/o FedBR" column can be run.
2. **Table 4, the component ablation.** There is no switch to run Component 1
   or Component 2 alone, or to remove the max step — `FedBR.update()` always
   runs the full objective.
3. **Table 6, local-model performance.** Requires evaluating each local model
   before aggregation on a balanced global test set; `train_fed.py` only
   evaluates the aggregated model.
4. **Figure 6 ablations** (with/without the projection layer, K in Mixture,
   balanced vs. unbalanced RSM). Only the pseudo-data *type* is switchable, via
   `--use_Mixture` / `--use_Mixup`.
5. **Table 9's exact model.** The paper uses "ResNet18 with group
   normalization"; the released `networks.py` never wires one up for 32×32
   inputs (`Resnet.py`'s ImageNet ResNet18 ends in an `AvgPool2d(7)` that cannot
   consume a 1×1 feature map). `BACKBONE=resnet18_gn` here is a standard
   CIFAR-style reconstruction: torchvision ResNet18, `GroupNorm(2, ·)`, 3×3
   stride-1 stem, no max-pool. Treat its numbers as indicative, not as a
   replication.
6. **Table 2 (VHL)** depends on StyleGAN-v2 virtual data. `generate.py` runs,
   but it needs `fire`/`einops`/`kornia`/`vector-quantize-pytorch`/`aim`
   (`make setup-vhl`) and a CUDA GPU, and the generator is untrained, so the
   data differs from the authors' run-to-run.

Also worth knowing, for anyone comparing numbers closely:

* **The projection MLP is bigger than the paper says.** Appendix A specifies
  width 256 and output dimension 128. `FedBR.__init__` overrides the hparam to
  `2 × featurizer.n_outputs_feature` and sets the output dimension to
  `n_outputs_feature` — with VGG11 that is width 1024, output 512. The released
  code is what runs here. It does not appear to matter: with it, FedBR scores
  65.9 on the client held-out split against the paper's 64.65.
* **Momentum — this one changes the numbers.** Appendix A says momentum 0.9
  "when using CCT and ResNet", i.e. plain SGD for the VGG11 CIFAR10 runs, but
  the released `ERM` (and `Moon`) hardcode `momentum=0.9`. Run that way,
  FedAvg reaches 99.9% accuracy on its *training* data and 72.9 on the client
  held-out split — 14 points above Table 1's 58.99 — while FedProx and FedBR,
  whose optimizers carry no momentum, land within 2 points of the paper. The
  default is now `MOMENTUM=0.0` for CIFAR10, which is what the paper describes;
  `Moon` reads the same hparam. Set `MOMENTUM=0.9` if you switch to a CCT or
  ResNet backbone.
* **Baseline hyperparameters were tuned over grids** (Appendix A: FedProx μ ∈
  {0.001, 0.01, 0.1}, DANN weight ∈ {0.01, 0.1, 1}, Moon ∈ {0.01, 0.1, 1, 10},
  FedMix λ ∈ {0.01, 0.1, 0.2}, FedNTD β ∈ {1.0, 0.1}). The paper does not say
  which value won for CIFAR10. The Makefile picks one from each grid; sweep them
  yourself if you need the tuned numbers:
  `make run-fedprox HP=', "fedprox_mu": 0.1' OUT=./output/sweep/fedprox-0.1`.

---

## 5. Choosing an instance

**Do not pick on VRAM or on tensor-core FLOPS — neither is the constraint.**

*Measured on this code:* FedAvg/ERM is 9.2 M parameters (exactly the figure in
the paper's Table 7, which is a useful confirmation that the VGG11 backbone is
the right one). The FedBR module holds 20.6 M, because it keeps frozen copies
of the featurizer and classifier as submodules. With ten client models, their
`FedAvg` wrapper's deepcopy, and an accumulated gradient state-dict each, peak
allocation lands in the low single-digit GB. Every run logs its own
`torch.cuda.max_memory_allocated` to `results.jsonl`, and `make summarize`
prints it as the `VRAM (GB)` column, so do not take this estimate on trust —
check it after `make probe`.

The batch is 32 images at 32×32, which is a *small* kernel, and
`Algorithm_Fed.update()` deep-copies the whole model and walks its full
state-dict **once per client per step** — 500 000 times over a 1000-round run.
That makes the workload largely bound by memory traffic, kernel-launch latency
and plain Python, not by arithmetic throughput. So a card with 4× the FLOPS
will not give 4× the speed, and CPU single-thread performance matters more than
usual.

What to actually check when renting:

| | |
| --- | --- |
| GPU count | 2 is worth it (§6), more is not — nine runs, and the tail is one long FedBR run |
| VRAM | a 12 GB card is generous; verify with the `VRAM (GB)` column rather than guessing |
| vCPU | **≥ 4 per concurrent run** (so ≥ 8 on a 2-GPU box). This is the spec most likely to bottleneck you |
| RAM | each process holds the whole ~1.8 GB dataset, with a transient spike while loading it; ≥ 16 GB for two runs, 32 GB comfortable |
| Disk | ~5 GB for `table1` (data + one 1.8 GB cache + checkpoints); ~30 GB if you also run `table8-errorbar`. vast.ai's default allocation is often smaller than you expect |

**So: yes, 2× RTX 3060 is a sensible choice**, and the 12 GB variant has far
more VRAM than this needs. A faster card shortens calendar time and therefore
your exposure to a preempted instance, but on an overhead-bound workload like
this one it is unlikely to pay for itself per unit of work. Rather than trust
that reasoning, measure it:

```bash
make data          # once
make probe         # ~10 min: 3 rounds of FedAvg and of FedBR, 10 clients
```

`probe` prints `h/1000rd` — the projected hours for one full run **on the card
you just rented** — and the peak VRAM. Multiply out against the instance's
hourly price before starting `table1`. If the projection is unacceptable, stop
the instance having spent minutes rather than a day.

## 6. Cost

Table 7 of the paper reports mean computation time **per step** on CIFAR10 with
VGG11: 0.29 s for FedAvg, 0.60 s for FedBR (each step updates all 10 clients).
A full 1000-round run is 50 000 steps, so roughly:

| | per run |
| --- | --- |
| FedAvg-like (ERM, Mixup, FedProx, GroupDRO) | ~4 h training |
| FedBR, Moon, VHL | ~8 h training |
| evaluation, `EVAL_ENVS=local+global`, `EVAL_EVERY=2` | ~5 h on top (measured throughput; `EVAL_EVERY=5` → ~2 h) |
| evaluation, `EVAL_ENVS=local` | ~10× cheaper — the paper's metric is only 10k images |
| evaluation, `EVAL_ENVS=all` | ~1.7× `local+global` |

`make table1` is nine such runs — on the order of two GPU-days on one card.
Options if that is too much:

* **Use both cards of a two-GPU instance.** `train_fed.py` has no
  DataParallel/DDP, so one run occupies exactly one GPU and a second card is
  only useful for a second experiment — which means one 2-GPU instance does the
  work of two 1-GPU instances, at a shared dataset cache and one set of setup
  costs. Run `make data` **first** so the split is built once, then two shells:

  ```bash
  tmux new -s g0; make table1-gpu0     # FedBR-family runs
  tmux new -s g1; make table1-gpu1     # the rest
  ```

  The two lists are balanced by the per-step costs in Table 7 (FedBR is ~2× the
  cost of FedAvg), so both finish in roughly 24 h rather than 49 h serial.
  Override `GPU0_RUNS` / `GPU1_RUNS` to re-split. Do **not** start both shells
  before `make data`: they would each spend ~13 minutes building the same split.
  Do **not** use `make -j2 table1` either — every job would inherit `DEVICE=0`
  and pile onto one card.
* Run targets individually on separate instances (`make run-fedavg`,
  `make run-fedbr`, …) — they share nothing but the dataset cache.
* `ROUNDS=300` reproduces the ordering of the methods and most of the
  convergence-curve story at a third of the cost.
* `EVAL_EVERY=10` cuts evaluation 5×, at the price of coarser
  "rounds to reach X%" columns.

The non-iid split plus per-image rotation takes several minutes and is rebuilt
by every run. `--cache_dir` (on by default, `./cache`) builds it once per
`(dataset, clients, seed)` and reuses it. Each entry holds all 20 environments
as fp32 tensors — 150 000 images × 3×32×32×4 B ≈ **1.8 GB** — so budget disk
accordingly (`table8-errorbar` uses three seeds, hence three entries).
When the cache is used, the RNG is re-seeded after loading so that a cached run
and a freshly built run share the same random stream.

The cache key is `(dataset, clients, seed)` only — it does **not** know about
changes to `datasets.py`. Run `make clean-cache` after editing the split or
rotation logic, or you will keep training on the old partition.

---

## 7. Source changes made for this reproduction

All are listed here so they can be reviewed or reverted. Defaults preserve the
released behaviour except where noted.

**Required for the package to import at all**

* `fedbr/src/__init__.py` — **added**; it was missing from the release.
  `networks.py` does `from fedbr.src import cct_7_3x1_32_c100, cct_7_3x1_32`,
  but with no `__init__.py` `fedbr.src` is an implicit namespace package with
  no attributes, so `import fedbr.networks` failed with
  `ImportError: cannot import name 'cct_7_3x1_32_c100'`. It re-exports `cct`.
* `lib/misc.py` — dropped `from cv2 import transform`. `cv2` is never used in
  that file (only `torchvision.transforms` is), is not in `requirements.txt`,
  and made every entry point fail with `ModuleNotFoundError: No module named
  'cv2'`.
* `scripts/train_fed.py` — dropped `from parso import parse` (unused; `parso`
  is an IDE dependency that happened to be imported).

**Required to run on modern PyTorch**

* `algorithms.py` — replaced the `Tensor.add_(Number, Tensor)` overload
  (removed in PyTorch 2.x) with `add_(tensor, alpha=...)` in the custom
  `FedCM` / `FedProx` / `SCAFFOLD_OPT` optimizers. Same arithmetic.
* `networks.py` — `torchvision.models.vgg11(pretrained=False)` →
  `vgg11(weights=None)`; the old spelling still works but warns on every run.
* `datasets.py` — the `wilds` import is now `try/except`, so CIFAR10 runs do
  not require the WILDS dependency tree.
* `generative/style_GAN_v2.py` — `import aim` is now guarded. `aim` is only
  used for optional experiment logging (`Trainer(log=True)`), has no wheels on
  several platforms, and having it in the lock forced an sdist build that made
  `uv lock` take 25 minutes instead of 7 seconds.
* `networks.py` — `CIFAR_Vgg.forward` / `CIFAR_resnet.forward` use
  `flatten(1)` instead of `squeeze()`, which silently dropped the batch
  dimension for a final batch of size 1.
* `datasets.py` — the LDA client split draws
  `Dirichlet(0.1 * class_frequencies)`. Once a class has been fully consumed by
  earlier clients its frequency is 0, and torch ≥ 1.8 rejects a non-positive
  concentration (`ValueError: Expected parameter concentration ... to satisfy
  the constraint`); torch 1.7 did not validate, which is why the released code
  ran. The Dirichlet is now taken over the classes that still have samples,
  with exhausted classes left at probability 0 — which is exactly what the
  `reweight()` fallback a few lines below already assumed. Same fix in the
  CIFAR10 and MNIST splits. Note this changes how many random draws the split
  consumes, so the client partition is *not* bit-identical to the authors' —
  it cannot be on a different torch version in any case.

**Behaviour fix that changes the numbers (read this one)**

* `datasets.py` — `RotatedCIFAR10.rotate_dataset` guarded on `if not angle:`,
  which is true for `None` (a training environment, intended) **and for `0`**.
  The test environments are built with angles `0, 15, …, 135`, so the 0°
  (unrotated) test set was silently replaced by a set of randomly rotated
  images, and the reported mean over the 10 test environments was taken over
  nine fixed angles plus one random one. `RotatedCIFAR100.rotate_dataset` in
  the same file already spells this `if angle is None:`, which is why this
  reads as a slip rather than a design choice. Now fixed to match CIFAR100 and
  the paper's description. Revert that one line if you want the
  released-code numbers instead.

**Required for `--algorithm FedBR` to start at all**

* `hparams_registry.py` — `FedBR` was missing from the group that registers
  `mlp_width` / `mlp_depth` / `mlp_dropout`, so constructing its projection MLP
  raised `KeyError: 'mlp_width'` under default hparams.

**New knobs (defaults unchanged)**

* `networks.py` / `hparams_registry.py` — `backbone` hparam for 32×32 inputs
  (`vgg11`, `cct`, `resnet18`, `resnet18_gn`, `resnet20_gn`, `wide_resnet`,
  `mnist_cnn`). The released code hardcoded CCT; the paper uses VGG11 for
  CIFAR10, which is now the default for `RotatedCIFAR10`/`CleanCIFAR10` and CCT
  everywhere else.
* `algorithms.py` — `FedBR`'s `mu`, `lambda`, `tau1`, `tau2`, `FedProx`'s `mu`
  and `FedMix`'s mixing weight read from hparams instead of being hardcoded.
  Defaults are the previously hardcoded values. Needed for Table 11.
* `algorithms.py` — `ERM`'s and `Moon`'s SGD momentum read
  `hparams['momentum']` instead of a hardcoded 0.9. `hparams_registry.py`
  defaults it to 0.0 for CIFAR10 (Appendix A) and 0.9 elsewhere. See §4 for
  why this is not cosmetic.
* `scripts/train_fed.py` — FedBR's proxy dataset is now built only under
  `--use_Mixture`, which is the only branch that reads it. Previously every
  FedBR run downloaded and decoded the whole of CIFAR100 (for a CIFAR10 run)
  and then ignored it. Its path also honours `--data_dir` now instead of the
  hardcoded `./fedbr/data/CIFAR10`. `make data` still fetches CIFAR100 so that
  `--use_Mixture` works offline.
* `scripts/train_fed.py` — `--cache_dir`, `--eval_envs`, `--eval_subsample`,
  `--n_workers`. `--eval_envs` chooses which splits each checkpoint evaluates
  (`local` = the paper's metric, 10k images; `local+global`, the default, adds
  the fixed-angle test environments; `all` = every split, as released).
  `--n_workers` matters in containers: the repo default of 8 workers × ~30
  loaders exhausts `/dev/shm`, and since every environment is an in-memory
  `TensorDataset`, `--n_workers 0` is both safe and usually faster.
  `--eval_subsample` only exists to make `make smoke` fast and defaults to off.
* `scripts/eval_checkpoint.py` — re-scores a saved `model.pkl` on all four
  env/split groups; how the metric question in §2 was settled.
* `datasets.py` — added `CleanCIFAR10` for Appendix A's unrotated CIFAR10
  (Table 9). `RotatedCIFAR10` cannot express it, because it treats angle `0` as
  "sample a random angle per image".

**New files**

* `pyproject.toml`, `.python-version` — uv project definition.
* `Makefile`, `setup_vastai.sh` — the reproduction entry points.
* `fedbr/scripts/summarize.py`, `fedbr/scripts/plot_curves.py` — the paper's
  metrics and convergence plots from `results.jsonl`.

---

## 8. Output layout

```
output/cifar10/<run>/
  out.txt          stdout (the per-checkpoint table)
  err.txt          stderr
  results.jsonl    one JSON record per checkpoint: step, per-env accuracies,
                   loss, step_time, mem_gb, the full args and hparams
  model.pkl        final aggregated model
output/cifar10/summary.csv
figures/cifar10_convergence.png
cache/RotatedCIFAR10_envs10_seed12345.pt
```

`results.jsonl` is append-only, so a resumed or re-run experiment adds to the
existing file. Delete the run directory before re-running if you want clean
numbers. `summarize.py` reports `Finished: NO (partial)` for any run directory
without a `done` marker.
