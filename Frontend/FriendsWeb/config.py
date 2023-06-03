"""Base application and server configurations."""
import sys
import pathlib

from helpers.context import CONTEXT

BASE_IP = '0.0.0.0'
BASE_DOMAIN = 'localhost'
BASE_PORT = 5000

# For the final address
HOST_IP = '127.0.0.1'
HOST_DOMAIN = 'localhost'
SITE_PORT = 5050


MANAGER_WORKDIR = pathlib.Path(__file__).resolve()
posix = MANAGER_WORKDIR.as_posix()
if posix not in sys.path:
    sys.path.insert(0, posix)


# Gunicorn options
GUNICORN_OPTIONS = {
    'workers': 2,
    'timeout': 1,
}
if CONTEXT.dev_normal():
    bind = ('unix:{P}/friends.sock'.
            format(P=CONTEXT.gunicorn_dir.as_posix()))
    GUNICORN_OPTIONS.update({'bind': bind})
else:
    GUNICORN_OPTIONS.update({'bind': f'{BASE_IP}:{BASE_PORT}'})
