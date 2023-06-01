"""Test the Docker environment."""
import os

import context
from helpers import base_dir
from helpers.context import get_context

MANAGER_WORKDIR = base_dir.get_path()
PROGRAM_CONTEXT = get_context()


def in_docker(func):
    """Skip if not in a container."""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) if PROGRAM_CONTEXT.indocker else None
    return wrapper


class TestDocker:
    """Test the Docker environment."""

    __slots__ = ()

    @in_docker
    def test_files(self):
        """Check for files in Docker."""
        dockerenv = MANAGER_WORKDIR / '.dockerenv'
        assert dockerenv.exists() is False
        bind_mount_friends = MANAGER_WORKDIR / 'friends' / '__init__.py'
        assert bind_mount_friends.exists() is True

    @in_docker
    def test_env_variables(self):
        """Check for the env vars."""
        assert os.environ['USER'] == 'luckybot'
        assert os.environ['GID'] == '1001'
        assert os.environ['UID'] == '1000'
        assert os.environ['PWD'] == '/FriendsWeb'
