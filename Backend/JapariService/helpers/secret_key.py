"""Resolves Django's secret key."""
import sys
import secrets
from pathlib import Path


def getkey() -> str:
    """
    Must get django secret key.

    If file not found - generate a random token.

    :return: string
    """
    base_dir = Path(__file__).resolve().parents[1]
    secret_key = base_dir / 'secrets' / '.django.secret'

    if secret_key.exists():
        with secret_key.open('r') as fl:
            return fl.read().strip()
    else:
        if sys.stdout.isatty():
            print(
                "[ WARNING: Django's secret key not found on path `",
                secret_key.as_posix(),
                "`, a random token will be generated ]",
                end='\n\n',
            )
        return secrets.token_urlsafe(50)
