#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Philipp Kats'
SITENAME = 'City Fish'
SITETITLE = 'Philipp Kats'

PATH = 'content'

TIMEZONE = 'America/Detroit'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Projects', '../category/projects.html'),
         ('Blog', '../category/blog.html'),
         )

# Social widget
SOCIAL = (
          ('medium', 'https://medium.com/data-journalism'),
          ('github', 'https://github.com/Casyfill'),
          ('linkedin', 'https://www.linkedin.com/in/philipp-kats/'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ("md", "ipynb")                # Add 'ipynb'
from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]
IGNORE_FILES = ['.ipynb_checkpoints']   # Prevent parsing checkpoints files

THEME = "./theme"
STATIC_PATHS = ['static']
FAVICON = 'theme/img/favicon.ico'
CUSTOM_CSS = 'theme/stylesheet/custom.css'
USE_LESS = True
SUMMARY_MAX_LENGTH = 100
LOAD_CONTENT_CACHE = False

# IPYTTHON
IPYNB_IGNORE_CSS = True
IPYNB_REMOVE_EMPTY = True