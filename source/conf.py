# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
import os
import ablog
from pathlib import Path

here = os.path.abspath(".")
sys.path.append(here)
from settings.html import *
from settings.ablog import *
from settings.nbsphinx import *
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
    "ext.xref",
    "ext.nbconvert",
    "ablog",
    "sphinx_reredirects",
]

redirects = {
    # redirects from old blog setup
    "pages/maxim-kochurov/index.html": "header/about.html",
    "posts/2023/Feb/01/linear-regression-r2m2d2/index.html": "/posts/test.html",
    "posts/2022/Feb/01/interpreting-loo-pit/index.html": "/posts/test.html",
}
