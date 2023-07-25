"""Flask application source."""
from pathlib import Path
from datetime import timedelta
from flask import Flask

from FriendsWeb.pathfinder import BASE_DIR, FLASK_CONFIG
from FriendsWeb.settings import DEBUG, SERV_STATIC, SITE_DOMAIN
from FriendsWeb.helpers import secret_key, printer, istestrun

from FriendsWeb import urls


class BaseConfig:
    """Common Flask settings."""

    APPLICATION_ROOT = BASE_DIR.as_posix()

    SERV_STATIC = SERV_STATIC

    LOGGER_NAME = 'friends_web_logger'

    CSRF_ENABLED = True
    SECRET_KEY = secret_key.getkey()

    SESSION_COOKIE_NAME = 'session'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
    MAX_COOKIE_SIZE = 4093

    USE_X_SENDFILE = True
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(minutes=5)
    MAX_CONTENT_LENGTH = pow(10, 6)

    PREFERRED_URL_SCHEME = 'http'


class DevelopmentConfig(BaseConfig):
    """Settings for a dev environment."""

    ENV = 'development'
    DEBUG = not istestrun.check()
    TESTING = istestrun.check()
    TEMPLATES_AUTO_RELOAD = True
    EXPLAIN_TEMPLATE_LOADING = True

    PROPAGATE_EXCEPTIONS = True
    TRAP_HTTP_EXCEPTIONS = True
    TRAP_BAD_REQUEST_ERRORS = True


class ProductionConfig(BaseConfig):
    """Settings for normal operations."""

    ENV = 'production'
    DEBUG = False
    TESTING = False
    TEMPLATES_AUTO_RELOAD = False
    EXPLAIN_TEMPLATE_LOADING = False

    PROPAGATE_EXCEPTIONS = False
    TRAP_HTTP_EXCEPTIONS = False
    TRAP_BAD_REQUEST_ERRORS = False


APP = Flask(
    'FriendsWeb',
    root_path=BASE_DIR.as_posix(),
    instance_path=BASE_DIR.as_posix(),
    template_folder=Path(BASE_DIR, 'templates').as_posix(),
    static_url_path='/static',
    static_folder=Path(BASE_DIR, 'static').as_posix(),
)
if DEBUG:
    APP.config.from_object(DevelopmentConfig)
else:
    APP.config.from_object(ProductionConfig)

if APP.config.from_pyfile(FLASK_CONFIG.as_posix(), silent=True):
    printer.write('[Flask has read the config file]')


# Register the urls
for route in urls.router:
    APP.add_url_rule(
        rule=route['rule'],
        view_func=route['view_func'],
        methods=route['methods'],
    )
