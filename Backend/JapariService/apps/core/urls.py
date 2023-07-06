"""JapariService - the core router."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.core.views.demoviews import TestEntryViewSet
from apps.core.views import ping

app_name = 'core'

viewset_router = DefaultRouter()
viewset_router.register('test-core-entries',
                        TestEntryViewSet, basename='test-entry')

urlpatterns = [
    path('ping', ping, name='service-ping'),

    path('api/', include(viewset_router.urls)),
]
