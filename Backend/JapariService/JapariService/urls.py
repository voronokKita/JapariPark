"""URL configuration for JapariService."""
from django.contrib import admin
from django.urls import path, include

from JapariService.settings import DEBUG


urlpatterns = [
    path('friends/', include('apps.friends.urls', namespace='friends')),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='api-auth')),

    path('', include('apps.core.urls', namespace='core')),
]

if DEBUG:
    urlpatterns.insert(
        0, path('__debug__/', include('debug_toolbar.urls', 'debug')),
    )
