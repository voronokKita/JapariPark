"""Django's settings for JapariService."""
from JapariService.pathfinder import BASE_DIR
from JapariService.appsconf import APPS_CONF
from helpers import secret_key

# Context switch
DEBUG = True


SECRET_KEY = secret_key.getkey()


ALLOWED_HOSTS = [
    '[::1]',
    '127.0.0.1',
    'localhost',
    'japari-service.rest',
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

    'apps.core.app.CoreConfig',
    'apps.accounts.app.AccountsConfig',
    'apps.friends.app.FriendsConfig',
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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
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


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}


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

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# <misc>
APPEND_SLASH = False
PREPEND_WWW = False
# </misc>
