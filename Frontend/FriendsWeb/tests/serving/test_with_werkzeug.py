"""Test the Flask app with its test-server."""
import pytest
import threading
import time

import requests
from werkzeug.serving import make_server

import context
from friends.constants import HOST
from friends.main import APPLICATION as app

TEST_PORT_ONE = 5001


class WerkzeugThread(threading.Thread):
    """A thread to easily manage server's start and stop."""

    server = make_server(host=HOST, port=TEST_PORT_ONE, app=app, processes=1)

    def __int__(self):
        threading.Thread.__init__(self)

    def run(self):
        """Code to run in thread."""
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
    def server(self):
        """Run a server from a separate thread."""
        server = WerkzeugThread()
        server.start()
        time.sleep(0.2)
        yield True
        server.merge()

    def test_flask_app_ping(self, server):
        """Simple text response."""
        response = requests.get(
            f'http://{HOST}:{TEST_PORT_ONE}/friends/ping',
            timeout=5,
        )
        assert response.status_code == 200
        assert response.text == 'pong'

    def test_flask_app_ping_html(self, server):
        """Complex html+css+js response."""
        response = requests.get(
            f'http://{HOST}:{TEST_PORT_ONE}/friends/ping-html',
            timeout=5,
        )
        assert response.status_code == 200
        assert '<!doctype html>' in response.text
        assert 'ping.css' in response.text
        assert 'ping.js' in response.text
        assert 'pong' in response.text
