"""Japari Park: Accounts - backend http views."""
from django.http import HttpResponse, HttpRequest


def ping(request: HttpRequest):
    """
    Ping-pong text.

    :returns: a plain text
    """
    return HttpResponse('Accounts Backend: pong!')
