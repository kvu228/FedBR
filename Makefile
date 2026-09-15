# FedBR (ICML 2023) - CIFAR10 reproduction
#
#   make setup            # create the uv environment
#   make data             # download CIFAR10 + build the non-iid split cache
#   make smoke            # ~2 minute end-to-end sanity check
#   make table1           # the CIFAR10 column of Table 1 (the main result)
#   make summarize        # print the table from whatever has finished
#
# `make help` lists everything. REPRODUCE.md maps each target onto the paper
# and gives the expected runtime.

SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help

# ---------------------------------------------------------------- environment
UV        ?= uv
PY        ?= $(UV) run python
DEVICE    ?= 0

# ----------------------------------------------------------------- experiment
# Appendix A, CIFAR10: 10 clients, LDA alpha=0.1, 50 local iterations,
# 1000 communication rounds, SGD lr=0.01, local batch size 32, VGG11.
DATASET       ?= RotatedCIFAR10
DATA_DIR      ?= ./fedbr/data/CIFAR10
CLIENTS       ?= 10
ROUNDS        ?= 1000
LOCAL_STEPS   ?= 50
SEED          ?= 12345
BACKBONE      ?= vgg11
LR            ?= 0.01
BATCH_SIZE    ?= 32
MOMENTUM      ?= 0.9

# Evaluate every N communication rounds. The repo default is 100 steps
# (= 2 rounds at 50 local steps), which is the resolution the paper's
# "rounds to reach X%" columns are quantized to. Raise it to trade table
# resolution for wall-clock.
EVAL_EVERY    ?= 2

# Evaluating the 10 training environments on top of the 10 test environments
# roughly triples evaluation cost and is not reported in the paper.
# 1 = only evaluate the held-out test environments.
EVAL_TEST_ONLY ?= 1

# Cap each evaluation loader at N samples. 0 = the full splits, which is what
# the paper reports. Only used to make `make smoke` finish quickly.
EVAL_SUBSAMPLE ?= 0

# DataLoader workers per loader. train_fed.py builds ~30 loaders, so the repo
# default of 8 spawns ~240 worker processes and blows up /dev/shm in a
# container. The environments are in-memory tensors, so 0 is safe and fast.
WORKERS   ?= 0

OUT       ?= ./output/cifar10
CACHE_DIR ?= ./cache
FIGURES   ?= ./figures

STEPS      := $(shell echo $$(( $(ROUNDS) * $(LOCAL_STEPS) )))
CKPT_FREQ  := $(shell echo $$(( $(EVAL_EVERY) * $(LOCAL_STEPS) )))

BASE_HPARAMS = "backbone": "$(BACKBONE)", "lr": $(LR), "batch_size": $(BATCH_SIZE), "momentum": $(MOMENTUM)

ifeq ($(EVAL_TEST_ONLY),1)
EVAL_FLAG := --eval_test_only
else
EVAL_FLAG :=
endif

# Per-target overrides, set with target-specific variables below.
HP    ?=
EXTRA ?=

# run_fed(output-name, algorithm)
#
# Skips a run that already wrote its `done` marker, so a multi-day target like
# `make table1` resumes instead of retraining everything after a dropped SSH
# session. `results.jsonl` is append-only, so re-running a finished experiment
# would also duplicate its rows. Set FORCE=1, or delete the run directory, to
# redo one.
define run_fed
	@if [ -e "$(OUT)/$(1)/done" ] && [ "$(FORCE)" != "1" ]; then \
	  echo ">>> $(1): already complete, skipping (FORCE=1 or rm -rf $(OUT)/$(1) to redo)"; \
	else \
	  echo ">>> $(1): algorithm=$(2) clients=$(CLIENTS) rounds=$(ROUNDS) seed=$(SEED) backbone=$(BACKBONE)"; \
	  rm -rf "$(OUT)/$(1)"; \
	  mkdir -p "$(OUT)"; \
	  $(PY) -m fedbr.scripts.train_fed \
	    --data_dir $(DATA_DIR) \
	    --dataset $(DATASET) \
	    --algorithm $(2) \
	    --train_envs $(CLIENTS) \
	    --steps $(STEPS) \
	    --local_steps $(LOCAL_STEPS) \
	    --checkpoint_freq $(CKPT_FREQ) \
	    --output_dir $(OUT)/$(1) \
	    --seed $(SEED) \
	    --device $(DEVICE) \
	    --cache_dir $(CACHE_DIR) \
	    --n_workers $(WORKERS) \
	    --eval_subsample $(EVAL_SUBSAMPLE) \
	    $(EVAL_FLAG) \
	    --hparams '{$(BASE_HPARAMS)$(HP)}' \
	    $(EXTRA); \
	fi
