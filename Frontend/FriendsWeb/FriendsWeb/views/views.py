"""Japari Park: Friends - web views."""
import requests
from flask import render_template, send_from_directory, abort

from FriendsWeb.pathfinder import STATIC_DIR
from FriendsWeb.settings import BACKEND_URL, SERV_STATIC

# TODO exceptions (TemplateNotFound, etc)


def ping_view() -> tuple[str, int]:
    """
    Return rendered html page with static content for testing.

    :returns: the ping.html page, 200-OK
    """
    return render_template('ping.html'), 200


def ping_backend():
    """
    Ping the Friends backend end return the response with statuscode.

    :returns: tuple[response, status]
    """
    try:
        result = requests.get(f'{BACKEND_URL}/ping', timeout=5)
    except Exception as err:
        abort(503)
    else:
        if result.status_code == 200:
            return result.text, 200
        else:
            st = 'Error to ping the backend service: {err}'
            return st.format(err=result.status_code), 500


def serv_favicon():
    """
    Process requests to base favicon.

    :return: an ico file or 404
    """
    if not SERV_STATIC:
        abort(404)

    return send_from_directory(
        STATIC_DIR, 'images/favicon.ico',
        mimetype='image/vnd.microsoft.icon',
    ), 200
