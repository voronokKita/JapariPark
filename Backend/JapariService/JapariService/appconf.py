"""Presets for Django's applications."""
from collections import namedtuple

from JapariService.pathfinder import (
    COREAPP_DIR,
    ACCOUNTS_DIR,
    FRIENDS_DIR,
)


Appconfig = namedtuple(
    'Appconfig',
    field_names=('dir',),
)

APP_CONF = {
    'core': Appconfig(COREAPP_DIR),
    'accounts': Appconfig(ACCOUNTS_DIR),
    'friends': Appconfig(FRIENDS_DIR),
}

CONTRIB_APPS = (
    'admin', 'auth', 'contenttypes', 'sessions',
    'sites', 'flatpages', 'redirects', 'permissions',
)
