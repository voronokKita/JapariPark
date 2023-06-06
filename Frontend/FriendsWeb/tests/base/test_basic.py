"""Japari Park: Friends Web - basic tests."""
import base_dir
from helpers.context import CONTEXT
import friends
import servers


class TestFriendsBase:
    """Japari Park: Friends Web - basic tests."""

    __slots__ = ()

    def test_friends_structure(self):
        """Test that base files not removed somehow."""
        files = {
            CONTEXT.manager_workdir / 'manage.py',
            CONTEXT.manager_workdir / 'config.py',
            CONTEXT.manager_workdir / 'base_dir.py',

            CONTEXT.flask_dir,
            CONTEXT.flask_dir / '__init__.py',
            CONTEXT.flask_dir / 'wsgi.py',
            CONTEXT.flask_dir / 'main.py',
            CONTEXT.flask_dir / 'config.py',
            CONTEXT.flask_dir / 'routes.py',
            CONTEXT.flask_dir / 'constants.py',
            CONTEXT.flask_dir / 'static',
            CONTEXT.flask_dir / 'templates',
        }
        for path in files:
            assert path.exists() is True

    def test_friends_context(self):
        """Test that the test-context is set."""
        assert CONTEXT.autotest is True
        assert CONTEXT.development is True
        assert CONTEXT.in_production() is False
        assert CONTEXT.dev_normal() is False
        assert CONTEXT.dev_lite() is False
