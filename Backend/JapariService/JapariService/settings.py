"""Django's settings for JapariService."""
import secrets
from pathlib import Path

from .pathfinder import BASE_DIR, SECRETS_DIR
from .appconf import APP_CONF


DEBUG = True


# Secret key
key = SECRETS_DIR / '.django.secret'
if key.exists():
    with key.open('r') as fl:
        SECRET_KEY = fl.read().strip()
else:
    # TODO print warning
    SECRET_KEY = secrets.token_urlsafe(50)
del key


ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'apps.friends.app.FriendsConfig',
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

ROOT_URLCONF = 'JapariService.urls'

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

WSGI_APPLICATION = 'JapariService.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

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


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
