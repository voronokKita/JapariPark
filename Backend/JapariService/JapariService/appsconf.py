"""Presets for Django's applications."""
from collections import namedtuple

from JapariService.pathfinder import (
    COREAPP_DIR,
    ACCOUNTS_DIR,
    FRIENDS_DIR,
)


Appsconfig = namedtuple(
    'Appsconfig',
    field_names=('core', 'accounts', 'friends'),
)
APPS_CONF = Appsconfig(
    {
        'dir': COREAPP_DIR,
    },
    {
        'dir': ACCOUNTS_DIR,
    },
    {
        'dir': FRIENDS_DIR,
    },
)
