"""Japari Park: Friends' router."""
from django.urls import path

from apps.friends import views


app_name = 'friends'

urlpatterns = [
    path('/ping', views.ping, name='friends-ping'),
]
