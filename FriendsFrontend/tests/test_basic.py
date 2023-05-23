"""Japari Park: Friends - basic tests."""

from tests.context import MANAGER_DIR


class TestBase:
    """Test base."""
    __slots__ = []

    def test_project_structure(self):
        """Test base files not changed."""
        files = {
            MANAGER_DIR / 'manage.py',
            MANAGER_DIR / 'Pipfile',

            MANAGER_DIR / 'friends',
            MANAGER_DIR / 'friends' / '__init__.py',
            MANAGER_DIR / 'friends' / 'application.py',
            MANAGER_DIR / 'friends' / 'config.py',
            MANAGER_DIR / 'friends' / 'routes.py',
            MANAGER_DIR / 'friends' / 'constants.py',
            MANAGER_DIR / 'friends' / 'static',
            MANAGER_DIR / 'friends' / 'templates',
        }
        for path in files:
            assert path.exists() is True

    def test_simple_errors(self):
        """Test import works."""
        import friends
        from friends import constants
        from friends import config
        from friends import routes
        from friends import application
