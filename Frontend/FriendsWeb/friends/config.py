"""Japari Park: Friends Web application - on startup configurations."""
from flask import Flask

from helpers.context import CONTEXT


APPLICATION = Flask('FriendsWeb', root_path=CONTEXT.flask_dir.as_posix())
APPLICATION.config.update(
    PROPAGATE_EXCEPTIONS=True,
    LOGGER_NAME='friends_flask_logger',
)


if CONTEXT.in_production():
    APPLICATION.config.update(
        ENV='production',
        DEBUG=False,
        TESTING=False,
    )
else:
    APPLICATION.config.update(
        ENV='development',
        DEBUG=True,
        TESTING=True,
    )
