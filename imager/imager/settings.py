"""
Django settings for imager project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import dj_database_url

from configurations import Configuration

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class Base(Configuration):

    BASE_DIR = BASE_DIR

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '%v42z#ni)p_b-ka2mf&$5d3(9y45j8lb!4i)!9!01z)%$mw2d='

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    TEMPLATE_DEBUG = True

    THUMBNAIL_DEBUG = True

    ALLOWED_HOSTS = []

    # Application definition

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'imagerapp',
        'imager_images',
        'registration',
#        'debug_toolbar',
        'sorl.thumbnail',
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

    # Database
    # https://docs.djangoproject.com/en/1.7/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'imager',
            'USER': 'JustinKan',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME': 'imager',
    #         'USER': 'postgres',
    #         'PASSWORD': 'admin',
    #         'HOST': '127.0.0.1',
    #         'PORT': '5432',
    #     }
    # }

    ROOT_URLCONF = 'imager.urls'

    WSGI_APPLICATION = 'imager.wsgi.application'

    #registration
    ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window
    REGISTRATION_AUTO_LOGIN = True  # Automatically log the user in.
    LOGIN_REDIRECT_URL = '/'  # The page you want users to arrive at after they successful log in
    LOGIN_URL = '/accounts/login/'

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'US/Pacific'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.7/howto/static-files/

    STATIC_URL = '/static/'

    STATIC_PATH = os.path.join(BASE_DIR, 'static/')

    STATICFILES_DIRS = (
        STATIC_PATH,
    )

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticroot')

    # Generates url fields to media files.
    MEDIA_URL = '/media/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

    TEMPLATE_DIRS =[ os.path.join(BASE_DIR, 'imager/templates')]

    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = 'tmp/activation'


class Dev(Base):

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    DEBUG = True

    TEMPLATE_DEBUG = True

    THUMBNAIL_DEBUG = True

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'imagerapp',
        'imager_images',
        'registration',
#        'debug_toolbar',
        'sorl.thumbnail',
    )
    


    # Internationalization
    # https://docs.djangoproject.com/en/1.7/topics/i18n/
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.7/howto/static-files/

    STATIC_URL = '/static/'

    STATIC_PATH = os.path.join(BASE_DIR, 'static/')

    STATICFILES_DIRS = (
        STATIC_PATH,
    )

    # Generates url fields to media files.
    MEDIA_URL = '/media/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

    TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'imager/templates')]

    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = 'tmp/activation'


class Prod(Base):

    DEBUG = True

    TEMPLATE_DEBUG = True

    THUMBNAIL_DEBUG = True

    raise Exception(os.environ.get('DATABASE_URL'))

    DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}

    STATIC_URL = '/staticroot/'

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'imagerapp',
        'imager_images',
        'registration',
        'sorl.thumbnail',
    )


    ALLOWED_HOSTS = ['ec2-54-69-236-218.us-west-2.compute.amazonaws.com',
                     'ec2-54-68-234-113.us-west-2.compute.amazonaws.com', ]