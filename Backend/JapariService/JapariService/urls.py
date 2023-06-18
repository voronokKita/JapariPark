"""URL configuration for JapariService."""
from django.contrib import admin
from django.urls import path, include

from helpers import istestrun

DEBUG = istestrun.check()


urlpatterns = [
    path('friends/', include('apps.friends.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('admin/', admin.site.urls),
]

if DEBUG:
    urlpatterns.append(
        path('__debug__/', include('debug_toolbar.urls')),
    )
