"""
Database router for Friends app.

Each model must be passed to one of two sets:
`main_models` or `posts_models`.
"""
from apps.friends.models import TestEntry, TestPost


class FriendsRouter:
    """A router to control all queries in the friends app."""

    main_db = 'japari_friends'
    posts_db = 'japari_friends_posts'
    main_model_namespace = {TestEntry._meta.model_name}
    posts_model_namespace = {TestPost._meta.model_name}

    def db_for_read(self, model, **hints):
        """
        Point each model to its database.

        A main model to the main db; a post model to the posts db.
        """
        if model._meta.app_label != 'friends':
            return None
        elif model._meta.model_name in self.posts_model_namespace:
            return self.posts_db
        else:
            return self.main_db

    def db_for_write(self, model, **hints):
        """
        Point each model to its database.

        A main model to the main db; a post model to the posts db.
        """
        if model._meta.app_label != 'friends':
            return None
        elif model._meta.model_name in self.posts_model_namespace:
            return self.posts_db
        else:
            return self.main_db

    def allow_relation(self, obj1, obj2, **hints):
        """
        Resolve relations.

        Deny relationships from other apps to the friends app.
        Deny relations if one model from main and other model from posts.
        Allow relations if both models from the friends and
        from the same db namespace.
        """
        lb = (obj1._meta.app_label, obj2._meta.app_label)
        if 'friends' not in lb:
            return None
        elif not (lb[0] == 'friends' and lb[1] == 'friends'):
            return False

        names = (obj1._meta.model_name, obj2._meta.model_name)
        if (names[0] in self.posts_model_namespace
                and names[1] in self.posts_model_namespace):
            return True
        elif (names[0] in self.main_model_namespace
              and names[1] in self.main_model_namespace):
            return True
        else:
            return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Allow migrations in the relevant databases.

        Main models in the main db; Post models in the posts db.
        """
        if app_label != 'friends':
            return None
        elif model_name in self.posts_model_namespace:
            return db == self.posts_db
        else:
            return db == self.main_db
