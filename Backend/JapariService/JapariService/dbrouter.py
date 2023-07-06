"""Default router."""
from JapariService.appconf import CONTRIB_APPS


class DefaultRouter:
    """
    Default router.

    The final router that will route all
    remaining requests to the default database.
    """

    contrib_apps = CONTRIB_APPS
    database = 'default'

    def db_for_read(self, model, **hints):
        """Read to the default db."""
        return self.database

    def db_for_write(self, model, **hints):
        """Write to the default db."""
        return self.database

    def allow_relation(self, obj1, obj2, **hints):
        """Relations to the default db."""
        return (obj1._meta.app_label in self.contrib_apps
                and obj2._meta.app_label in self.contrib_apps)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Migrations to the default db."""
        return db == self.database
