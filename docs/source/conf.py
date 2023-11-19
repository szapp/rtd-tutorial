# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'uq4rw7demo'
copyright = '2023, Sören Zapp'
author = 'Sören Zapp'

release = uq4rw7demo.__version__
version = uq4rw7demo.__version__

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
]

autoclass_content = 'both'
autodoc_member_order = 'bysource'

napoleon_use_param = False
napoleon_use_rtype = False
napoleon_preprocess_types = True

mathjax_path = ('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/'
                'MathJax.js?config=TeX-MML-AM_CHTML')

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'attrs': ('https://www.attrs.org/en/stable/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'