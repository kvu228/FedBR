# `fedbr.networks` does `from fedbr.src import cct_7_3x1_32_c100, cct_7_3x1_32`.
# Without this file `fedbr.src` is a namespace package and those names are not
# reachable, so importing `fedbr.networks` fails.
from .cct import *
from .vit import *