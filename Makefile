# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
LINKCHECKDIR  = build/linkcheck
LOCALES = ru en
TRANSLATIONS = ru
TRANSIFEX_PROJECT = ferrine-github-io
TRANSIFEX_ORGANIZATION = ferrine


.PHONY: help Makefile env checklinks serve update-locale

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

env:
	micromamba create -f environment.yml -y
	curl -o- https://raw.githubusercontent.com/transifex/cli/master/install.sh | bash

checklinks:
	$(SPHINXBUILD) -b linkcheck $(SPHINXOPTS) "$(SOURCEDIR)" "$(LINKCHECKDIR)"
	@echo
	@echo "Check finished. Report is in $(LINKCHECKDIR)."

serve: html
	python -m http.server --directory $(BUILDDIR)/html

gettext:
	@echo collect project pot files
	@$(SPHINXBUILD) -M gettext "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo collect theme pot files to $(BUILDDIR)/gettext/theme.pot
	@$(eval theme_locale := $(shell python -c 'import os, pydata_sphinx_theme as theme; print(os.path.dirname(theme.__file__))')/locale/sphinx.pot)
	@cp $(theme_locale) $(BUILDDIR)/gettext/theme.pot

%/update-locale: gettext
	sphinx-intl update -p $(BUILDDIR)/gettext -l $(@D)

update-locale: $(TRANSLATIONS:%=%/update-locale)
	sphinx-intl update-txconfig-resources  --pot-dir build/gettext/ --transifex-project-name $(TRANSIFEX_PROJECT) --transifex-organization-name $(TRANSIFEX_ORGANIZATION)

%/html:
	@$(SPHINXBUILD) -b html -D language=$(@D) "$(SOURCEDIR)" "$(BUILDDIR)/html/$(@D)" $(SPHINXOPTS) $(O)

html: $(LOCALES:%=%/html)
	echo '<meta http-equiv="refresh" content="0;url=en/index.html" />' > "$(BUILDDIR)/html/index.html"
