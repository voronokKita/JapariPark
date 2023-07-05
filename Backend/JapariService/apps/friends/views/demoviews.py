"""JapariService - Friends test views."""
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.friends.models import TestEntry, TestPost
from apps.friends.serializers import TestEntrySrz, TestPostSrz


class TestEntryViewSet(ModelViewSet):
    """
    API for the TestEntry model.

    This viewset provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = TestEntry.objects.all()
    serializer_class = TestEntrySrz
    permission_classes = [IsAuthenticatedOrReadOnly]


class TestPostViewSet(ModelViewSet):
    """
    API for the TestEntry model.

    This viewset provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = TestPost.objects.all()
    serializer_class = TestPostSrz
    permission_classes = [IsAuthenticatedOrReadOnly]
