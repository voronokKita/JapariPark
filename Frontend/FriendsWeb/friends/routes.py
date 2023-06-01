"""Japari Park: Friends Web - urls."""
from flask import render_template

from friends.config import APPLICATION as app


@app.route('/friends/ping', methods=['GET'])
def ping():
    """
    Ping-pong lite.

    :returns: tuple[str,int]: plain text, 200-OK
    """
    return 'pong', 200


@app.route('/friends/ping-html', methods=['GET'])
def ping_html():
    """
    Ping-pong.

    :returns: tuple[str,int]: the ping.html page, 200-OK
    """
    return render_template('ping.html'), 200
