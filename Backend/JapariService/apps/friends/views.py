"""Japari Friends - views."""
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def ping(request: HttpRequest) -> HttpResponse:
    """
    Ping-pong.

    :returns: a plain text
    """
    return HttpResponse('pong')
