"""Resolve Flask's secret key."""
import secrets

from FriendsWeb.pathfinder import SECRETS_DIR, BASE_DIR
from FriendsWeb.helpers import printer, isdocker


if isdocker.check():
    SECRET = SECRETS_DIR / 'flask_secret'
else:
    SECRET = BASE_DIR / 'secrets' / '.flask.secret'


def getkey() -> str:
    """
    Must get flask's secret key.

    If file not found - generate a random token.

    :return: string
    """
    if SECRET.exists():
        with SECRET.open('r') as fl:
            return fl.read().strip()

    msg = (
        "[ WARNING: Flask's secret key not found on path `" +
        SECRET.as_posix() +
        "`, a random token will be generated. ]"
    )
    printer.write(msg)
    return secrets.token_urlsafe(50)
