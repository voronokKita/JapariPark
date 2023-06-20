"""Entry points into the Friends application from the Web."""
import requests
from flask import render_template

from friends.flask_init import APP
from friends import views


@APP.route('/ping', methods=['GET'])
def ping():
    """
    Ping-pong lite.

    :returns: tuple[str,int]: plain text, 200-OK
    """
    return 'FriendsWeb: pong!', 200


@APP.route('/ping-html', methods=['GET'])
def ping_html():
    """
    Ping-pong.

    :returns: tuple[str,int]: the ping.html page, 200-OK
    """
    return render_template('ping.html'), 200


@APP.route('/ping-backend', methods=['GET'])
def ping_backend():
    """
    Ping-pong the backend service.

    :returns: tuple[str,int]: responce, 200-OK
    """
    result = requests.get('http://japari-service.rest/ping', timeout=20)
    if result.status_code == 200:
        return result.text
    else:
        st = 'Error to ping the backend service: {err}'
        return st.format(err=result.status_code)
