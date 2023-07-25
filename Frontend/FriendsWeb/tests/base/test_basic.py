"""Japari Park: FriendsWeb - basic tests."""
from tests.context import BASE_DIR


class TestFriendsBase:
    """Japari Park: FriendsWeb - basic tests."""

    __slots__ = ()

    def test_friends_structure(self):
        """Test that base files not removed somehow."""
        app_dir = BASE_DIR / 'FriendsWeb'
        files = {
            BASE_DIR / 'manage.py',
            BASE_DIR / 'manager',
            BASE_DIR / 'requirements.txt',

            BASE_DIR / 'mnt-logs',
            BASE_DIR / 'templates',

            app_dir,
            app_dir / 'main.py',
            app_dir / 'wsgi.py',
            app_dir / 'urls.py',
            app_dir / 'flask_init.py',
            app_dir / 'settings.py',
            app_dir / 'pathfinder.py',
            app_dir / 'views',
            app_dir / 'helpers',
        }
        for path in files:
            assert path.exists() is True
