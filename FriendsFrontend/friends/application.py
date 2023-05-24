"""Japari Park: Friends - main root."""

from friends.constants import HOST, PORT
from friends import routes
from friends.config import FLASK


def run_test_server():
    """Run flask's wsgi test-server."""
    FLASK.run(HOST, PORT)
