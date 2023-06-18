"""JapariService - core tests."""
from django.test import SimpleTestCase
from django.urls import reverse

from django.conf import settings

BASE_DIR = settings.BASE_DIR
SETTINGS_DIR = BASE_DIR / 'JapariService'
APPS_CONF = settings.APPS_CONF


class TestCoreAppResources(SimpleTestCase):
    """Check that I didn't miss anything."""

    app_dir = APPS_CONF.core['dir']
    resources = (
        app_dir / 'app.py',
        app_dir / 'admin.py',
        app_dir / 'urls.py',
        app_dir / 'views.py',
        app_dir / 'models.py',
        app_dir / 'api.py',
    )

    def test_core_app_files(self):
        """Check application files."""
        self.assertTrue(
            all((item.exists() for item in self.resources)),
        )


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

        BASE_DIR / 'manage.py',
        BASE_DIR / 'JapariService',
        BASE_DIR / 'helpers',
        BASE_DIR / 'apps',
        BASE_DIR / 'secrets',
        BASE_DIR / 'logs',

        APPS_CONF.core['dir'],
        APPS_CONF.accounts['dir'],
        APPS_CONF.friends['dir'],

        SETTINGS_DIR / 'pathfinder.py',
        SETTINGS_DIR / 'appsconf.py',
        SETTINGS_DIR / 'settings.py',
        SETTINGS_DIR / 'urls.py',
        SETTINGS_DIR / 'wsgi.py',
        SETTINGS_DIR / 'asgi.py',
    )

    def test_project_files(self):
        """Check project files."""
        self.assertTrue(
            all((item.exists() for item in self.resources)),
        )