"""Japari Park: Friends - configurations."""
from flask import Flask

from friends.constants import MAX_CONTENT_LENGTH, FLASK_DIR


# TODO a normal argument parser and startup scripts

''' Configure the environment
Examples:
  python manage.py runwith gunicorn
  python manage.py testwith werkzeug
  python manage.py testwith gunicorn nginx
  python manage.py e2e-tests
  python manage.py production

  python manage.py == testwith werkzeug
'''
ENVIRONMENT = 'test with werkzeug'


# Configure Flask
APPLICATION = Flask('FriendsFrontend', root_path=FLASK_DIR.as_posix())

APPLICATION.config.update(
    ENV='development',
    DEBUG=True,
    TESTING=True,
    PROPAGATE_EXCEPTIONS=True,
    LOGGER_NAME='flask_app_logger',
    MAX_CONTENT_LENGTH=MAX_CONTENT_LENGTH,
)
