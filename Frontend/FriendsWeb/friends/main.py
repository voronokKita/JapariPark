"""
Japari Park: Friends Web - main root.

The Flask application instance must be used from here,
for all settings to work through import.
"""
import subprocess

from friends import routes
from friends.config import APPLICATION
from config import BASE_IP, BASE_PORT, GUNICORN_OPTIONS
from servers.gunicornd.config import GunicornApplication


def run_werkzeug_server():
    """Run a werkzeug mini-server."""
    APPLICATION.run(host=BASE_IP, port=BASE_PORT)


def run_gunicorn_server():
    """Run a normal server."""
    GunicornApplication(APPLICATION, GUNICORN_OPTIONS).run()


def run_gunicorn_server_with_nginx():
    """Run a normal server through a proxy."""
    # TODO
    pass
