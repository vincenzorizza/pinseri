# Django settings for pinseri project.

# Common settings and globals.

import os, sys
import pinseri as project_module
import django.conf.global_settings as DEFAULT_SETTINGS
import socket

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) #pinseri
PROJECT_ROOT = os.path.dirname(os.path.realpath(project_module.__file__)) #pinseri/pinseri


DEBUG = False
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    ('Vincenzo Rizza', 'vincenzorizza6@gmail.com'),
)
MANAGERS = ADMINS
SITE_ID = 1
TIME_ZONE = 'Europe/Rome'
# Default language, that will be used for requests without language prefix
LANGUAGE_CODE = 'it'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#SETTINGS IN ALPHABETICAL ORDER

#Take into account that backends **must** be defined in AUTHENTICATION_BACKENDS_
#or Django won't pick them when trying to authenticate the user.
#Don't miss ``django.contrib.auth.backends.ModelBackend`` if using ``django.contrib.auth``
#application or users won't be able to login by username / password method.


AUTHENTICATION_BACKENDS = (
    'social.backends.open_id.OpenIdAuth',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.yahoo.YahooOpenId',
    'django.contrib.auth.backends.ModelBackend',
)


COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
    #('text/less', 'lessc {infile}'),
)
COMPRESS_CSS_FILTERS = [
    #creates absolute urls from relative ones
    'compressor.filters.css_default.CssAbsoluteFilter',
    #css minimizer
    'compressor.filters.cssmin.CSSMinFilter'
]

#Solve Lighttpd bug on I18n redirect to mysite.fcgi
FORCE_SCRIPT_NAME = ''

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'social.apps.django_app.me',
    'thirdauth',
    'compressor',
    'django_activeurl',
    #'static_precompiler',
    #'debug_toolbar',
)

# supported languages
LANGUAGES = (
    ('en', 'English'),
    ('it', 'Italiano'),
)
# Optional. If you want to use redirects, set this to True
SOLID_I18N_USE_REDIRECTS = True

LOCALE_PATHS = (
    #os.path.join(BASE_DIR, "locale"), # Assuming BASE_DIR is where your manage.py file is
    os.path.join(PROJECT_ROOT, "locale"),
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL    = '/login-error/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'solid_i18n.middleware.SolidLocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pinseri.urls.base'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '_iw9+=zl&^f!t+pny!^-#d1^q==7tvb79qy@tnq(!v0x-+^yd*'

SOCIAL_AUTH_STORAGE = 'social.apps.django_app.me.models.DjangoStorage'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/another-login-url/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association-redirect-url/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-disconnected-redirect-url/'
SOCIAL_AUTH_BACKEND_ERROR_URL = '/new-error-url/'
SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

SOCIAL_AUTH_MODELS = 'social_auth.db.mongoengine_models'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticroot')
# Additional locations of static files

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
    'static_precompiler.finders.StaticPrecompilerFinder',
)

#STATIC_PRECOMPILER_COMPILERS = (
#   'static_precompiler.compilers.CoffeeScript',
#    'static_precompiler.compilers.SASS',
#   'static_precompiler.compilers.SCSS',
#   'static_precompiler.compilers.LESS',
#)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'pinseri.settings.context_processors.solid_i18n',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pinseri.wsgi.application'

#----SOCIAL KEY ---- #CAPIRE QUALE DELLE DUE SINTASSI FUNZIONA!!!
SOCIAL_AUTH_FACEBOOK_KEY = '427750234037595'
SOCIAL_AUTH_FACEBOOK_SECRET = 'a095d61d98f7cc0861daf09497020670'
FACEBOOK_APP_ID              = '427750234037595'
FACEBOOK_API_SECRET          = 'a095d61d98f7cc0861daf09497020670'

