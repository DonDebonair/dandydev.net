#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Daan Debie'
SITENAME = u'DandyDev.net'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

GITHUB_USER = 'DandyDev'
GITHUB_SKIP_FORK = True

TWITTER_USERNAME = 'DaanDebie'

STATIC_PATHS = ['images', 'files', 'extra/robots.txt', 'extra/favicon.ico']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Blogroll
LINKS = None

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/DaanDebie'),
          ('linkedin', 'http://www.linkedin.com/in/danieldebie'),
          ('github', 'http://github.com/DandyDev'),)

DEFAULT_PAGINATION = 5

TAG_CLOUD_MAX_ITEMS = 10

DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_TAGS_ON_SIDEBAR = True

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid']
THEME = os.path.join(os.environ.get('HOME'),
                     'projects/python/pelican-bootstrap3')

BOOTSTRAP_THEME = 'simplex'

BOOTSTRAP_NAVBAR_INVERSE = True

USE_OPEN_GRAPH = True
OPEN_GRAPH_FB_APP_ID = '202018593182706'
OPEN_GRAPH_IMAGE = 'images/dandydev.png'
TWITTER_CARDS = True

CC_LICENSE = "CC-BY-NC-SA"

PLUGIN_PATHS = [os.path.join(os.environ.get('HOME'),
                'projects/python/pelican-plugins')]

DISQUS_SITENAME = 'dandydev-dev'
ADDTHIS_PROFILE = 'ra-520d4af6518bf3c7'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'
