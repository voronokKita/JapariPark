"""Resolves Django's secret key."""
import secrets

from JapariService.pathfinder import SECRETS_DIR
from JapariService.helpers import printer

SECRET = SECRETS_DIR / 'django_secret'


def getkey() -> str:
    """
    Must get django's secret key.

    If file not found - generate a random token.

    :return: string
    """
    if SECRET.exists():
        with SECRET.open('r') as fl:
            return fl.read().strip()
    else:
        msg = (
            "[ WARNING: Django's secret key not found on path `" +
            SECRET.as_posix() +
            "`, a random token will be generated. ]"
        )
        printer.write(msg)
        return secrets.token_urlsafe(50)
