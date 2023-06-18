"""URL configuration for JapariService."""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('friends/', include('apps.friends.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('admin/', admin.site.urls),
]
