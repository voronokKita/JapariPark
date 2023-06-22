"""JapariService - REST serializers."""
from django.contrib.auth.models import User
from rest_framework.serializers import (
    ModelSerializer, HyperlinkedModelSerializer,
    PrimaryKeyRelatedField, ReadOnlyField,
    HyperlinkedRelatedField, HyperlinkedIdentityField,
)

from apps.core.models import ListEntry


class UserSrz(HyperlinkedModelSerializer):
    """Serializer for the User model."""

    list_entries = HyperlinkedRelatedField(view_name='core:entry-detail',
                                           many=True, read_only=True)
    url = HyperlinkedIdentityField(view_name='core:user-detail',
                                   read_only=True)

    class Meta:
        """Meta settings."""

        model = User
        fields = ('username', 'url', 'list_entries')


class ListEntrySrz(HyperlinkedModelSerializer):
    """Serializer for the ListEntry model."""

    owner = ReadOnlyField(source='owner.username')
    url = HyperlinkedIdentityField(view_name='core:entry-detail',
                                   read_only=True)

    class Meta:
        """Meta settings."""

        model = ListEntry
        fields = ('pk', 'entry_text', 'owner', 'url', 'pub_date')
