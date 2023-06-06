"""Test with normal serving configuration."""
import requests

import base_dir
from config import SITE_PORT
from helpers.context import CONTEXT


class TestThroughGuWithNx:
    """Test the Flask app with Gunicorn + NGINX."""

    __slots__ = ()

    def test_flask_app_ping(self, gunicorn_server, nginx_server):
        """Simple text response."""
        if CONTEXT.in_github_ci:
            return True

        response = requests.get(
            f'http://127.0.0.1:{SITE_PORT}/friends/ping',
            timeout=5,
        )
        assert response.status_code == 200
        assert response.text == 'pong'

    def test_flask_app_ping_html(self, gunicorn_server, nginx_server):
        """Complex html+css+js response."""
        if CONTEXT.in_github_ci:
            return True

        response = requests.get(
            f'http://127.0.0.1:{SITE_PORT}/friends/ping-html',
            timeout=5,
        )
        assert response.status_code == 200
        assert '<!doctype html>' in response.text
        assert 'ping.css' in response.text
        assert 'ping.js' in response.text
        assert 'pong' in response.text
