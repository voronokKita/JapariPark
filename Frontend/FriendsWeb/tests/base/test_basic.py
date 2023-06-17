"""Japari Park: Friends Web - basic tests."""
from tests.context import BASE_DIR
from helpers.context import CONTEXT
import friends


class TestFriendsBase:
    """Japari Park: Friends Web - basic tests."""

    __slots__ = ()

    def test_friends_structure(self):
        """Test that base files not removed somehow."""
        app_dir = BASE_DIR / 'friends'
        files = {
            BASE_DIR / 'manage.py',
            BASE_DIR / 'requirements.txt',

            BASE_DIR / 'logs',
            BASE_DIR / 'templates',

            app_dir,
            app_dir / '__init__.py',
            app_dir / 'main.py',
            app_dir / 'wsgi.py',
            app_dir / 'urls.py',
            app_dir / 'flask_init.py',
            app_dir / 'settings.py',
            app_dir / 'pathfinder.py',
            app_dir / 'exceptions.py',
            app_dir / 'gunicorn_wrapper.py',
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
