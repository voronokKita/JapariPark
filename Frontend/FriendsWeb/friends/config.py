"""Japari Park: Friends Web - on startup configurations."""
from flask import Flask

from friends.constants import MAX_CONTENT_LENGTH, FLASK_DIR


# Configure Flask
APPLICATION = Flask('FriendsWeb', root_path=FLASK_DIR.as_posix())

APPLICATION.config.update(
    ENV='development',
    DEBUG=True,
    TESTING=True,
    PROPAGATE_EXCEPTIONS=True,
    LOGGER_NAME='friends_flask_logger',
    MAX_CONTENT_LENGTH=MAX_CONTENT_LENGTH,
)
