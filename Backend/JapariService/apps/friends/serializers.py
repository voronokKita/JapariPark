"""Japari Park: Friends - REST serializers."""
from rest_framework.serializers import ModelSerializer
from apps.friends.models import TestEntry, TestPost


class TestEntrySrz(ModelSerializer):
    """Serializer for the TestEntry model."""

    class Meta:
        """Serializer settings."""

        model = TestEntry
        fields = ('pk', 'text', 'pub_date')


class TestPostSrz(ModelSerializer):
    """Serializer for the TestPost model."""

    class Meta:
        """Serializer settings."""

        model = TestPost
        fields = ('pk', 'text', 'pub_date')
