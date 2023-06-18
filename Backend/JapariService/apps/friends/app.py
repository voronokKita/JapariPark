"""Django's configuration for Japari Park: Friends."""
from django.apps import AppConfig


class FriendsConfig(AppConfig):
    """Backend of Japari Park: Friends."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.friends'
    label = 'friends'
    verbose_name = 'Japari Park: Friends'
