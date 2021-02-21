"""
Django settings for PetProject project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from .config import EMAIL_BACKEND, EMAIL_HOST_USER, EMAIL_USE_TLS, EMAIL_PORT, EMAIL_HOST, EMAIL_HOST_PASSWORD

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('RAZZLE_DJANGO_SECRET_KEY') if os.getenv(
    'RAZZLE_DJANGO_SECRET_KEY') else '+4h5y0lvqyx33g8cme%v%8)gep2d*l^5c!toky+x)$o&-=7%$j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.getenv('RAZZLE_DJANGO_DEBUG') else True

ALLOWED_HOSTS = ['dondj-url.herokuapp.com', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'UrlShortenerApp',
    "UserApp",
    'crispy_forms',
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

ROOT_URLCONF = 'PetProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'PetProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'url_shortener',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/user/profile'  # адрес перехода после успешного входа на сайт
LOGIN_URL = '/user/login/'  # адрес перехода не авторизованных пользователей при попытке перехода на закрытую
# для них страницу

PASSWORD_RESET_TIMEOUT_DAYS = 7  # сколько дней действительна ссылка сброса пароля

# smtp settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv('RAZZLE_EMAIL_HOST') if os.getenv('RAZZLE_EMAIL_HOST') else EMAIL_HOST
EMAIL_PORT = int(os.getenv('RAZZLE_EMAIL_PORT')) if os.getenv('RAZZLE_EMAIL_PORT') else EMAIL_PORT
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('RAZZLE_EMAIL_HOST_USER') if os.getenv('RAZZLE_EMAIL_HOST_USER') else EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = os.getenv('RAZZLE_EMAIL_HOST_PASSWORD') if os.getenv('RAZZLE_EMAIL_HOST_PASSWORD') else EMAIL_HOST_PASSWORD

CRISPY_TEMPLATE_PACK = 'bootstrap4'
# SITE_BASE_URL ='https://dondj.com/'
SITE_BASE_URL = 'http://127.0.0.1:8000/' if DEBUG else os.getenv('RAZZLE_SITE_BASE_URL')
# SITE_BASE_URL = 'https://dondj-url.herokuapp.com/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
