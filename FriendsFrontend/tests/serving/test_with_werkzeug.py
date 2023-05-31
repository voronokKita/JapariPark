"""Test the Flask app with its test-server."""
import pytest
from friends.main import APPLICATION as app


class TestFlaskApp:
    __slots__ = ()

    @pytest.fixture(scope='class')
    def client(self):
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
