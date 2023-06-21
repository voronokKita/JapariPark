"""JapariService - the core router."""
from django.urls import path

from apps.core.views import (
    UserListView, UserDetailView,
    EntryListView, EntryDetailView,
    ping, entry_list, entry_detail,
)

app_name = 'core'


urlpatterns = [
    path('ping', ping, name='service-ping'),

    path(
        'api/users/',
        UserListView.as_view(),
        name='users-api',
    ),
    path(
        'api/users/<int:pk>',
        UserDetailView.as_view(),
        name='user-get-api',
    ),
    path(
        'api/entry-list',
        entry_list,
        name='entry-list-api',
    ),
    path(
        'api/entry-list/<int:pk>',
        entry_detail,
        name='entry-detail-api',
    ),
    path(
        'api/v2/entry-list',
        EntryListView.as_view(),
        name='entry-list-api2',
    ),
    path(
        'api/v2/entry-list/<int:pk>',
        EntryDetailView.as_view(),
        name='entry-detail-api2',
    ),
]
