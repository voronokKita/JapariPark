"""Django's settings for JapariService."""
from JapariService.pathfinder import BASE_DIR, SECRETS_DIR

from JapariService.appconf import APP_CONF, CONTRIB_APPS
from JapariService.dbconf import DB_CONF
from JapariService.helpers import secret_key, is_db_online

# Context switch
DEBUG = True

SECRET_KEY = secret_key.getkey()


ALLOWED_HOSTS = []
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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

drf_permissions = 'rest_framework.permissions'
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        f'{drf_permissions}.DjangoModelPermissionsOrAnonReadOnly',
    ],
}

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')


ROOT_URLCONF = 'JapariService.urls'

WSGI_APPLICATION = 'JapariService.wsgi.application'
ASGI_APPLICATION = 'JapariService.asgi.application'


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


# <database>
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
            'ATOMIC_REQUESTS': True,
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
    'apps.core.dbrouter.CoreRouter',
    'JapariService.dbrouter.DefaultRouter',
]
# </database>


# Password validation
django_validators = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': f'{django_validators}.UserAttributeSimilarityValidator'},
    {'NAME': f'{django_validators}.MinimumLengthValidator'},
    {'NAME': f'{django_validators}.CommonPasswordValidator'},
    {'NAME': f'{django_validators}.NumericPasswordValidator'},
]


# <internationalization>
DEFAULT_CHARSET = 'utf-8'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True
USE_TZ = True
USE_L10N = False

DATE_FORMAT = 'Y.n.j'
TIME_FORMAT = 'G:i:s'
DATETIME_FORMAT = 'Y.n.j G:i:s'
SHORT_DATE_FORMAT = 'Y.n.j P'
# </internationalization>


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'


# <misc>
APPEND_SLASH = False
PREPEND_WWW = False
# </misc>
