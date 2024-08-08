# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Dev Page'
copyright = '2024'
author = 'esse LL'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx_design',
    'myst_nb',
    'sphinx_copybutton',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'changes/*.rst']

# -- Options for HTML output

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['overrides.css']
html_title = "Dev Page"

# -- Options for EPUB output
epub_show_urls = 'footnote'
