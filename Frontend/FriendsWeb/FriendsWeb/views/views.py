"""Japari Park: Friends - web views."""
import requests
from flask import render_template

from FriendsWeb.settings import BACKEND_URL


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
        return str(err.args), 202

    if result.status_code == 200:
        return result.text, 200
    else:
        st = 'Error to ping the backend service: {err}'
        return st.format(err=result.status_code), 202
