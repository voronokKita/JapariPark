"""Japari Park: Friends - url router."""

from flask import render_template

from friends.config import APPLICATION


@APPLICATION.route('/friends/ping', methods=['GET'])
def ping():
    """
    Ping-pong.

    Returns:
        tuple[str,int]: plain text, 200-OK
    """
    return 'pong', 200


@APPLICATION.route('/friends/ping-html', methods=['GET'])
def ping_html():
    """
    Ping-pong.

    Returns:
        tuple[str,int]: the ping.html page, 200-OK
    """
    return render_template('ping.html'), 200
