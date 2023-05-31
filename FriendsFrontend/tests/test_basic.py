"""Japari Park: Friends - basic tests."""
from helpers import base_dir

MANAGER_WORKDIR = base_dir.get_path()


class TestFriendsBase:
    __slots__ = ()

    def test_friends_structure(self):
        """Test base files not removed somehow."""
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

    def test_friends_simple_errors(self):
        """Test import works and a test-constant is set."""
        from helpers import context

        import friends
        from friends import constants
        from friends import config
        from friends import routes
        from friends import main
