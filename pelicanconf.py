#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rohit Maitri'
SITENAME = 'Rohit Maitri'
SITEDESCRIPTION = 'Fill it later.'
SITEURL = 'http://localhost:8000'

# Plugins
PLUGIN_PATHS = ['plugins/pelican-plugins']
PLUGINS = ['i18n_subsites', 'tipue_search']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# theme and theme localization
THEME = 'themes/pelican-fh5co-marble-mod'
I18N_GETTEXT_LOCALEDIR = 'themes/pelican-fh5co-marble-mod/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = 'Europe/Zurich'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
I18N_TEMPLATES_LANG = 'en_US'
DEFAULT_LANG = 'en'
LOCALE = 'en_US'

# content paths
PATH = 'content'
PAGE_PATHS = ['pages/en']
ARTICLE_PATHS = ['blog/en']

# i18n
I18N_SUBSITES = {
    'de': {
        'PAGE_PATHS': ['pages/de'],
        'ARTICLE_PATHS': ['blog/de'],
        'LOCALE': 'de_DE'
    }
}

# logo path, needs to be stored in PATH Setting
LOGO = '/images/profile_pic.jpg'

# special content
HERO = [
  {
    'image': '/images/profile_pic.jpg',
    # for multilanguage support, create a simple dict
    'title': {
      'en':'Some special content',
      'de': 'Spezieller Inhalt'
    },
    'text': {
      'en': 'Any special content you want to tease here',
      'de': 'Jeglicher spezieller Inhalt den Sie hier bewerben möchten'
    },
    'links': [
      {
        'icon': 'icon-code',
        'url': 'https://github.com/rohitmaitri/rohitmaitri.github.io',
        'text': 'Github'
      }
    ]
  }, {
    'image': '/images/profile_pic.jpg',
    # keep it a string if you dont need multiple languages
    'title': 'Uh, special too',
    # keep it a string if you dont need multiple languages
    'text': 'Keep hero.text and hero.title a string if you dont need multilanguage.',
    'links': []
  }
]
# # Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
  ('Github', 'https://www.github.com/rohitmaitri'),
  ('Linkedin', 'https://www.linkedin.com/in/RohitMaitri'),
)

ABOUT = {
  'image': '/images/about/profile_pic.jpeg',
  'mail': 'rohitmaitri@gmail.com',
  # keep it a string if you dont need multiple languages
  'text': {
    'en': 'Learn more about the creator of this theme or just drop a message.',
    'de': 'Lernen Sie den Author kennen oder hinterlassen Sie einfach eine Nachricht'
  },
  'link': 'contact.html',
  # the address is also taken for google maps
  'address': 'The Netherlands',
  'phone': '+31 6xxxxxxxx'
}

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False
PAGE_ORDER_BY = 'order'

MENUITEMS = [
  ('Archive', 'archives.html'),
  ('Contact', 'contact.html')
]

DIRECT_TEMPLATES = [
  'index',
  'tags',
  'categories',
  'authors',
  'archives',
  'search', # needed for tipue_search plugin
  'contact' # needed for the contact form
]

# setup disqus
DISQUS_SHORTNAME = 'rohitmaitriblog'
DISQUS_ON_PAGES = False # if true its just displayed on every static page, like this you can still enable it per page
