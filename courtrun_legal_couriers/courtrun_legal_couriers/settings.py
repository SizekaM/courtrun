"""
Django settings for courtrun_legal_couriers project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

#Order confirmed email
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtpout.secureserver.net'
EMAIL_HOST_USER = 'orders@courtrun.co.za'
EMAIL_HOST_PASSWORD = 'Courtrun@1301%'
EMAIL_PORT = 465

#Contact email
EMAIL1_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL1_USE_TLS = False
EMAIL1_USE_SSL = True
EMAIL1_HOST = 'smtp.mailgun.org'
EMAIL1_HOST_USER = 'contact@mg.courtrun.co.za'
EMAIL1_HOST_PASSWORD = '3041702008b940ccfa8a915a87e5553a-30344472-c3aac5d1'
EMAIL1_PORT = 465


from pathlib import Path
import os
import psycopg2
import django_heroku
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7-$^b3xs-lk0tjvf^n+8=do!h3_tn#p6uj#s@8d)49)r04vgf0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'courtrun_legal_couriers.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'courtrun_legal_couriers.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASE_URL = os.environ['DATABASE_URL']
#DATABASE_URL = os.environ.get('DATABASE_URL', None)
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Africa/Johannesburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

'''STATICFILES_DIRS = [
        os.path.join(BASE_DIR,'static'),
        ]'''

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

PREPEND_WWW = False

django_heroku.settings(locals())

GOOGLE_API_KEY = "AIzaSyA4IBw2ws3NQ-9q68yD26xqRf6zTE1mHUY"
