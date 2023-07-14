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
LOCALES       = ru en
TRANSLATIONS  = ru
TRANSIFEX_PROJECT = ferrine-github-io
TRANSIFEX_ORGANIZATION = ferrine
METRIKA_ID	  = 94179175
# literally no idea how to make this properly
EXTRA_POTS = ./scripts/extra-pot
POTS = pydata_sphinx_theme:/locale/sphinx.pot ablog:/locales/sphinx.pot
export

.PHONY: help Makefile gettext checklinks serve update-locale install-pandoc

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

install-pandoc:
    # install pandoc binary using pypandoc
	python -c 'import pypandoc, sys, os, tempfile; pypandoc.download_pandoc( \
		targetfolder=os.path.dirname(sys.executable), \
		delete_installer=True, download_folder=tempfile.mkdtemp() \
		)'

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
	@mkdir -p $(BUILDDIR)/gettext/
	@touch $(BUILDDIR)/gettext/sphinx.pot
	@$(SPHINXBUILD) -M gettext "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo merge extra pot files to $(BUILDDIR)/gettext/sphinx.pot
	@msgcat $(BUILDDIR)/gettext/sphinx.pot $(shell $(EXTRA_POTS) $(POTS)) > $(BUILDDIR)/gettext/sphinx-m.pot
	@mv $(BUILDDIR)/gettext/sphinx-m.pot $(BUILDDIR)/gettext/sphinx.pot


%/update-locale: gettext
	sphinx-intl update -p $(BUILDDIR)/gettext -l $(@D)

update-locale: $(TRANSLATIONS:%=%/update-locale)
	sphinx-intl update-txconfig-resources  --pot-dir build/gettext/ --transifex-project-name $(TRANSIFEX_PROJECT) --transifex-organization-name $(TRANSIFEX_ORGANIZATION)

%/html:
	@$(SPHINXBUILD) -W -b html -t $(@D) -D language=$(@D) "$(SOURCEDIR)" "$(BUILDDIR)/html/$(@D)" $(SPHINXOPTS) $(O)

html: $(LOCALES:%=%/html)
	jinja2 source/_templates/redirect.html -D redirect_to=/en/index.html -D metrika_id=$(METRIKA_ID) > $(BUILDDIR)/html/index.html
