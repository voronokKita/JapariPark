"""The WSGI entry point."""

from friends.main import APPLICATION as app


def get_app():
    """
    Let it be.

    :return: a Flask application
    """
    return app
