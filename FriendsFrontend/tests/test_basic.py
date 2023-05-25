"""Japari Park: Friends - basic tests."""

from tests.context import MANAGER_DIR


class TestFriendsBase:
    __slots__ = ()

    def test_friends_structure(self):
        """Test base files not removed somehow."""
        flaskapp_dir = MANAGER_DIR / 'friends'
        files = {
            MANAGER_DIR / 'requirements.txt',
            MANAGER_DIR / 'Pipfile',

            MANAGER_DIR / 'manage.py',
            MANAGER_DIR / 'tests',

            flaskapp_dir,
            flaskapp_dir / '__init__.py',
            flaskapp_dir / 'application.py',
            flaskapp_dir / 'config.py',
            flaskapp_dir / 'routes.py',
            flaskapp_dir / 'constants.py',
            flaskapp_dir / 'static',
            flaskapp_dir / 'templates',
        }
        for path in files:
            assert path.exists() is True

    def test_friends_simple_errors(self):
        """Test import works and a test-constant is set."""
        import friends
        from friends import constants
        from friends import config
        from friends import routes
        from friends import application

        from friends.constants import TESTING, PRODUCTION_TESTING
        assert any((TESTING, PRODUCTION_TESTING))