endef

# Set to 1 to re-run experiments that already completed.
FORCE ?= 0

# ========================================================================= meta
.PHONY: help
help:
	@echo "FedBR - CIFAR10 reproduction"
	@echo ""
	@echo "Setup"
	@echo "  setup              create the uv env (CUDA wheels on Linux)"
	@echo "  setup-vhl          + StyleGAN deps needed by the VHL baseline"
	@echo "  data               download CIFAR10 and pre-build the split cache"
	@echo "  smoke              short end-to-end run to validate the install"
	@echo ""
	@echo "Paper tables (CIFAR10 only)"
	@echo "  table1             Table 1 / Figure 5(a): 10 clients, 1000 rounds"
	@echo "  table2-vhl         Table 2: FedBR vs VHL (needs 'make vhl-data')"
	@echo "  table3-baselines   Table 3, 'w/o FedBR' column only - see REPRODUCE.md"
	@echo "  table5-100clients  Table 5: 100 clients, 10 sampled per round"
	@echo "  table8-errorbar    Table 8: 3 seeds for the error-bar runs"
	@echo "  table9-resnet      Table 9: ResNet18-GN, no per-client rotation"
	@echo "  table11-tau        Table 11: FedBR tau1/tau2 sweep"
	@echo "  all                table1 + table5-100clients + table11-tau"
	@echo ""
	@echo "Single runs   run-local run-fedavg run-fedprox run-moon run-dann"
	@echo "              run-groupdro run-fedbr run-mixup run-fedmix"
	@echo "              run-fedbr-mixup run-fedntd run-feddecorr run-fedcm"
	@echo ""
	@echo "Reporting"
	@echo "  summarize          accuracy / rounds-to-threshold table (+ CSV)"
	@echo "  figures            convergence curves"
	@echo ""
	@echo "Runs that already wrote a 'done' marker are skipped, so a target"
	@echo "that dies part way can simply be re-run. FORCE=1 redoes them."
	@echo ""
	@echo "Knobs  ROUNDS=$(ROUNDS) CLIENTS=$(CLIENTS) SEED=$(SEED) DEVICE=$(DEVICE)"
	@echo "       BACKBONE=$(BACKBONE) EVAL_EVERY=$(EVAL_EVERY) OUT=$(OUT)"
	@echo "       EVAL_TEST_ONLY=$(EVAL_TEST_ONLY)  ($(STEPS) steps, eval every $(CKPT_FREQ))"

# ======================================================================== setup
.PHONY: setup setup-vhl lock
setup:
	$(UV) sync
	@$(PY) -c "import torch; print('torch', torch.__version__, '| cuda available:', torch.cuda.is_available(), '|', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'cpu only')"

setup-vhl:
	$(UV) sync --extra vhl

lock:
	$(UV) lock

.PHONY: data
data:
	@mkdir -p $(DATA_DIR) $(CACHE_DIR)
	$(PY) -c "from torchvision.datasets import CIFAR10, CIFAR100; \
	  CIFAR10('$(DATA_DIR)', train=True,  download=True); \
	  CIFAR10('$(DATA_DIR)', train=False, download=True); \
	  CIFAR100('$(DATA_DIR)', train=True, download=True)"
	@echo ">>> Pre-building the non-iid split cache (a few minutes, once per seed)"
	@$(MAKE) run-fedavg ROUNDS=1 EVAL_EVERY=1 EVAL_SUBSAMPLE=64 OUT=$(CACHE_DIR)/_warmup
	@echo ">>> Cache ready in $(CACHE_DIR)"

