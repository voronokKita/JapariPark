"""URL configuration for JapariService."""
from django.contrib import admin
from django.urls import path, include

from JapariService.settings import DEBUG


urlpatterns = [
    path('', include('apps.core.urls', namespace='core')),

    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('friends/', include('apps.friends.urls', namespace='friends')),

    path('admin/', admin.site.urls),
]

if DEBUG:
    urlpatterns.insert(
        0, path('__debug__/', include('debug_toolbar.urls')),
    )
    urlpatterns.append(
        path('api-auth/', include('rest_framework.urls')),
    )
