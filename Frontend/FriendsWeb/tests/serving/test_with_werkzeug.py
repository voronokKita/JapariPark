"""Test the Flask app with Werkzeug server."""
import pytest
import requests

import base_dir
from config import WERKZEUG_TEST_PORT
from helpers.context import CONTEXT
from friends.main import APPLICATION as app


class TestWithTestClient:
    """Test the Flask app with its test-client."""

    __slots__ = ()

    @pytest.fixture(scope='function')
    def client(self):
        """Get a test client."""
        return app.test_client()

    def test_flask_app_ping(self, client):
        """Simple text response."""
        response = client.get('friends/ping')
        assert response.status_code == 200
        assert response.text == 'pong'

    def test_flask_app_ping_html(self, client):
        """Complex html+css+js response."""
        response = client.get('friends/ping-html')
        assert response.status_code == 200
        assert '<!doctype html>' in response.text
        assert 'ping.css' in response.text
        assert 'ping.js' in response.text
        assert 'pong' in response.text


class TestThroughBaseWSGIServer:
    """Test the Flask app with running Werkzeug server."""

    __slots__ = ()

    def test_flask_app_ping(self, werkzeug_server):
        """Simple text response."""
        if CONTEXT.in_github_ci:
            return True

        response = requests.get(
            f'http://127.0.0.1:{WERKZEUG_TEST_PORT}/friends/ping',
            timeout=5,
        )
        assert response.status_code == 200
        assert response.text == 'pong'

    def test_flask_app_ping_html(self, werkzeug_server):
        """Complex html+css+js response."""
        if CONTEXT.in_github_ci:
            return True

        response = requests.get(
            f'http://127.0.0.1:{WERKZEUG_TEST_PORT}/friends/ping-html',
            timeout=5,
        )
        assert response.status_code == 200
        assert '<!doctype html>' in response.text
        assert 'ping.css' in response.text
        assert 'ping.js' in response.text
        assert 'pong' in response.text
