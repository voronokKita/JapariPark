"""Japari Park: Accounts - tests."""
from django.test import SimpleTestCase
from django.urls import reverse

from django.conf import settings

APPS_CONF = settings.APPS_CONF


class TestAccountsResources(SimpleTestCase):
    """Check that I didn't miss anything."""

    app_dir = APPS_CONF.accounts['dir']
    resources = (
        app_dir / 'app.py',
        app_dir / 'admin.py',
        app_dir / 'urls.py',
        app_dir / 'views.py',
        app_dir / 'models.py',
    )

    def test_accounts_files(self):
        """Check application files."""
        for fp in self.resources:
            self.assertTrue(fp.exists(), msg=fp)


class TestAccountsViews(SimpleTestCase):
    """Run views through the test client."""

    def test_accounts_ping(self):
        """Application http ping."""
        response = self.client.get(reverse('accounts:accounts-ping'))
        self.assertEqual(response.status_code, 200)
