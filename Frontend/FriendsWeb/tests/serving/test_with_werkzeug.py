"""Test the Flask app with Werkzeug server."""
import requests
import pytest

from tests import context
from FriendsWeb.settings import TESTPORT
from FriendsWeb.helpers import in_github_ci


@pytest.mark.skip(reason='deprecated')
class TestThroughBaseWSGIServer:
    """Test the Flask app with Werkzeug server."""

    __slots__ = ()

    def test_flask_app_ping(self, werkzeug_server):
        """Simple text response."""
        if in_github_ci.check():
            return True

        response = requests.get(
            f'http://127.0.0.1:{TESTPORT}/ping',
            timeout=5,
        )
        assert response.status_code == 200
        assert response.text == 'FriendsWeb: pong!'
