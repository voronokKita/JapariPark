"""Test the Flask app with Gunicorn."""
import requests

from tests import context
from helpers.context import CONTEXT
from friends.settings import HOST_DOMAIN, SITE_PORT


class TestThroughGunicorn:
    """Test the Flask app with Gunicorn."""

    __slots__ = ()

    def test_flask_app_ping(self, gunicorn_server):
        """Simple text response."""
        if CONTEXT.in_github_ci:
            return True

        response = requests.get(
            f'http://{HOST_DOMAIN}:{SITE_PORT}/friends/ping',
            timeout=5,
        )
        assert response.status_code == 200
        assert response.text == 'pong!'
