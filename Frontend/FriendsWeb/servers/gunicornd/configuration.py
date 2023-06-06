"""Gunicorn configurations."""
import json

from config import GUNICORN_CONFIG_FILE, PROXY_SOCKET


class GunicornMissingConfig(Exception):
    """Can't find the config file."""


if not GUNICORN_CONFIG_FILE.exists():
    raise GunicornMissingConfig()


with GUNICORN_CONFIG_FILE.open('r') as fl:
    GUNICORN_OPTIONS = json.load(fl)

GUNICORN_OPTIONS.update({'bind': f'unix:{PROXY_SOCKET}'})
