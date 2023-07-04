"""JapariService - test core views."""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response as RestResponse
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.core.models import TestEntry
from apps.core.serializers import TestEntrySrz
from apps.core.permissions import IsOwnerOrReadOnly


class TestEntryViewSet(ModelViewSet):
    """
    APIv3 for the TestEntry model.

    This viewset provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = TestEntry.objects.all()
    serializer_class = TestEntrySrz
    permission_classes = [IsAuthenticatedOrReadOnly]


class EntryListView(ListCreateAPIView):
    """
    APIv2 for the TestEntry model.

    List-read and create.
    """

    queryset = TestEntry.objects.all()
    serializer_class = TestEntrySrz
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """Associate the entry with the user."""
        serializer.save(owner=self.request.user)


class EntryDetailView(RetrieveUpdateDestroyAPIView):
    """
    APIv2 for the TestEntry model.

    Read, update, delete.
    """

    queryset = TestEntry.objects.all()
    serializer_class = TestEntrySrz
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


@api_view(['GET', 'POST'])
def entry_list(request):
    """
    Serve APIv1 for the TestEntry model.

    List-read and create.
    Probably broken.
    :returns: RestResponse
    """
    if request.method == 'GET':
        entries = TestEntry.objects.all()
        serialized = TestEntrySrz(entries, many=True)
        return RestResponse(serialized.data)

    elif request.method == 'POST':
        serialized = TestEntrySrz(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return RestResponse(
                serialized.data, status=status.HTTP_201_CREATED,
            )
        else:
            return RestResponse(
                serialized.errors, status=status.HTTP_400_BAD_REQUEST,
            )


@api_view(['GET', 'PUT', 'DELETE'])
def entry_detail(request, pk):
    """
    Serve APIv1 for the TestEntry model.

    Read, update, delete.
    Probably broken.
    :returns: RestResponse
    """
    try:
        entry = TestEntry.objects.get(pk=pk)
    except TestEntry.DoesNotExist:
        return RestResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized = TestEntrySrz(entry)
        return RestResponse(serialized.data)

    elif request.method == 'PUT':
        serialized = TestEntrySrz(entry, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return RestResponse(serialized.data)
        else:
            return RestResponse(
                serialized.errors, status=status.HTTP_400_BAD_REQUEST,
            )

    elif request.method == 'DELETE':
        entry.delete()
        return RestResponse(status=status.HTTP_204_NO_CONTENT)
