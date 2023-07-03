"""JapariService - views."""
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response as RestResponse
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
    ListAPIView, RetrieveAPIView,
)
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.core.models import TestEntry
from apps.core.serializers import ListEntrySrz, UserSrz
from apps.core.permissions import IsOwnerOrReadOnly


def ping(request: HttpRequest):
    """
    Ping-pong text.

    :returns: a plain text
    """
    return HttpResponse('JapariService: pong!')


@api_view(['GET', 'POST'])
def entry_list(request):
    """
    Serve API for the ListEntry model.

    List-read and create.
    Probably broken.
    :returns: RestResponse
    """
    if request.method == 'GET':
        entries = TestEntry.objects.all()
        serialized = ListEntrySrz(entries, many=True)
        return RestResponse(serialized.data)

    elif request.method == 'POST':
        serialized = ListEntrySrz(data=request.data)
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
    Serve API for the ListEntry model.

    Read, update, delete.
    Probably broken.
    :returns: RestResponse
    """
    try:
        entry = TestEntry.objects.get(pk=pk)
    except TestEntry.DoesNotExist:
        return RestResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized = ListEntrySrz(entry)
        return RestResponse(serialized.data)

    elif request.method == 'PUT':
        serialized = ListEntrySrz(entry, data=request.data)
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


class EntryListView(ListCreateAPIView):
    """
    APIv2 for the ListEntry model.

    List-read and create.
    """

    queryset = TestEntry.objects.all()
    serializer_class = ListEntrySrz
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """Associate the entry with the user."""
        serializer.save(owner=self.request.user)


class EntryDetailView(RetrieveUpdateDestroyAPIView):
    """
    APIv2 for the ListEntry model.

    Read, update, delete.
    """

    queryset = TestEntry.objects.all()
    serializer_class = ListEntrySrz
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class EntryViewSet(ModelViewSet):
    """
    APIv3 for the ListEntry model.

    This viewset provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = TestEntry.objects.all()
    serializer_class = ListEntrySrz
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """Associate the entry with the user."""
        serializer.save(owner=self.request.user)


class UserListView(ListAPIView):
    """
    API for the Users model.

    Read list.
    """

    queryset = User.objects.all()
    serializer_class = UserSrz
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserDetailView(RetrieveAPIView):
    """
    API for the Users model.

    Read by pk.
    """

    queryset = User.objects.all()
    serializer_class = UserSrz
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserViewSet(ReadOnlyModelViewSet):
    """
    APIv2 for the Users model.

    This viewset provides `list` and `retrieve` actions.
    """

    queryset = User.objects.all()
    serializer_class = UserSrz
