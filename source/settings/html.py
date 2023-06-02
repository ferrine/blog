from sphinx.locale import get_translation


_ = get_translation("sphinx")

templates_path = ["_templates"]

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_static_path = ["_static"]
html_css_files = [
    "css/light/default.css",
    "css/dark/default.css",
    "css/font/text/font.css",
    "css/font/text/finlandica.css",
    "css/font/text/noto-emoji.css",
    "css/font/text/noto-serif.css",
    "css/font/code/font.css",
    "css/custom.css",
]
html_js_files = [
    # load using theme instead of relying on nbsphinx extension requirejs loader
    "require-2.3.6.min.js"
]
html_favicon = "_static/favicon.ico"
html_theme = "pydata_sphinx_theme"
# options for theme templates
html_theme_options = {
    "navbar_end": [
        "theme-switcher",
    ],
    "footer_start": ["copyright", "icon-links"],
    "footer_end": ["translations"],
    "show_prev_next": False,
    "search_bar_text": _("Search..."),
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/ferrine/",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/ferrine/",
            "icon": "fa-brands fa-linkedin-in",
            "type": "fontawesome",
        },
        {
            "name": "Email",
            "url": "mailto:max.kochurov@pymc-labs.io",
            "icon": "fa-solid fa-envelope",
            "type": "fontawesome",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/ferrine96/",
            "icon": "fa-brands fa-square-twitter",
            "type": "fontawesome",
        },
    ],
}
html_show_sourcelink = False
html_sidebars = {}
# options for custom templates
html_context = {
    # used in _templates/translations.html
    "available_translations": {"en": "🇬🇧", "ru": "🇷🇺"},
}
