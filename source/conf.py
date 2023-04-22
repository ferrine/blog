# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
import os
import yaml
here = os.path.abspath(".")
sys.path.append(here)

xref_links = yaml.safe_load(
    open(os.path.join(here, "xref.yaml"))
)

project = html_title = 'In Search of the Holy Posterior'
copyright = '2023, Max Kochurov'
author = 'Max Kochurov'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "ext.xref",
    "ablog",
    "sphinx_reredirects",
]

redirects = {
    # redirects from old blog setup
    "pages/maxim-kochurov/index.html": "header/about.html",
    "posts/2023/Feb/01/linear-regression-r2m2d2/index.html": "/posts/test.html",
    "posts/2022/Feb/01/interpreting-loo-pit/index.html": "/posts/test.html"
}


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