.PHONY: smoke
smoke:
	@$(MAKE) run-fedbr ROUNDS=4 LOCAL_STEPS=5 EVAL_EVERY=1 CLIENTS=4 EVAL_SUBSAMPLE=256 OUT=$(OUT)/_smoke FORCE=1
	@$(PY) -m fedbr.scripts.summarize $(OUT)/_smoke --threshold 10 --baseline ''
	@echo ">>> smoke test OK"

# ========================================================================= runs
# Table 1 uses FedAvg as the backbone for every algorithm.
.PHONY: run-local run-fedavg run-fedprox run-moon run-dann run-groupdro \
        run-fedbr run-mixup run-fedmix run-fedbr-mixup run-fedntd \
        run-feddecorr run-fedcm run-vhl

# No-communication reference: only aggregate at step 0.
run-local: EXTRA = --local_steps $(STEPS)
run-local:
	$(call run_fed,local,ERM)

run-fedavg:
	$(call run_fed,fedavg,ERM)

run-fedprox: HP = , "fedprox_mu": 0.01
run-fedprox:
	$(call run_fed,fedprox,FedProx_algo)

run-moon: HP = , "lambda": 1.0, "mlp_width": 256
run-moon:
	$(call run_fed,moon,Moon)

run-dann: HP = , "lambda": 0.1
run-dann:
	$(call run_fed,dann,DANN)

run-groupdro: HP = , "groupdro_eta": 0.01
run-groupdro:
	$(call run_fed,groupdro,GroupDRO)

# FedBR: 32 pseudo-data built once by RSM at the start of training (Fig. 6(b)),
# tau1 = tau2 = 2.0, mu = 0.5, lambda = 1.0 (Appendix A).
run-fedbr:
	$(call run_fed,fedbr,FedBR)

run-mixup: HP = , "mixup_alpha": 0.2
run-mixup:
	$(call run_fed,mixup,Mixup)

run-fedmix: HP = , "fedmix_lambda": 0.1
run-fedmix:
	$(call run_fed,fedmix,FedMix)

run-fedbr-mixup: EXTRA = --use_Mixup
run-fedbr-mixup:
	$(call run_fed,fedbr-mixup,FedBR)

run-fedntd:
	$(call run_fed,fedntd,FedNTD)

run-feddecorr:
	$(call run_fed,feddecorr,FedDeCorr)

run-fedcm: HP = , "mixup_alpha": 0.2
run-fedcm:
	$(call run_fed,fedcm,FedCM_algo)

VHL_SAMPLES ?= 2000
run-vhl: EXTRA = --virtual_set style_GAN_init_32_c10_$(VHL_SAMPLES)
run-vhl:
	$(call run_fed,vhl-$(VHL_SAMPLES),VHL)

# ======================================================================= tables
.PHONY: table1
table1: run-fedavg run-fedprox run-moon run-dann run-groupdro run-fedbr \
        run-mixup run-fedmix run-fedbr-mixup
	@$(MAKE) summarize
	@$(MAKE) figures

.PHONY: table3-baselines
table3-baselines: run-fedavg run-fedcm run-feddecorr run-fedntd
	@$(MAKE) summarize

.PHONY: table5-100clients
table5-100clients:
	@for t in run-fedavg run-feddecorr run-fedmix run-fedprox run-mixup run-fedbr; do \
	  $(MAKE) $$t CLIENTS=100 OUT=$(OUT)-100clients || exit 1; \
	done
	@$(MAKE) summarize OUT=$(OUT)-100clients SUMMARIZE_ARGS="--threshold 35"

