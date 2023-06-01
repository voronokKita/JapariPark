"""
Japari Park: Friends Web - main root.

The Flask application instance must be used from here,
for all settings to work through import.
"""
from friends import routes
from friends.constants import APPLICATION_HOST, APPLICATION_PORT
from friends.config import APPLICATION


def run_werkzeug_server():
    """Run a werkzeug mini-server."""
    APPLICATION.run(host=APPLICATION_HOST, port=APPLICATION_PORT)


def run_gunicorn_server():
    """Run a normal server."""
    # TODO
    pass


def run_gunicorn_server_with_nginx():
    """Run a normal server through a proxy."""
    # TODO
    pass
