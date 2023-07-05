"""Database router for Japari Park: Accounts."""


class AccountsRouter:
    """A router to control all queries in the accounts app."""

    database = 'japari_park_accounts'

    def db_for_read(self, model, **hints):
        """Read from the accounts app models go to the [database]."""
        if model._meta.app_label == 'accounts':
            return self.database
        return None

    def db_for_write(self, model, **hints):
        """Write to the accounts app models go to the [database]."""
        if model._meta.app_label == 'accounts':
            return self.database
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Resolve relations.

        Allow relationships between tables in the accounts app.
        Reject relations from other apps.
        """
        if (obj1._meta.app_label != 'accounts'
                and obj2._meta.app_label != 'accounts'):
            return None
        return (obj1._meta.app_label == 'accounts'
                and obj2._meta.app_label == 'accounts')

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Make sure the accounts tables only appear in the [database]."""
        if app_label == 'accounts':
            return db == self.database
        return None
