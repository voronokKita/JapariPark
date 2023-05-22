"""Flask's configurations."""

import sys
from flask import Flask

from flask_app.constants import (
    FLASK_DIR, FRONTEND_WORKDIR,
    HOST, PORT, MAX_CONTENT_LENGTH,
)


# check up for the paths
flask_path_posix = FLASK_DIR.as_posix()
if flask_path_posix not in sys.path:
    sys.path.insert(0, flask_path_posix)

workdir_as_posix = FRONTEND_WORKDIR.as_posix()
if workdir_as_posix not in sys.path:
    sys.path.insert(0, workdir_as_posix)


# configure flask
FLASK_APP = Flask('JapariParkFrontend')

FLASK_APP.config.update(
    ENV='development',
    DEBUG=True,
    TESTING=True,
    PROPAGATE_EXCEPTIONS=True,
    LOGGER_NAME='flask_app_logger',
    MAX_CONTENT_LENGTH=MAX_CONTENT_LENGTH,
    HOST=HOST,
    PORT=PORT,
)
