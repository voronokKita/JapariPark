"""JapariService - REST serializers."""
from rest_framework.serializers import ModelSerializer
from apps.core.models import TestEntry


class TestEntrySrz(ModelSerializer):
    """Serializer for the TestEntry model."""

    class Meta:
        """Serializer settings."""

        model = TestEntry
        fields = ('pk', 'text', 'pub_date')
