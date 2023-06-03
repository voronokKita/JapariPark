"""Test the Flask app with Gunicorn."""
import time
import pytest
import subprocess

import requests

from context import BASE_DIR
from config import BASE_IP, BASE_PORT


TEST_PORTS = [
    BASE_PORT + 10,
    BASE_PORT + 11,
]


class TestThroughGunicorn:
    """Test the Flask app with running Gunicorn server."""

    __slots__ = ()

    @pytest.fixture(scope='class')
    def server_port(self):
        """Run a server from a separate process."""
        port = TEST_PORTS.pop()
        command = f'gunicorn friends.wsgi:app -w 1 -b {BASE_IP}:{port}'
        gunicorn_process = subprocess.Popen(
            command.split(),
            shell=False,
            cwd=BASE_DIR.as_posix(),
        )
        time.sleep(1.01)
        yield port
        gunicorn_process.terminate()

    def test_flask_app_ping(self, server_port):
        """Simple text response."""
        response = requests.get(
            f'http://{BASE_IP}:{server_port}/friends/ping',
            timeout=5,
        )
        assert response.status_code == 200
        assert response.text == 'pong'

    def test_flask_app_ping_html(self, server_port):
        """Complex html+css+js response."""
        response = requests.get(
            f'http://{BASE_IP}:{server_port}/friends/ping-html',
            timeout=5,
        )
        assert response.status_code == 200
        assert '<!doctype html>' in response.text
        assert 'ping.css' in response.text
        assert 'ping.js' in response.text
        assert 'pong' in response.text
