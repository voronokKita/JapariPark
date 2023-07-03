"""Database router for the core app."""
from django.conf import settings


class CoreRouter:
    """A router to control all queries in the core app."""

    contrib_apps = settings.CONTRIB_APPS
    database = 'default'

    def db_for_read(self, model, **hints):
        """Read from the core app models go to the [database]."""
        if model._meta.app_label == 'core':
            return self.database
        return None

    def db_for_write(self, model, **hints):
        """Write to the core app models go to the [database]."""
        if model._meta.app_label == 'core':
            return self.database
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Resolve relations.

        Allow relationships between tables in the core app.
        Allow relations between the core app and the contrib apps.
        Reject relations from other apps.
        """
        lb = (obj1._meta.app_label, obj2._meta.app_label)
        if 'core' not in lb:
            return None
        elif lb[0] == 'core' and lb[1] == 'core':
            return True
        elif lb[0] in self.contrib_apps or lb[1] in self.contrib_apps:
            return True
        else:
            return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Make sure the core app tables only appear in the [database]."""
        if app_label == 'core':
            return db == self.database
        return None
