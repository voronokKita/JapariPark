"""Presets for Django's applications."""
from collections import namedtuple

from JapariService.pathfinder import FRIENDS_DIR, ACCOUNTS_DIR


Appsconfig = namedtuple(
    'Appsconfig',
    field_names=('friends', 'accounts'),
)
APPS_CONF = Appsconfig(
    {
        'dir': FRIENDS_DIR,
    },
    {
        'dir': ACCOUNTS_DIR,
    },
)
