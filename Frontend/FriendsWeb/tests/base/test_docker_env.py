"""Test the Docker environment."""
import os

import base_dir
from helpers.context import CONTEXT


def in_docker(func):
    """Skip if not in a container."""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) if CONTEXT.indocker else True
    return wrapper


class TestDocker:
    """Test the Docker environment."""

    __slots__ = ()

    @in_docker
    def test_files(self):
        """Check for files in Docker."""
        dockerenv = CONTEXT.manager_workdir / '.dockerenv'
        assert dockerenv.exists() is False
        bind_mount_app = CONTEXT.manager_workdir / 'friends' / '__init__.py'
        assert bind_mount_app.exists() is True

    @in_docker
    def test_env_variables(self):
        """Check for the env vars."""
        assert os.environ['USER'] == 'luckybot'
        assert os.environ['GID'] == '1001'
        assert os.environ['UID'] == '1000'
        assert os.environ['PWD'] == '/FriendsWeb'
