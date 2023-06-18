"""Django's configuration for Japari Park: Accounts."""
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Backend of Japari Park: Accounts."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'
    label = 'accounts'
    verbose_name = 'Japari Park: Accounts'
