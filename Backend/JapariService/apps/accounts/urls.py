"""Japari Park: Accounts' router."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.accounts.views.demoviews import TestEntryViewSet
from apps.accounts.views import ping

app_name = 'accounts'


viewset_router = DefaultRouter()
viewset_router.register('test-accounts-entries',
                        TestEntryViewSet, basename='test-entry')

urlpatterns = [
    path('ping', ping, name='accounts-ping'),

    path('api/', include(viewset_router.urls)),
]
