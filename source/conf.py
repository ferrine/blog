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

# References
xref_links = yaml.safe_load(open(os.path.join(here, "xref.yaml")))

# Project info

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
    "ablog",
    "sphinx_reredirects",
]

redirects = {
    # redirects from old blog setup
    "pages/maxim-kochurov/index.html": "header/about.html",
    "posts/2023/Feb/01/linear-regression-r2m2d2/index.html": "/posts/test.html",
    "posts/2022/Feb/01/interpreting-loo-pit/index.html": "/posts/test.html",
}


templates_path = ["_templates"]

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_static_path = ["_static"]
html_favicon = "_static/favicon.ico"
html_theme = "pydata_sphinx_theme"
# options for theme templates
html_theme_options = {
    "navbar_end": ["theme-switcher", "navbar-icon-links", "translations"],
    "footer_start": ["copyright"],
    "footer_end": [],
    "show_prev_next": False,
}
html_show_sourcelink = False
html_sidebars = {"header/about": ["profile"]}
# options for custom templates
html_context = {
    # used in source/_templates/translations.html
    "available_translations": {"en": "🇬🇧", "ru": "🇷🇺"},
}
