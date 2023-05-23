"""Japari Park: Friends - main root."""

from friends import constants, routes
from friends.config import FLASK


def run_test_server():
    """Run flask's wsgi test-server."""
    FLASK.run()
