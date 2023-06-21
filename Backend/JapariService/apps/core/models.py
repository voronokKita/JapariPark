"""The JapariService core - db models."""
from django.utils import timezone
from django.db.models import (
    Manager, Model,
    CharField, DateTimeField, ForeignKey,
    CASCADE,
)


class ListEntry(Model):
    """List of rows with text."""

    objects = Manager()

    entry_text = CharField('text', max_length=200)
    pub_date = DateTimeField('date published', default=timezone.localtime)
    owner = ForeignKey(
        'auth.User', related_name='list_entries', on_delete=CASCADE,
    )

    class Meta:
        """Meta settings."""

        verbose_name = 'List entry'
        verbose_name_plural = 'List entries'
