"""Flask application source."""
from pathlib import Path
from flask import Flask

from friends.settings import BASE_DIR


APP = Flask(
    'FriendsWeb',
    root_path=BASE_DIR.as_posix(),
    template_folder=Path(BASE_DIR, 'templates').as_posix(),
)

APP.config.update(
    PROPAGATE_EXCEPTIONS=True,
    LOGGER_NAME='friends_web_logger',
)

APP.config.update(
    ENV='development',
    DEBUG=True,
    TESTING=True,
)
