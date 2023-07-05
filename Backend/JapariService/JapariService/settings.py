"""Django's settings for Japari Service."""
from JapariService.pathfinder import BASE_DIR, SECRETS_DIR, APPS_DIR

from JapariService.appconf import APP_CONF, CONTRIB_APPS
from JapariService.dbconf import DB_CONF
from JapariService.helpers import (
    secret_key, is_db_online, isdocker,
    ismanage, istestrun,
)

# Context switch
DEBUG = True

DEBUG_PROPAGATE_EXCEPTIONS = False

SECRET_KEY = secret_key.getkey()

ROOT_URLCONF = 'JapariService.urls'
APPEND_SLASH = True
PREPEND_WWW = False

WSGI_APPLICATION = 'JapariService.wsgi.application'
ASGI_APPLICATION = 'JapariService.asgi.application'


# Some context flags
ISDOCKER = isdocker.check()
ISMANAGE = ismanage.check()
ISTESTRUN = istestrun.check()


# Host settings
ALLOWED_HOSTS = [
    '[::1]',
    '127.0.0.1',
    'localhost',
    '.japari-service.rest',
]
INTERNAL_IPS = [
    '[::1]',
    '127.0.0.1',
]

# Application definition
INSTALLED_APPS = [
    'daphne',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'apps.core.apps.CoreConfig',
    'apps.accounts.app.AccountsConfig',
    'apps.friends.apps.FriendsConfig',
]

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Cache settings
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
}
CACHE_MIDDLEWARE_ALIAS = 'default'


# Django Rest Framework
drf_permissions = 'rest_framework.permissions'
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        f'{drf_permissions}.DjangoModelPermissionsOrAnonReadOnly',
    ],
}


# Templates settings
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


# <Databases>
# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if is_db_online.check():
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DB_CONF['default'].dbname,
            'USER': DB_CONF['default'].user,
            'PASSWORD': DB_CONF['default'].password,
            'HOST': DB_CONF['default'].host,
            'PORT': DB_CONF['default'].port,
            'ATOMIC_REQUESTS': True,
            'AUTOCOMMIT': True,
            'CONN_MAX_AGE': 0,
            'TEST': {
                'NAME': 'test_default',
            },
        },
        'japari_park_accounts': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DB_CONF['accounts'].dbname,
            'USER': DB_CONF['accounts'].user,
            'PASSWORD': DB_CONF['accounts'].password,
            'HOST': DB_CONF['accounts'].host,
            'PORT': DB_CONF['accounts'].port,
            'ATOMIC_REQUESTS': True,
            'AUTOCOMMIT': True,
            'CONN_MAX_AGE': 0,
            'TEST': {
                'NAME': 'test_accounts',
            },
        },
        'japari_friends': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DB_CONF['friends'].dbname,
            'USER': DB_CONF['friends'].user,
            'PASSWORD': DB_CONF['friends'].password,
            'HOST': DB_CONF['friends'].host,
            'PORT': DB_CONF['friends'].port,
            'ATOMIC_REQUESTS': True,
            'AUTOCOMMIT': True,
            'CONN_MAX_AGE': 0,
            'TEST': {
                'NAME': 'test_friends',
            },
        },
        'japari_friends_posts': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DB_CONF['friends-posts'].dbname,
            'USER': DB_CONF['friends-posts'].user,
            'PASSWORD': DB_CONF['friends-posts'].password,
            'HOST': DB_CONF['friends-posts'].host,
            'PORT': DB_CONF['friends-posts'].port,
            'ATOMIC_REQUESTS': False,
            'AUTOCOMMIT': True,
            'CONN_MAX_AGE': 0,
            'TEST': {
                'NAME': 'test_friends_posts',
            },
        },
    }
else:
    data = BASE_DIR / 'mnt-data'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': data / 'japari_park_default.sqlite3',
        },
        'japari_park_accounts': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': data / 'japari_park_accounts.sqlite3',
        },
        'japari_friends': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': data / 'japari_friends.sqlite3',
        },
        'japari_friends_posts': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': data / 'japari_friends_posts.sqlite3',
        },
    }

DATABASE_ROUTERS = [
    'apps.friends.dbrouter.FriendsRouter',
    'apps.accounts.dbrouter.AccountsRouter',
    'apps.core.dbrouter.CoreRouter',
    'JapariService.dbrouter.DefaultRouter',
]
# </Databases>


# Password validation
django_validators = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': f'{django_validators}.UserAttributeSimilarityValidator'},
    {'NAME': f'{django_validators}.MinimumLengthValidator'},
    {'NAME': f'{django_validators}.CommonPasswordValidator'},
    {'NAME': f'{django_validators}.NumericPasswordValidator'},
]


# Internationalization
USE_TZ = True
TIME_ZONE = 'Europe/Moscow'

DEFAULT_CHARSET = 'utf-8'
LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = False

DATE_FORMAT = 'Y.m.d'
TIME_FORMAT = 'G:i:s'
DATETIME_FORMAT = 'Y.m.d_G:i:s e z'
SHORT_DATE_FORMAT = 'Y.n.j P'
FIRST_DAY_OF_WEEK = 1


# CSRF
CSRF_COOKIE_DOMAIN = '.japari-park.fun'
CSRF_COOKIE_SECURE = False
CSRF_USE_SESSIONS = False
CSRF_COOKIE_AGE = 31449600


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'


if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
