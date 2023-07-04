"""Django's configuration for the JapariService core."""
from django.apps import AppConfig


class CoreConfig(AppConfig):
    """System app of JapariService."""

    name = 'apps.core'
    label = 'core'
    verbose_name = 'JapariService core'

    def ready(self):
        """
        Initialize some code after the program starts.

        The hook will create superuser
        (and some other users), if not exist.
        """
        from apps.core.helpers import create_djusers
        create_djusers.run()
