#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'hanepjiv'
SITENAME = 'hanepjiv'
SITEURL = 'https://hanepjiv.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None # 'feeds/all-%s.atom.xml'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    #('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    #('You can add links in your config file', '#'),
    #('Another social link', '#'),
    ('@hanepjiv', 'http://twitter.com/hanepjiv'),
    ('Blogger', 'http://hanepjiv.blogspot.jp'),
)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
