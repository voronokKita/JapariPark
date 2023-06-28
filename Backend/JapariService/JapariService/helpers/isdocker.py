"""Recognizes a container context."""
from JapariService.pathfinder import BASE_DIR

flag = BASE_DIR / 'indocker'
INDOCKER = flag.exists()


def check() -> bool:
    """
    Check for a docker-mode.

    :returns: bool
    """
    return INDOCKER
