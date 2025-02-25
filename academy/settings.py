"""
Django settings for academy project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lm$aihj4nvnq9ep6p^a2hrp5%ph(mcmqknyxv-ai^09!=p1^yd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'user',
    'checkout',
    'blog',
    'academy_app',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'academy.urls'

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
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'academy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': BASE_DIR / 'db.sqlite3',        
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

# تعيين اللغة الافتراضية (يمكنك تغييرها حسب رغبتك)
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LANGUAGES = [
    ('en', ('English')),
    ('ar', ('Arabic')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR,'locale')
]




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = '/academy_app/'
LOGOUT_REDIRECT_URL = '/'



BASE_DIR = Path(__file__).resolve().parent.parent

# settings.py

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
# في حال كان لديك مجلدات محددة لل static
STATICFILES_DIRS = [
    BASE_DIR / "static",
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Stripe Settings
STRIPE_PUBLIC_KEY = "pk_test_51Qu2zOGb4WLCDijsYuV5Syn4HXtq1Y3JlSRhI9mGXz6Q1nWXKvyvrpVCdUthoJYxVMRslmSj8fzB4QW21FYQK0sL00qZjuJput"
STRIPE_SECRET_KEY = "sk_test_51Qu2zOGb4WLCDijsEhI1Ib8N5SqfAOMemU6axHQtezB6TQcBzGeVhevz8DhbMvwXVVyjgvq3Rv6gaql9wiLhsIiW00aVwbDVLW"



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}


ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    'https://a5aa-78-172-14-251.ngrok-free.app',
    'http://a5aa-78-172-14-251.ngrok-free.app',  # إذا كنت تستخدم HTTP
]



ALLOWED_HOSTS = ['.ngrok-free.app', 'localhost', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = ['https://*.ngrok-free.app']
