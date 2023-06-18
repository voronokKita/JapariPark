"""JapariService - the core views."""
from django.http import HttpResponse, HttpRequest


def ping(request: HttpRequest) -> HttpResponse:
    """
    Ping-pong.

    :returns: a plain text
    """
    return HttpResponse('JapariService: pong!')
