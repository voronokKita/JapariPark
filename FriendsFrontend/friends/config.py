"""Japari Park: Friends - configurations."""

import sys
from flask import Flask

from friends.constants import (
    FLASK_WORKDIR, MANAGER_DIR,
    MAX_CONTENT_LENGTH,
)


# check up for the paths
manager_as_posix = MANAGER_DIR.as_posix()
if manager_as_posix not in sys.path:
    sys.path.insert(0, manager_as_posix)

flask_path_posix = FLASK_WORKDIR.as_posix()
if flask_path_posix not in sys.path:
    sys.path.insert(0, flask_path_posix)


# configure flask
FLASK = Flask('FriendsFrontend')

FLASK.config.update(
    ENV='development',
    DEBUG=True,
    TESTING=True,
    PROPAGATE_EXCEPTIONS=True,
    LOGGER_NAME='flask_app_logger',
    MAX_CONTENT_LENGTH=MAX_CONTENT_LENGTH,
)
