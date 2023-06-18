"""Japari Park: Friends - http views."""
from django.http import HttpResponse, HttpRequest


def ping(request: HttpRequest) -> HttpResponse:
    """
    Ping-pong.

    :returns: a plain text
    """
    return HttpResponse('Friends Backend: pong!')
