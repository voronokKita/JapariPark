"""URL configuration for JapariService."""
from django.contrib import admin
from django.urls import path, include

from helpers import istestrun

DEBUG = istestrun.check()


urlpatterns = [
    path('', include('apps.core.urls', namespace='core')),

    path('accounts', include('apps.accounts.urls', namespace='accounts')),
    path('friends', include('apps.friends.urls', namespace='friends')),

    path('admin/', admin.site.urls),
]

if DEBUG:
    urlpatterns.insert(
        0, path('__debug__/', include('debug_toolbar.urls')),
    )
