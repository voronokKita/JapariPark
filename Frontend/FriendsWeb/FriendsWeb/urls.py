"""Entry points into the Friends application from the Web."""
from FriendsWeb.flask_init import APP
from FriendsWeb import views

""" TODO
add_url_rule(rule, endpoint=None, view_func=None,
             provide_automatic_options=None, **options)
app.add_url_rule("/", view_func=index)

string accepts any text without a slash (the default)
int accepts integers
float like int but for floating point values
path like the default but also accepts slashes
any matches one of the items provided
uuid accepts UUID strings
"""

URL_SET = {
    # testing
    '/ping',
    '/ping-static',
    '/ping-backend',
    '/index/',

    # static
    '/favicon.ico',

    # redirect to the accounts app
    '/users/',
    '/users/<int>',
    '/users/<slug>',

    # main
    '/',
    '/<int:user-page>',
    '/<slug:user-page>',
    '/<slug>/posts/',
    '/<slug>/posts/<int>',
}


@APP.route('/ping', methods=['GET'])
def ping():
    """Ping-pong lite."""
    return 'FriendsWeb: pong!', 200


@APP.route('/ping-static', methods=['GET'])
def ping_static():
    """Ping-pong a normal html page with static content."""
    return views.ping_view()


@APP.route('/ping-backend', methods=['GET'])
def ping_backend():
    """Ping-pong the backend service."""
    return views.ping_backend()


@APP.route('/index/', methods=['GET'])
def index():
    """
    Index page.

    TODO
    """
    return 'TODO', 200


@APP.route('/favicon.ico', methods=['GET'])
def favicon():
    """Return default favicon."""
    return views.serv_favicon()


@APP.route('/users/', methods=['GET'])
def users():
    """
    Accounts management.

    TODO
    """
    return 'TODO', 200


@APP.route('/', methods=['GET'])
def root():
    """
    Process main title page.

    TODO
    """
    return 'TODO', 200
