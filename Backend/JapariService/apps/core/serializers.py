"""JapariService - REST serializers."""
from django.contrib.auth.models import User
from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField, ReadOnlyField,
)

from apps.core.models import ListEntry


class UserSrz(ModelSerializer):
    """Serializer for the User model."""

    list_entries = PrimaryKeyRelatedField(
        many=True, queryset=ListEntry.objects.all(),
    )

    class Meta:
        """Meta settings."""

        model = User
        fields = ('pk', 'username', 'list_entries')


class ListEntrySrz(ModelSerializer):
    """Serializer for the ListEntry model."""

    owner = ReadOnlyField(source='owner.username')

    class Meta:
        """Meta settings."""

        model = ListEntry
        fields = ('pk', 'entry_text', 'pub_date', 'owner')
