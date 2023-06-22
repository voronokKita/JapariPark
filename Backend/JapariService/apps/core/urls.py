"""JapariService - the core router."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from apps.core.views import (
    UserListView, UserDetailView, UserViewSet,
    EntryListView, EntryDetailView, EntryViewSet,
    ping, entry_list, entry_detail,
)

app_name = 'core'

viewset_router = DefaultRouter()
viewset_router.register('users', UserViewSet, basename='user')
viewset_router.register('entries', EntryViewSet, basename='entry')


urlpatterns = [
    path('ping', ping, name='service-ping'),

    path('api/', include(viewset_router.urls)),

    # path('api/users/', UserListView.as_view(),
    #      name='user-list-old'),
    # path('api/users/<int:pk>/', UserDetailView.as_view(),
    #      name='user-detail-old'),
    #
    # path('api/entry-list', entry_list,
    #      name='entry-list-old'),
    # path('api/entry-list/<int:pk>', entry_detail,
    #      name='entry-detail-old'),

    # path('api/v2/entry-list', EntryListView.as_view(),
    #      name='entry-list'),
    # path('api/v2/entry-list/<int:pk>', EntryDetailView.as_view(),
    #      name='entry-detail'),
]
