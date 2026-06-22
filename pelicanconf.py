#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Philipp Kats'
SITENAME = 'City Fish'
SITETITLE = 'Philipp Kats'

PATH = 'content'
TIMEZONE = "America/New_York"
DEFAULT_LANG = 'en'

THEME = "./theme_tufte"

# Dev: root-relative links; production SITEURL is set in publishconf.py
SITEURL = ''
RELATIVE_URLS = False

# Feeds off while developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# ---- Flat, topic-named URLs: every page lives at /slug/ ----
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
DRAFT_URL = 'drafts/{slug}/'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'

# ---- Curated nav (no auto taxonomy). Empty group => "soon". ----
NAV_GROUPS = [
    ("AI", []),
    ("Work", [
        ("Wrapping Combo", "/pycombo/"),
        ("DataFrame Schema", "/dataframe-schema/"),
    ]),
    ("Talks & Publications", [
        ("All talks & papers", "/talks-and-publications/"),
    ]),
    ("Personal", [
        ("Data Journalism", "/data-journalism/"),
    ]),
]

# Turn off the blog scaffolding we don't want in a flat, curated site
DIRECT_TEMPLATES = []
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
PERIOD_ARCHIVES_SAVE_AS = ''
USE_FOLDER_AS_CATEGORY = True

SOCIAL = (
    ('GitHub', 'https://github.com/Casyfill'),
    ('LinkedIn', 'https://www.linkedin.com/in/philipp-kats/'),
    ('CV', 'https://github.com/Casyfill/cv/releases/download/v2.2/main.pdf'),
)

MARKUP = ("md",)

# Protect LaTeX from Markdown and hand it to MathJax (arithmatex, generic mode)
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'pymdownx.arithmatex': {'generic': True},
    },
    'output_format': 'html5',
}
STATIC_PATHS = ['static']
DEFAULT_PAGINATION = False
DELETE_OUTPUT_DIRECTORY = True
LOAD_CONTENT_CACHE = False
