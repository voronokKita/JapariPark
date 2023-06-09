"""JapariService - core tests."""
from django.test import SimpleTestCase
from django.urls import reverse

from django.conf import settings

BASE_DIR = settings.BASE_DIR
SETTINGS_DIR = BASE_DIR / 'JapariService'
APP_CONF = settings.APP_CONF


class TestCoreAppResources(SimpleTestCase):
    """Check that I didn't miss anything."""

    app_dir = APP_CONF['core'].dir
    resources = (
        app_dir / 'apps.py',
        app_dir / 'admin.py',
        app_dir / 'urls.py',
        app_dir / 'dbrouter.py',
        app_dir / 'serializers.py',
        app_dir / 'permissions.py',

        app_dir / 'views',
        app_dir / 'models',
        app_dir / 'helpers',
    )

    def test_core_app_files(self):
        """Check application files."""
        for fp in self.resources:
            self.assertTrue(fp.exists(), msg=fp)


class TestCoreAppViews(SimpleTestCase):
    """Run views through the test client."""

    def test_core_app_ping(self):
        """Application http ping."""
        response = self.client.get(reverse('core:service-ping'))
        self.assertEqual(response.status_code, 200)


class TestProjectResources(SimpleTestCase):
    """Check that I didn't miss anything."""

    resources = (
        BASE_DIR / 'Pipfile',
        BASE_DIR / 'requirements.txt',
        BASE_DIR / 'Dockerfile',
        BASE_DIR / 'docker-compose.yaml',
        BASE_DIR / 'pytest.ini',

        BASE_DIR / 'manage.py',
        BASE_DIR / 'migrate.py',
        BASE_DIR / 'JapariService',
        BASE_DIR / 'apps',

        APP_CONF['accounts'].dir,
        APP_CONF['friends'].dir,

        SETTINGS_DIR / 'helpers',
        SETTINGS_DIR / 'pathfinder.py',
        SETTINGS_DIR / 'appconf.py',
        SETTINGS_DIR / 'dbconf.py',
        SETTINGS_DIR / 'dbrouter.py',
        SETTINGS_DIR / 'settings.py',
        SETTINGS_DIR / 'urls.py',
        SETTINGS_DIR / 'wsgi.py',
        SETTINGS_DIR / 'asgi.py',
    )

    def test_project_files(self):
        """Check project files."""
        for fp in self.resources:
            self.assertTrue(fp.exists(), msg=fp)
