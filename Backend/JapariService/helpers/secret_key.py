"""Resolves Django's secret key."""
import sys
import secrets
from pathlib import Path

SECRET = Path('/run/secrets/django_secret').resolve()


def getkey() -> str:
    """
    Must get django secret key.

    If file not found - generate a random token.

    :return: string
    """
    if SECRET.exists():
        with SECRET.open('r') as fl:
            return fl.read().strip()
    else:
        if sys.stdout.isatty():
            print(
                "[ WARNING: Django's secret key not found on path `",
                SECRET.as_posix(),
                "`, a random token will be generated. ]",
                end='\n\n',
            )
        return secrets.token_urlsafe(50)
