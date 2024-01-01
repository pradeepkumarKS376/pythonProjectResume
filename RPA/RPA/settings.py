"""
Django settings for RPA project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import socket
from pathlib import Path
import os
import django_heroku
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR4 = os.path.dirname(__file__)  # C:\Users\BCTPK1\Documents\pythonProjectResume
BASE_DIR3 = os.path.dirname(os.path.dirname(__file__))  # C:\Users\BCTPK1\Documents
BASE_DIR2 = os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))
)  # C:\Users\BCTPK1\'
Template_DIR = os.path.join(BASE_DIR2, r"RPA\template")
STATIC_DIR = os.path.join(BASE_DIR2, r"RPA\staticfiles")
Env_DIR = os.path.join(BASE_DIR2, r"RPA\RPA.env")
Mod_DIR = os.path.join(BASE_DIR2, r"RPA\RPAResume\models.py")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR2, r"RPA\RPAResume\Resume File")
load_dotenv(Env_DIR)  # or just load_dotenv() if .env is in the same folder
ROOT_URLCONF = "RPA.urls"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
# SECRET_KEY = 'django-insecure-h&#%(b#zov85weplnov2k(6zal8#h@fuovaaufe@7=!i)tp0$*'
# SECRET_KEY = os.environ['SECRET_KEY']#.get('SECRET_KEY')
SECRET_KEY = os.getenv("SECRET_KEY")

if socket.gethostname().endswith(
    ".local"
):  # True in your local computer =='AP-MBeaW5Ur0LNf':#
    DEBUG = True
    ALLOWED_HOSTS = ["*"]
else:
    DEBUG = True
    ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "RPAResume",
    "bootstrap5",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            Template_DIR,
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "RPA.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        # 'NAME': os.path.join(BASE_DIR, 'Resume.sqlite3'),
        "NAME": BASE_DIR / "Resume.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        ),
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

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR2, r"RPA\staticfiles")
STATICFILES_DIRS = [STATIC_DIR,]


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
# EMAIL_HOST_USER = Gmail.Username
# EMAIL_HOST_PASSWORD =  Gmail.Password

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = True

HOST_SCHEME = "http://"

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
django_heroku.settings(locals())
