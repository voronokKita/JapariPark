"""Test the Flask app with Gunicorn."""
import time
import pytest
import subprocess

import requests

from context import BASE_DIR
from friends.constants import HOST

TEST_PORT_TWO = 5002


class TestThroughGunicorn:
    """Test the Flask app with running Gunicorn server."""

    __slots__ = ()

    @pytest.fixture(scope='class')
    def server(self):
        """Run a server from a separate process."""
        command = f'gunicorn friends.wsgi:app -w 1 -b {HOST}:{TEST_PORT_TWO}'
        gunicorn_process = subprocess.Popen(
            command.split(),
            shell=False,
            cwd=BASE_DIR.as_posix(),
        )
        time.sleep(1.1)
        yield True
        gunicorn_process.terminate()

    def test_flask_app_ping(self, server):
        """Simple text response."""
        response = requests.get(
            f'http://{HOST}:{TEST_PORT_TWO}/friends/ping',
            timeout=5,
        )
        assert response.status_code == 200
        assert response.text == 'pong'

    def test_flask_app_ping_html(self, server):
        """Complex html+css+js response."""
        response = requests.get(
            f'http://{HOST}:{TEST_PORT_TWO}/friends/ping-html',
            timeout=5,
        )
        assert response.status_code == 200
        assert '<!doctype html>' in response.text
        assert 'ping.css' in response.text
        assert 'ping.js' in response.text
        assert 'pong' in response.text
