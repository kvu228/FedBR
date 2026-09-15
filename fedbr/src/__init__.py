# Re-exports for the vendored Compact-Transformers models.
#
# `fedbr/networks.py` does `from fedbr.src import cct_7_3x1_32_c100,
# cct_7_3x1_32`, which only resolves if this package re-exports them. The file
# was missing from the release, so `fedbr.src` was an implicit namespace
# package with no attributes and importing `fedbr.networks` failed outright.
#
# Only `cct` is re-exported: `cvt` and `vit` are unused by FedBR and pull in
# further optional dependencies.
from .cct import *  # noqa: F401,F403
