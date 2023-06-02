# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SHELL		  = poetry run sh -c
.SHELLFLAGS	  =
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
LINKCHECKDIR  = build/linkcheck
LOCALES = ru en
TRANSLATIONS = ru
TRANSIFEX_PROJECT = ferrine-github-io
TRANSIFEX_ORGANIZATION = ferrine
# literally no idea how to make this properly
EXTRA_POTS = ./scripts/extra-pot
POTS = pydata_sphinx_theme:/locale/sphinx.pot ablog:/locales/sphinx.pot

.PHONY: help Makefile gettext checklinks serve update-locale

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

checklinks:
	$(SPHINXBUILD) -b linkcheck $(SPHINXOPTS) "$(SOURCEDIR)" "$(LINKCHECKDIR)"
	@echo
	@echo "Check finished. Report is in $(LINKCHECKDIR)."

serve:
	python -m http.server --directory $(BUILDDIR)/html

gettext:
	@echo collect project pot files
	@$(SPHINXBUILD) -M gettext "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo merge extra pot files to $(BUILDDIR)/gettext/sphinx.pot
	@msgcat $(BUILDDIR)/gettext/sphinx.pot $(shell $(EXTRA_POTS) $(POTS)) > $(BUILDDIR)/gettext/sphinx-m.pot
	@mv $(BUILDDIR)/gettext/sphinx-m.pot $(BUILDDIR)/gettext/sphinx.pot


%/update-locale: gettext
	sphinx-intl update -p $(BUILDDIR)/gettext -l $(@D)

update-locale: $(TRANSLATIONS:%=%/update-locale)
	sphinx-intl update-txconfig-resources  --pot-dir build/gettext/ --transifex-project-name $(TRANSIFEX_PROJECT) --transifex-organization-name $(TRANSIFEX_ORGANIZATION)

%/html:
	@$(SPHINXBUILD) -b html -t $(@D) -D language=$(@D) "$(SOURCEDIR)" "$(BUILDDIR)/html/$(@D)" $(SPHINXOPTS) $(O)

html: $(LOCALES:%=%/html)
	echo '<meta http-equiv="refresh" content="0;url=en/index.html" />' > "$(BUILDDIR)/html/index.html"
