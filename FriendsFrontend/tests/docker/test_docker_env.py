"""Test the Docker environment."""
import os

from tests.context import MANAGER_DIR

indocker = MANAGER_DIR / 'indocker'
ISDOCKER = indocker.exists()


class TestDocker:
    __slots__ = ()

    def test_files(self):
        """Check for files in Docker."""
        dockerenv = MANAGER_DIR / '.dockerenv'
        if not ISDOCKER:
            assert dockerenv.exists() is True
        else:
            assert dockerenv.exists() is False
            bind_mount_friends = MANAGER_DIR / 'friends' / '__init__.py'
            assert bind_mount_friends.exists() is True

    def test_env_variables(self):
        """Check for the env vars."""
        if not ISDOCKER:
            pass
        else:
            assert os.environ['USER'] == 'luckybot'
            assert os.environ['GID'] == '1001'
            assert os.environ['UID'] == '1000'
            assert os.environ['PWD'] == '/FriendsFrontend'
