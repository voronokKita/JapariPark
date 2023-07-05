"""Japari Park: Friends router."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.friends.views.demoviews import TestEntryViewSet, TestPostViewSet
from apps.friends.views import ping

app_name = 'friends'

viewset_router = DefaultRouter()
viewset_router.register('test-friends-entries',
                        TestEntryViewSet, basename='test-entry')
viewset_router.register('test-friends-posts',
                        TestPostViewSet, basename='test-post')

urlpatterns = [
    path('ping', ping, name='friends-ping'),

    path('api/', include(viewset_router.urls)),
]
