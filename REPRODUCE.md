# Reproducing the CIFAR10 results of FedBR

This document covers the CIFAR10 half of Guo et al., *FedBR: Improving Federated
Learning on Heterogeneous Data via Local Learning Bias Reduction* (ICML 2023).
RotatedMNIST, CIFAR100 and PACS are out of scope here, though nothing below
prevents you from running them.

---

## 1. Quick start on a vast.ai instance

Pick an image with CUDA 12.4+ drivers (`pytorch/pytorch` or `nvidia/cuda` both
work — nothing from the image is used except the driver). Then:

```bash
git clone <this repo> && cd FedBR
bash setup_vastai.sh          # installs uv + make, syncs deps, downloads CIFAR10
make smoke                    # ~2 min end-to-end check - do not skip this
tmux new -s fedbr             # table1 runs for ~2 days; do not lose it to SSH
make table1                   # the main CIFAR10 result (see §5 for cost)
```

`make table1` ends by running `make summarize` and `make figures` itself, so
there is no separate reporting step — but both can also be run at any time
against a partially finished set of runs.

**Runs resume.** Each experiment writes a `done` marker when it finishes, and
the Makefile skips experiments that already have one. If `make table1` dies at
the seventh of nine algorithms, re-running it picks up there instead of
retraining the first six (which would also append duplicate rows to their
append-only `results.jsonl`). A run that died *part-way* has no marker, so it is
deleted and restarted cleanly. Use `FORCE=1`, or delete the run directory, to
redo a finished experiment.

`setup_vastai.sh` is a thin wrapper over `make setup && make data`; if `uv` is
already on the instance you can skip it and run those two targets directly.

Everything runs through `uv`, so there is no `conda`, no `pip install -r`, and
no system Python to fight with. `uv sync` resolves from `pyproject.toml` and
writes `uv.lock`; commit the lock file if you want byte-identical environments
across instances.

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

Reported metric (paper: "mean of maximum 5 test accuracies over rounds"):
`fedbr/scripts/summarize.py` averages the top-5 rounds of the mean accuracy over
the 10 held-out client environments, using the `in` split of each environment —
the same convention as the repo's own `model_selection.py`. Pass
`--split full` to reweight `in`+`out` back into the complete test set instead.

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
make run-fedbr MOMENTUM=0.0     # see §4 on the momentum question
make run-fedbr EVAL_EVERY=10    # evaluate 5x less often
make table1 EVAL_TEST_ONLY=0    # also evaluate the training environments
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
  code is what runs here; change `FedBR.__init__` if you want the paper's shape.
* **Momentum.** Appendix A says momentum 0.9 "when using CCT and ResNet",
  implying plain SGD for the VGG11 CIFAR10 runs, but the released `ERM` hardcodes
  `momentum=0.9` for every backbone. The default here follows the released code;
  `MOMENTUM=0.0` follows the paper text.
* **Baseline hyperparameters were tuned over grids** (Appendix A: FedProx μ ∈
  {0.001, 0.01, 0.1}, DANN weight ∈ {0.01, 0.1, 1}, Moon ∈ {0.01, 0.1, 1, 10},
  FedMix λ ∈ {0.01, 0.1, 0.2}, FedNTD β ∈ {1.0, 0.1}). The paper does not say
  which value won for CIFAR10. The Makefile picks one from each grid; sweep them
  yourself if you need the tuned numbers:
  `make run-fedprox HP=', "fedprox_mu": 0.1' OUT=./output/sweep/fedprox-0.1`.

---

## 5. Cost

Table 7 of the paper reports mean computation time **per step** on CIFAR10 with
VGG11: 0.29 s for FedAvg, 0.60 s for FedBR (each step updates all 10 clients).
A full 1000-round run is 50 000 steps, so roughly:

| | per run |
| --- | --- |
| FedAvg-like (ERM, Mixup, FedProx, GroupDRO) | ~4 h training |
| FedBR, Moon, VHL | ~8 h training |
| evaluation, `EVAL_TEST_ONLY=1`, `EVAL_EVERY=2` | ~1–2 h on top |
| evaluation, `EVAL_TEST_ONLY=0` | ~3× the above |

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
`(dataset, clients, seed)` and reuses it; each cache entry is ~700 MB.
When the cache is used, the RNG is re-seeded after loading so that a cached run
and a freshly built run share the same random stream.

The cache key is `(dataset, clients, seed)` only — it does **not** know about
changes to `datasets.py`. Run `make clean-cache` after editing the split or
rotation logic, or you will keep training on the old partition.

---

## 6. Source changes made for this reproduction

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

**Required to run on modern PyTorch (continued)**

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
* `algorithms.py` — `ERM`'s SGD momentum reads `hparams['momentum']`,
  default 0.9 as before.
* `scripts/train_fed.py` — FedBR's proxy dataset is now built only under
  `--use_Mixture`, which is the only branch that reads it. Previously every
  FedBR run downloaded and decoded the whole of CIFAR100 (for a CIFAR10 run)
  and then ignored it. Its path also honours `--data_dir` now instead of the
  hardcoded `./fedbr/data/CIFAR10`. `make data` still fetches CIFAR100 so that
  `--use_Mixture` works offline.
* `scripts/train_fed.py` — `--cache_dir`, `--eval_test_only`,
  `--eval_subsample`, `--n_workers`. The last one matters in containers: the
  repo default of 8 workers × ~30 loaders exhausts `/dev/shm`, and since every
  environment is an in-memory `TensorDataset`, `--n_workers 0` is both safe and
  usually faster. `--eval_subsample` only exists to make `make smoke` fast and
  defaults to off.
* `datasets.py` — added `CleanCIFAR10` for Appendix A's unrotated CIFAR10
  (Table 9). `RotatedCIFAR10` cannot express it, because it treats angle `0` as
  "sample a random angle per image".

**New files**

* `pyproject.toml`, `.python-version` — uv project definition.
* `Makefile`, `setup_vastai.sh` — the reproduction entry points.
* `fedbr/scripts/summarize.py`, `fedbr/scripts/plot_curves.py` — the paper's
  metrics and convergence plots from `results.jsonl`.

---

## 7. Output layout

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
