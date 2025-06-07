

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Klon Gladiatusa'
copyright = '2025, Mateusz Rduch, Denis Kuczka'
author = 'Mateusz Rduch, Denis Kuczka'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser',
    ]

autodoc_mock_imports = ["numpy", "django"]  
templates_path = ['_templates']
html_theme = 'sphinx_rtd_theme'

templates_path = ['_templates']
exclude_patterns = []

language = 'pl'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

import os
import sys

# Dodaj katalog C:\klon_gladiatusa do sys.path
sys.path.insert(0, os.path.abspath('C:\\klon_gladiatusa'))

# Poprawna ścieżka do settings – bo to: klon/klon_gl/settings.py
os.environ['DJANGO_SETTINGS_MODULE'] = 'klon.klon_gl.settings'

import django
django.setup()
