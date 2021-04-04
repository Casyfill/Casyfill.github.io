#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Philipp Kats'
SITENAME = 'City Fish'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# FLEX OPTS
COPYRIGHT_NAME = 'Philipp Kats'
COPYRIGHT_YEAR = '2018'
HOME_HIDE_TAGS = True
MAIN_MENU = True
PYGMENTS_STYLE = 'github'
DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS = (('EN', '../category/en.html'),
         ('RU', '../category/ru.html'),
         )

# Social widget
SOCIAL = (('github', 'https://github.com/Casyfill'),
          ('linkedin', 'https://www.linkedin.com/in/philipp-kats/'),)

DEFAULT_PAGINATION = 100

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')                # Add 'ipynb'
PLUGIN_PATHS = ['pelican-plugins']      # Ensure your plugin path is in it
PLUGINS = ['ipynb2pelican']             # Name of the plugin
IGNORE_FILES = ['.ipynb_checkpoints']   # Prevent parsing checkpoints files
THEME = "./theme"
STATIC_PATHS = ['static']
FAVICON = 'img/favicon.ico'
CUSTOM_CSS = 'custom.css'
SUMMARY_MAX_LENGTH = 100
LOAD_CONTENT_CACHE = False

# IPYTTHON
IPYNB_IGNORE_CSS = True
IPYNB_REMOVE_EMPTY = True