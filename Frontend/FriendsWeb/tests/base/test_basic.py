"""Japari Park: Friends Web - basic tests."""
import context

from helpers import base_dir
from helpers.context import get_context
import friends

MANAGER_WORKDIR = base_dir.get_path()


class TestFriendsBase:
    """Japari Park: Friends Web - basic tests."""

    __slots__ = ()

    def test_friends_structure(self):
        """Test that base files not removed somehow."""
        flaskapp_dir = MANAGER_WORKDIR / 'friends'
        files = {
            MANAGER_WORKDIR / 'manage.py',
            MANAGER_WORKDIR / 'tests',
            MANAGER_WORKDIR / 'helpers' / 'context.py',

            flaskapp_dir,
            flaskapp_dir / '__init__.py',
            flaskapp_dir / 'wsgi.py',
            flaskapp_dir / 'main.py',
            flaskapp_dir / 'config.py',
            flaskapp_dir / 'routes.py',
            flaskapp_dir / 'constants.py',
            flaskapp_dir / 'static',
            flaskapp_dir / 'templates',
        }
        for path in files:
            assert path.exists() is True

    def test_friends_context(self):
        """Test a test-context is set."""
        program_context = get_context()
        assert program_context.autotest is True
        assert program_context.development is True
