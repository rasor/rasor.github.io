#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '@rasor'
SITENAME = "Rasor's Tech Blog"
#SITEURL = 'https://rasor.github.io'

PATH = 'content'
STATIC_PATHS = ['img', 'pdf']

TIMEZONE = 'Europe/Copenhagen'

DEFAULT_LANG = 'EN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/rasor'),
          ('GitHub', 'https://github.com/rasor'),
          ('Wordpress', 'https://rasor.wordpress.com/'),)

DEFAULT_PAGINATION = 30

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#MARKDOWN = {
#    'extension_configs': {
#        'markdown.extensions.codehilite': {'css_class': 'highlight'},
#        'markdown.extensions.extra': {},
#        'markdown.extensions.meta': {},
#    },
#    'output_format': 'html5',
#}

