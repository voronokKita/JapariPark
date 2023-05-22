"""Frontend router."""

from flask_app.config import FLASK_APP


@FLASK_APP.route('/ping', methods=['GET'])
def ping():
    """
    Ping-pong.

    Returns:
        tuple[str,int]: plain text
    """
    return 'pong', 200
