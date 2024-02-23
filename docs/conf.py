# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

project = 'FastAPI ElasticSearch FAQ'
copyright = '2024, Gennady'
author = 'Gennady'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []
extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode", "sphinx.ext.autodoc"]

# Sphinx may not include docstrings from main.py
# if it is not explicitly configured to do so.
# By default, Sphinx looks for docstrings in modules and packages,
# but the main.py file may not be recognized as a module or package by Sphinx.
# # To include docstrings from main.py in your Sphinx documentation,
# you can explicitly configure Sphinx to include the main.py file
# by modifying the conf.py file in your Sphinx project.
# You can use the autodoc extension to automatically include docstrings from Python modules

# autodoc_mock_imports = ["main"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
