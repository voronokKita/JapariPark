"""Flask application source."""
from pathlib import Path
from flask import Flask

from FriendsWeb.settings import BASE_DIR, DEBUG, SERV_STATIC


# Base configs
APP = Flask(
    'FriendsWeb',
    root_path=BASE_DIR.as_posix(),
    template_folder=Path(BASE_DIR, 'templates').as_posix(),
)
APP.config.update(
    PROPAGATE_EXCEPTIONS=True,
    LOGGER_NAME='friends_web_logger',
)


# Static configs
if SERV_STATIC:
    APP.config.update(
        static_folder=Path(BASE_DIR, 'static').as_posix(),
        static_url_path='/static',
    )


# Environment configs
if DEBUG:
    APP.config.update(
        ENV='development',
        DEBUG=True,
        TESTING=True,
    )
else:
    APP.config.update(
        ENV='production',
        DEBUG=False,
        TESTING=False,
    )
