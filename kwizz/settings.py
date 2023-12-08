"""
Django settings for kwizz project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-na(scspqoh_!4qq&@*gggh39q6p=2t8i8+o0=wp9yli)7x^!#q'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = os.getenv("DEBUG", "False").lower() in ["yes", "true", "1", "on"]

ALLOWED_HOSTS = [
    "kwizz-app-app-0258d5adb35cac548-duefjrmtca-uc.a.run.app",
    "kwizz.adaptable.app",
    "localhost"
]
# ALLOWED_HOSTS = ['192.168.208.29']
# ALLOWED_HOSTS = ['192.168.208.145']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "host",
    "client",
    "home",
    "login",
    "rest_framework",
    'corsheaders',
]

CORS_ORIGIN_WHITELIST = (
    'https://kwizz.adaptable.app',
    'https://kwizz-app-app-0258d5adb35cac548-duefjrmtca-uc.a.run.app',
    'http://localhost:8000',
)

CSRF_TRUSTED_ORIGINS = [
    'https://kwizz.adaptable.app',
    'https://kwizz-app-app-0258d5adb35cac548-duefjrmtca-uc.a.run.app',
    'http://localhost:8000',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kwizz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'context_processors.main_context_processor.base_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'kwizz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# for postgres with database url
DATABASES = {
    'default': dj_database_url.config(default=os.getenv("DATABASE_URL"))
}

# for postgres
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'kwizz',
#         'USER': 'postgres',
#         'PASSWORD': '123',
#         'HOST': 'localhost',
#         'PORT': '5432'
#     }
# }

# For sqlite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # project-level static folder
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
