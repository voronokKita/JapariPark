"""
Japari Park: Friends - main root.

The Flask application must be used from here,
for all settings to work through import.
"""

from friends import routes
from friends.constants import APPLICATION_HOST, APPLICATION_PORT
from friends.config import APPLICATION


def run_werkzeug_server():
    """Run the werkzeug mini-server."""
    APPLICATION.run(host=APPLICATION_HOST, port=APPLICATION_PORT)


def run_gunicorn_server():
    """Run normal server."""
    # TODO
    ...


def run_gunicorn_server_with_nginx():
    """Run normal server through a proxy."""
    # TODO
    ...
