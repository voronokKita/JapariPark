"""Flask application source."""
from pathlib import Path
from flask import Flask

from FriendsWeb.pathfinder import BASE_DIR, FLASK_CONFIG
from FriendsWeb.settings import DEBUG, SERV_STATIC
from FriendsWeb.helpers import secret_key, printer


class BaseConfig:
    """Common Flask settings."""

    PROPAGATE_EXCEPTIONS = True
    LOGGER_NAME = 'friends_web_logger'

    CSRF_ENABLED = True
    SECRET_KEY = secret_key.getkey()

    SERV_STATIC = SERV_STATIC


class DevelopmentConfig(BaseConfig):
    """Settings for a dev environment."""

    ENV = 'development'
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """Settings for normal operations."""

    ENV = 'production'
    DEBUG = False
    TESTING = False


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
