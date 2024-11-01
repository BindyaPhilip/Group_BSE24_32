"""
Django settings for cakeaddicts project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
import sys
# settings.py

from applicationinsights import TelemetryClient

APPLICATION_INSIGHTS_KEY = os.getenv('APPLICATION_INSIGHTS_KEY','5176e78f-253f-4613-9a53-9285287185d2')

telemetry_client = TelemetryClient(APPLICATION_INSIGHTS_KEY)
if 'pytest' in sys.modules:
    # Mock the telemetry client or skip this setup
    telemetry_client = None
else:
    telemetry_client = TelemetryClient(APPLICATION_INSIGHTS_KEY)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-b0%zs_fyk!@-d03w782n+dt5y)*k!bfb!=s7g36m)823yzq%(+"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "cakestore.apps.CakestoreConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django_prometheus'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware'
]

ROOT_URLCONF = "cakeaddicts.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # 'django.template.context_processors.debug',
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
        },
    },
]

WSGI_APPLICATION = "cakeaddicts.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

STATIC_URL = "static/"
MEDIA_URL = "uploadMedia/"
# MEDIA_ROOT =  os.path.join(BASE_DIR, '/media/images')
MEDIA_ROOT = os.path.join(BASE_DIR, "media/images")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# STATICFILES_DIRS = (
#     'cakestore',
#     # os.path.join(BASE_DIR, 'static'),
#     )
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "images"),  # Root-level images directory
    os.path.join(BASE_DIR, "media"),  # Root-level media directory
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# keys for the stripe api (payment gateway)
STRIPE_SECRET_KEY = "sk_test_51LmstwIcrvW4NoX9f0FtWODlbP8XiuRtd6817oFqFa1cYvWbUZNYhrveRxCExIwzJunj3lts9uVjbm7Rm7rRUY7P002PoVLWMe"
STRIPE_PUBLISHABLE_KEY = "pk_test_51LmstwIcrvW4NoX9WGPDv6PZ52lt8oc3vq9e5ynZ3bg2EU2djQVLWM64GYsWGYOpTwKk7SCMO9ZpwdDj0UkqpXEx00KLuwwyEd"


# STMP CONFIG
from django.core.mail import send_mail

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "rujumbaleonard2@gmail.com"
EMAIL_HOST_PASSWORD = "ihkxvuxwwgmardib"
