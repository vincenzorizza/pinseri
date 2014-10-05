# Django project environment-specific settings
from pinseri.settings.base import *
from django.conf.urls.static import static
from django.conf import settings

if socket.gethostname() == 'vincenzo-DOTS' or socket.gethostname() == 'vincenzo-Lenovo-IdeaPad-S510p' or socket.gethostname() == 'giles-liveconsole1':
    DEBUG = TEMPLATE_DEBUG = True
elif socket.gethostname() == 's19.wservices.ch':
    DEBUG = TEMPLATE_DEBUG = False
else:
    DEBUG = TEMPLATE_DEBUG = False

print "DEBUG = " + str(DEBUG) + " on " + socket.gethostname()

SITE_ID = 1
INTERNAL_IPS = ('127.0.0.1', )

#TODO: replace localhost with the domain name of the site
DEFAULT_FROM_EMAIL = 'messenger@pinseri'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

ALLOWED_HOSTS = [
    '127.0.0.1', # Allow domain and subdomains
    '127.0.0.1.', # Also allow FQDN and subdomains
    'vincenzorizza.pythonanywhere.com',
    'vincenzorizza.pythonanywhere.com.',
    'pinseri.it',
    'pinseri.it.',
    'www.pinseri.it',
    'www.pinseri.it.',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_ROOT, 'database/mydata.db'), # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                       # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                       # Set to empty string for default.
    }
}

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Overwrite default ROOT_URLCONF to include static file serving by Django.
# In production, this should be handled separately by your webserver or CDN.
#ROOT_URLCONF = 'pinseri.urls.dev'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
#DO NOT FORGET INITIAL SLASH, like "/static/"
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'static'),
    #"/home/vincenzo/Projects/Django/pinseri/pinseri/static",
)

#COMPRESS_URL = STATIC_URL
#COMPRESS_ROOT = STATIC_ROOT
#COMPRESS_STORAGE = "staticfiles.storage.StaticFileStorage"


