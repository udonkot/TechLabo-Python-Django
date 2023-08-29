"""
Django settings for facescore project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(p+f8tfnf^wa8nh22tj9h_)4u$vft_sy_lsu#5uaq7(dgt7t-j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    'azurefaceapiservices.azurewebsites.net',
    'dxservice-techlabo-python-django.azurewebsites.net',
    '127.0.0.1',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mathfilters',
    'apps',

    # ユーザ用アプリケーション
    'apps.okayasu',
    'apps.kobayashi',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'facescore.urls'

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

WSGI_APPLICATION = 'facescore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },

    # ユーザ用データベース
    'okayasu_sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'apps/' 'okayasu/' 'db.sqlite3',
    },
    # ユーザ用データベース
    'kobayashi_sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'apps/' 'kobayashi/' 'db.sqlite3',
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_DIRS = (
#     [
#         os.path.join(BASE_DIR, "static"),
#     ]
# )


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CSRF_TRUSTED_ORIGINS = [
    'https://azurefaceapiservices.azurewebsites.net'
]


# ユーザの設定

from dotenv import load_dotenv
load_dotenv()
APP = os.getenv('LAUNCH_APP')
os.environ['APP'] = APP


# ロガーの設定

LOGS_DIR = os.path.join(BASE_DIR, 'apps', APP, 'logs')
# 'app.log'にはloggerの関数のメッセージが出力される
# 'django.log'にはフレームワーク関連のログが出力される
LOG_FILE_APP = os.path.join(LOGS_DIR, 'app.log')
LOG_FILE_DJANGO = os.path.join(LOGS_DIR, 'django.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # ログ出力フォーマットの設定
    'formatters': {
        'production': {
            # 'format': '%(asctime)s [%(levelname)s] %(process)d %(thread)d '
            #           '%(pathname)s:%(lineno)d %(message)s'
            'format': '%(asctime)s [%(levelname)s] '
                      '%(pathname)s:%(lineno)d %(funcName)s %(message)s'
        },
    },
    # ハンドラの設定
    'handlers': {
        'file.app': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            #'filename': '/var/log/{}/app.log'.format(PROJECT_NAME),
            'filename': LOG_FILE_APP,
            'formatter': 'production',
        },
        'file.django': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            #'filename': '/var/log/{}/app.log'.format(PROJECT_NAME),
            'filename': LOG_FILE_DJANGO,
            'formatter': 'production',
        },
    },
    # ロガーの設定
    'loggers': {
        # 自分で追加したアプリケーション全般のログを拾うロガー
        'app': {
            'handlers': ['file.app'],
            'level': 'DEBUG',
            'propagate': True,
            # 独自のロガークラス
            'logger_class': 'apps.python_learning.logging.logger.CustomLogger',
        },
        # Django自身が出力するログ全般を拾うロガー
        'django': {
            'handlers': ['file.django'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
