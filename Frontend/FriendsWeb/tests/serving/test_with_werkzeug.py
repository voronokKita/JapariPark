"""Test the Flask app with its test-server."""
import pytest
import threading
import time

import requests
from werkzeug.serving import make_server, BaseWSGIServer

import context
from friends.main import APPLICATION as app
from config import BASE_IP, BASE_PORT

TEST_PORTS = [
    BASE_PORT + 1,
    BASE_PORT + 2,
]


class WerkzeugThread(threading.Thread):
    """A thread to easily manage server's start and stop."""

    server: BaseWSGIServer
    port: int

    def __int__(self):
        threading.Thread.__init__(self)

    def run(self):
        """Code to run in thread."""
        self.server = make_server(
            host=BASE_IP, port=self.port, app=app, processes=1,
        )
        self.server.serve_forever()

    def merge(self):
        """Shutdown the server and join the thread."""
        self.server.shutdown()
        threading.Thread.join(self, 5)


class TestWithTestClient:
    """Test the Flask app with its test-server."""

    __slots__ = ()

    @pytest.fixture(scope='class')
    def client(self):
        """Get a test client."""
        yield app.test_client()

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

    @pytest.fixture(scope='class')
    def server_port(self):
        """Run a server from a separate thread."""
        port = TEST_PORTS.pop()
        server = WerkzeugThread()
        server.port = port
        server.start()
        time.sleep(0.2)
        yield port
        server.merge()

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
