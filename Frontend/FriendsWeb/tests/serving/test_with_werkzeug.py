"""Test the Flask app with Werkzeug server."""
import requests

from tests import context
from helpers.context import CONTEXT
from friends.settings import HOST_DOMAIN, WERKZEUG_TESTPORT


class TestThroughBaseWSGIServer:
    """Test the Flask app with Werkzeug server."""

    __slots__ = ()

    def test_flask_app_ping(self, werkzeug_server):
        """Simple text response."""
        if CONTEXT.in_github_ci:
            return True

        response = requests.get(
            f'http://{HOST_DOMAIN}:{WERKZEUG_TESTPORT}/friends/ping',
            timeout=5,
        )
        assert response.status_code == 200
        assert response.text == 'pong!'
