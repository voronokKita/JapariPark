"""Entry points into the Friends application from the Web."""
from FriendsWeb import views

"""
string- accepts any text without a slash (the default)
path- like the default but also accepts slashes
float- like int but for floating point values
any- matches one of the items provided
uuid- accepts UUID strings
"""

# TODO
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

router = (
    {
        'rule': '/ping', 'methods': ['GET'],
        'view_func': views.ping_view,
    },
    {
        'rule': '/ping-static', 'methods': ['GET'],
        'view_func': views.ping_static_view,
    },
    {
        'rule': '/ping-backend', 'methods': ['GET'],
        'view_func': views.ping_backend,
    },
    {
        'rule': '/favicon.ico', 'methods': ['GET'],
        'view_func': views.serv_favicon,
    },
)
