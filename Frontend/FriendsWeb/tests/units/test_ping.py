"""Test the Flask app with test client."""
import pytest

from tests import context
from FriendsWeb.main import APP


class TestWithTestClient:
    """Test the Flask app with its test-client."""

    __slots__ = ()

    @pytest.fixture(scope='function')
    def client(self):
        """Get a test client."""
        return APP.test_client(use_cookies=False)

    def test_flask_app_ping(self, client):
        """Simple text response."""
        response = client.get('/ping')
        assert response.status_code == 200
        assert response.text == 'FriendsWeb: pong!'
