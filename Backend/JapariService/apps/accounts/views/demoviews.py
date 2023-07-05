"""Japari Park: Accounts - test views."""
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.accounts.models import TestEntry
from apps.accounts.serializers import TestEntrySrz


class TestEntryViewSet(ModelViewSet):
    """
    API for the TestEntry model.

    This viewset provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = TestEntry.objects.all()
    serializer_class = TestEntrySrz
    permission_classes = [IsAuthenticatedOrReadOnly]
