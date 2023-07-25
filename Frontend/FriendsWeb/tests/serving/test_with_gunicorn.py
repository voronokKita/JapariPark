"""Test the Flask app with Gunicorn."""
import requests

from tests import context
from FriendsWeb.settings import TESTPORT
from FriendsWeb.helpers import in_github_ci


class TestThroughGunicorn:
    """Test the Flask app with Gunicorn."""

    __slots__ = ()

    def test_flask_app_ping(self, gunicorn_server):
        """Simple text response."""
        if in_github_ci.check():
            return True

        response = requests.get(
            f'http://127.0.0.1:{TESTPORT}/ping',
            timeout=5,
        )
        assert response.status_code == 200
        assert response.text == 'FriendsWeb: pong!'
