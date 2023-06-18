"""Entry points into the Friends application from the Web."""
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
