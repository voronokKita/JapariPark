"""Django's configuration for the JapariService core."""
from django.apps import AppConfig


class CoreConfig(AppConfig):
    """System app of JapariService."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
    label = 'core'
    verbose_name = 'JapariService core'
