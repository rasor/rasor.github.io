#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
#https://github.com/getpelican/pelican/blob/master/pelican/settings.py

AUTHOR = 'rasor'
SITENAME = "Rasor\'s Tech Blog"
RELATIVE_URLS = False
#SITEURL = '.'
SITEURL = 'https://rasor.github.io'
SITETITLE = SITENAME
#SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
#SITEDESCRIPTION = '%s\'s playground' % AUTHOR
SITESUBTITLE = '... still playing with this Lego'
SITELOGO = '//s.gravatar.com/avatar/5b6cf6c4e0fa216452dccc8158bf673f?s=120'
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


DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'
STATIC_PATHS = ['img', 'static', 'pdf']
DEFAULT_METADATA = {
    'status': 'draft',
}
FAVICON = 'img/favicon.ico'
CUSTOM_CSS = 'static/custom.css'

PLUGIN_PATHS = ['C:\Program Files (x86)\Python36-32\pelican-addon-clones\pelican-plugins']
#PLUGINS = ['neighbors']
#PLUGINS = ['sitemap', 'post_stats', 'i18n_subsites']
PLUGINS = ['sitemap']

#https://github.com/alexandrevicenzi/blog/blob/master/pelicanconf.py
THEME = 'Flex'
#THEME = 'notmyidea'

TIMEZONE = 'Europe/Copenhagen'

#OG_LOCALE = 'en_US'
#LOCALE = 'en_US'
I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
DATE_FORMATS = {
    'en': DEFAULT_DATE_FORMAT,
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

# Blogroll
LINKS = (
        ('StackOverflow', 'https://stackoverflow.com/users/750989/rasor'),
        ('npm', 'https://www.npmjs.com/~rasor'),
        ('dock.io', 'https://dock.io?r=sorenraarup:aaaaCSAu'),
        ('Keybase', 'https://keybase.io/rasor'),
        ('-- CV --', 'https://stackoverflow.com/cv/rasor'),
        ('AngelList', 'https://angel.co/rasor'),
#         ('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/rasor'),
          ('linkedin', 'https://www.linkedin.com/in/rasor'),
          ('wordpress', 'https://rasor.wordpress.com'),
          ('github', 'https://github.com/rasor'),
          ('bitbucket', 'https://bitbucket.org/rasor'),
          ('rss', '/feeds/all.atom.xml'),)

DEFAULT_PAGINATION = 30

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

COPYRIGHT_NAME = AUTHOR
COPYRIGHT_YEAR = 2017
