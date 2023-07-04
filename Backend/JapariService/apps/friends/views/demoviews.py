"""JapariService - Friends test views."""
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.friends.models import TestEntry
from apps.friends.serializers import TestEntrySrz


class TestEntryViewSet(ModelViewSet):
    """
    APIv3 for the TestEntry model.

    This viewset provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = TestEntry.objects.all()
    serializer_class = TestEntrySrz
    permission_classes = [IsAuthenticatedOrReadOnly]
