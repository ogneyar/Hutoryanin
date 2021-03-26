from pathlib import Path

import os
import django_heroku

# from dotenv import load_dotenv
# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)


BASE_DIR = Path(__file__).resolve().parent.parent
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secretsecretkeY'


# SECURITY WARNING: don't run with debug turned on in production!
debug = os.getenv("DEBUG")
if debug is None:
    debug = "Да"
else:
    SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

if debug == "Да":
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web',
    'bots',
    'classes'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hutoryanin.urls'

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

WSGI_APPLICATION = 'hutoryanin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

db_url = str(os.getenv("DATABASE_URL"))

num = db_url.find("://")
base = db_url[:num]
db_url = db_url.replace(base+"://", "")

num = db_url.find(":")
user = db_url[:num]
db_url = db_url.replace(user+":", "")

num = db_url.find("@")
passw = db_url[:num]
db_url = db_url.replace(passw+"@", "")

num = db_url.find(":")
host = db_url[:num]
db_url = db_url.replace(host+":", "")

num = db_url.find("/")
port = db_url[:num]
db_url = db_url.replace(port+"/", "")

name = db_url

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'OPTIONS': {'sslmode': 'require'},
#         'NAME': name,
#         'USER': user,
#         'PASSWORD': passw,
#         'HOST': host,
#         'PORT': port,
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    base: {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {'sslmode': 'require'},
        'NAME': name,
        'USER': user,
        'PASSWORD': passw,
        'HOST': host,
        'PORT': port,
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached'
    }
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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'


django_heroku.settings(locals())
