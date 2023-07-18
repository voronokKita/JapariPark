"""Entry points into the Friends application from the Web."""
from FriendsWeb.flask_init import APP
from FriendsWeb import views


@APP.route('/ping', methods=['GET'])
def ping():
    """
    Ping-pong lite.

    :returns: plain text, 200-OK
    """
    return 'FriendsWeb: pong!', 200


@APP.route('/ping-static', methods=['GET'])
def ping_static():
    """Ping-pong a normal html page with static content."""
    return views.ping_view(), 200


@APP.route('/ping-backend', methods=['GET'])
def ping_backend():
    """Ping-pong the backend service."""
    return views.ping_backend()
