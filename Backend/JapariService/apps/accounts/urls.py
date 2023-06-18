"""Japari Park: Accounts' router."""
from django.urls import path

from apps.accounts import views


urlpatterns = [
    path('/ping', views.ping, name='accounts ping'),
]
