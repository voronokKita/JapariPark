"""JapariService - the core router."""
from django.urls import path

from apps.core import views


urlpatterns = [
    path('ping', views.ping, name='service ping'),
]
