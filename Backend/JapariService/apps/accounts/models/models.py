"""The Japari Park: Accounts - db models."""
from django.utils import timezone
from django.db.models import (
    Manager, Model, SmallAutoField,
    CharField, DateTimeField,
)


class TestEntry(Model):
    """List of rows with text."""

    objects = Manager()

    id = SmallAutoField(primary_key=True, blank=True, editable=False)

    text = CharField(
        'text', max_length=32, unique_for_date='pub_date',
        error_messages={'blank': 'the test neads a text'},
    )
    pub_date = DateTimeField(
        'date published', default=timezone.localtime,
        blank=True, editable=False,
    )

    class Meta:
        """Anything that’s not a field."""

        db_table = 'test_accounts'
        verbose_name = 'test accounts-app entry'
        verbose_name_plural = 'test accounts-app entries'
        ordering = ['pub_date']
        get_latest_by = ['pub_date']

    def __str__(self):
        return f'test accounts entry #{self.pk}'

    def __repr__(self):
        return f'TestEntry(text={self.text}, date={self.pub_date})'
