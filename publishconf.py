#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://casyfill.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Drafts are a local workbench only: `make serve` (pelicanconf) still renders
# them at /drafts/, but the published site never contains them. An unlisted
# URL is still a public URL.
DRAFT_URL = ''
DRAFT_SAVE_AS = ''
DRAFT_PAGE_URL = ''
DRAFT_PAGE_SAVE_AS = ''

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""