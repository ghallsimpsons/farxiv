"""
Django settings for farxiv project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#a31#2f4d%wi78y$qp-)iezhu#c((k6v=f)9-eutvv2$zf!&al'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'farxiv',
    'registration',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Registration
ACCOUNT_ACTIVATION_DAYS = 3

LOGIN_URL = '/users/login'
LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = PROJECT_ROOT + '/media'
TEMPLATE_DIRS = (
        PROJECT_ROOT + '/templates',
        )

STATIC_URL = '/static/'

STATICFILES_DIRS = (
            os.path.join(PROJECT_ROOT, 'static/'),
            )

try:
    from local_settings import *
except:
    print "WARNING: COULD NOT IMPORT LOCAL SETTINGS"
