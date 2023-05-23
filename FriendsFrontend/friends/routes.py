"""Japari Park: Friends - url router."""

from friends.config import FLASK


@FLASK.route('/friends/ping', methods=['GET'])
def ping():
    """
    Ping-pong.

    Returns:
        tuple[str,int]: plain text
    """
    return 'pong', 200
