templates_path = ["_templates"]

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_static_path = ["_static"]
html_css_files = [
    "css/custom.css",
]
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
html_sidebars = {"index": ["profile"]}
# options for custom templates
html_context = {
    # used in _templates/translations.html
    "available_translations": {"en": "🇬🇧", "ru": "🇷🇺"},
}
