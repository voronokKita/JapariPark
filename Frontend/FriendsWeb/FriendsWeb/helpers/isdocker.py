"""Recognizes a container context."""
from pathlib import Path
from FriendsWeb.pathfinder import BASE_DIR

INDOCKER = Path(BASE_DIR, 'indocker').exists()


def check() -> bool:
    """
    Check for a docker-mode.

    :returns: bool
    """
    return INDOCKER
