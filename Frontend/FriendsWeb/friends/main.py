"""
Japari Park: Friends Web - main root.

The Flask application instance must be used from here,
for all settings to work through import.
"""
from friends import routes
from friends.constants import HOST, PORT
from friends.config import APPLICATION, GunicornApplication


def run_werkzeug_server():
    """Run a werkzeug mini-server."""
    APPLICATION.run(host=HOST, port=PORT)


def run_gunicorn_server():
    """Run a normal server."""
    GunicornApplication().run()


def run_gunicorn_server_with_nginx():
    """Run a normal server through a proxy."""
    # TODO
    pass
