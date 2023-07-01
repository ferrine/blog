# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
import os

here = os.path.abspath(".")
sys.path.append(here)
from settings import *
import yaml

# References
xref_links = yaml.safe_load(open(os.path.join(here, "xref.yaml")))

# Project info

exclude_patterns = ["_build", "**.ipynb_checkpoints"]
project = html_title = "In Search of the Holy Posterior"
copyright = "2023, Max Kochurov"
author = "Max Kochurov"
# Translation

locale_dirs = ["locale/"]  # path is example but recommended.
gettext_compact = True  # optional.

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_carousel.carousel",
    "ext.xref",
    "ablog",
    "sphinx_reredirects",
    "sphinx_design",
    "ext.nbconvert",
    "sphinx.ext.graphviz",
    "sphinxcontrib.youtube",
]
