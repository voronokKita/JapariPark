"""Test the Docker environment."""
import os

from tests.context import BASE_DIR
from FriendsWeb.helpers import isdocker


def in_docker(func):
    """Skip if not in a container."""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) if isdocker.check() else True
    return wrapper


class TestDocker:
    """Test the Docker environment."""

    __slots__ = ()

    @in_docker
    def test_files(self):
        """Check for files in Docker."""
        app = BASE_DIR / 'FriendsWeb' / '__init__.py'
        assert app.exists() is True

    @in_docker
    def test_env_variables(self):
        """Check for the env vars."""
        assert os.environ['USER'] == 'luckybot'
        assert os.environ['GROUP'] == 'luckybot'
        assert os.environ['GID'] == '1000'
        assert os.environ['UID'] == '1000'
        assert os.environ['PWD'] == '/FriendsWeb'
