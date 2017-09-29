#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '@rasor'
SITENAME = "Rasor\'s Tech Blog"
SITEURL = '.'
#SITEURL = 'https://rasor.github.io'
SITETITLE = SITENAME
#SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
#SITEDESCRIPTION = '%s\'s playground' % AUTHOR
SITESUBTITLE = '... still playing with this Lego'
SITELOGO = '//s.gravatar.com/avatar/5b6cf6c4e0fa216452dccc8158bf673f?s=120'
#FAVICON = '/images/favicon.ico'
#BROWSER_COLOR = '#333333'
#PYGMENTS_STYLE = 'monokai'

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = False

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
             ('Sitemap', '/sitemap.xml'),)

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}


PATH = 'content'
STATIC_PATHS = ['img', 'pdf']

PLUGIN_PATHS = ['C:\ProgramFilesExtra\Python\Python36-32\pelican-addon-clones\pelican-plugins']
#PLUGINS = ['neighbors']
#PLUGINS = ['sitemap', 'post_stats', 'i18n_subsites']
PLUGINS = ['sitemap']

#https://github.com/alexandrevicenzi/blog/blob/master/pelicanconf.py
THEME = 'Flex'

TIMEZONE = 'Europe/Copenhagen'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
#LOCALE = 'en_US'
DATE_FORMATS = {
    'en': '%B %d, %Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/rasor'),
          ('github', 'https://github.com/rasor'),
          ('wordpress', 'https://rasor.wordpress.com/'),
          ('linkedin', 'https://www.linkedin.com/in/rasor/'),
          ('rss', '/feeds/all.atom.xml'),)

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


#Footer ---------------------------
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2017
