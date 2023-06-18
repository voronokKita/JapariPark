"""Japari Park: Friends' router."""
from django.urls import path

from apps.friends import views


urlpatterns = [
    path('/ping', views.ping, name='friends ping'),
]