# Table 8: three seeds for ERM / DANN / Mixup / GroupDRO / FedBR.
SEEDS ?= 12345 23456 34567
.PHONY: table8-errorbar
table8-errorbar:
	@for s in $(SEEDS); do \
	  for t in run-fedavg run-dann run-mixup run-groupdro run-fedbr; do \
	    $(MAKE) $$t SEED=$$s OUT=$(OUT)-seed$$s || exit 1; \
	  done; \
	done
	@for s in $(SEEDS); do \
	  echo "=== seed $$s ==="; $(MAKE) summarize OUT=$(OUT)-seed$$s; \
	done

# Table 9: CIFAR10 without the per-client rotation, on a group-norm ResNet18.
.PHONY: table9-resnet
table9-resnet:
	@for t in run-fedavg run-fedprox run-moon run-fedbr; do \
	  $(MAKE) $$t DATASET=CleanCIFAR10 BACKBONE=resnet18_gn \
	              OUT=$(OUT)-resnet || exit 1; \
	done
	@$(MAKE) summarize OUT=$(OUT)-resnet SUMMARIZE_ARGS="--threshold 40"

# Table 11: FedBR under different (tau1, tau2).
.PHONY: table11-tau
table11-tau:
	@$(MAKE) _tau TAU2=0.0
	@$(MAKE) _tau TAU2=0.5
	@$(MAKE) _tau TAU2=1.0
	@$(MAKE) _tau TAU2=2.0
	@$(MAKE) summarize OUT=$(OUT)-tau SUMMARIZE_ARGS="--threshold 55 60 --baseline ''"

TAU1 ?= 2.0
TAU2 ?= 2.0
.PHONY: _tau
_tau: HP = , "fedbr_tau1": $(TAU1), "fedbr_tau2": $(TAU2)
_tau: OUT := $(OUT)-tau
_tau:
	$(call run_fed,fedbr-tau$(TAU1)-$(TAU2),FedBR)

# Table 2: FedBR (32 pseudo-data) vs VHL with 2000 virtual samples.
.PHONY: vhl-data table2-vhl
vhl-data:
	@echo ">>> Generating StyleGAN-v2 virtual data (needs a CUDA GPU, 'make setup-vhl' first)"
	$(PY) fedbr/generative/generate.py \
	  --gpu_index $(DEVICE) \
	  --root_path ./fedbr/data/generative \
	  --model style_GAN_v2_G \
	  --generate_dataset style_GAN_init_32_c10_$(VHL_SAMPLES) \
	  --batch_size 100 --sample $$(( $(VHL_SAMPLES) / 10 )) --noise_num 10 \
	  --image_resolution 32 --style_gan_style_dim 64 --style_gan_n_mlp 1 \
	  --style_gan_cmul 1

table2-vhl:
	@$(MAKE) run-vhl  OUT=$(OUT)-vhl
	@$(MAKE) run-fedbr OUT=$(OUT)-vhl
	@$(MAKE) summarize OUT=$(OUT)-vhl SUMMARIZE_ARGS="--threshold 60 --baseline ''"

.PHONY: all
all: table1
	@$(MAKE) table5-100clients
	@$(MAKE) table11-tau

# ==================================================================== reporting
SUMMARIZE_ARGS ?= --threshold 55 60
.PHONY: summarize figures
summarize:
	@$(PY) -m fedbr.scripts.summarize $(OUT) $(SUMMARIZE_ARGS) \
	  --csv $(OUT)/summary.csv

figures:
	@mkdir -p $(FIGURES)
	@$(PY) -m fedbr.scripts.plot_curves $(OUT) \
	  -o $(FIGURES)/cifar10_convergence.png \
	  --title "CIFAR10 convergence ($(CLIENTS) clients, alpha=0.1)"

# ====================================================================== cleanup
.PHONY: clean clean-cache clean-all
clean:
	rm -rf $(OUT)

clean-cache:
	rm -rf $(CACHE_DIR)

clean-all: clean clean-cache
	rm -rf $(FIGURES) .venv
