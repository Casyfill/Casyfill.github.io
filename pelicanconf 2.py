#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False
AUTHOR = 'Zillow_econ / StreetEasy econ'
SITENAME = 'research blog'
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

# Blogroll
LINKS = (('One Block Over', 'https://streeteasy.com/blog/'),
         ('Porchlight', 'https://www.zillow.com/blog/'),
         ('Zillow Research', 'https://www.zillow.com/research/'),
         ('Trulia Research', 'https://www.trulia.com/research/'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

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
IPYNB_IGNORE_CSS = True
IPYNB_REMOVE_EMPTY = True
SUMMARY_MAX_LENGTH = 100

S3_BUCKET = 'streeteasy-research/internal_blog'
