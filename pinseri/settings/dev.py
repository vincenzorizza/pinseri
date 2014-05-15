# Django project environment-specific settings

from pinseri.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = True

SITE_ID = 1

#TODO: replace localhost with the domain name of the site
DEFAULT_FROM_EMAIL = 'messenger@pinseri'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '../database/mydata.db', # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                       # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                       # Set to empty string for default.
    }
}


TIME_ZONE = 'Canada/Eastern'

INTERNAL_IPS = ('127.0.0.1', )

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'media/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'static/'

# Overwrite default ROOT_URLCONF to include static file serving by Django.
# In production, this should be handled separately by your webserver or CDN.
ROOT_URLCONF = 'pinseri.urls.dev'

