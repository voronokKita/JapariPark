"""Must find absolute paths to some utilities and programs."""
import os
from pathlib import Path


class UtilNotFoundError(Exception):
    """Couldn't find a name."""


NAMES_TO_RESOLVE = (
    'sudo',
    'nginx',
    'ls',
    'chmod',
)

OSDIR = {}
environ_path = os.environ['PATH'].split(':')


for name in NAMES_TO_RESOLVE:
    for path in environ_path[::-1]:
        to_check = Path(path, name)
        if to_check.exists():
            OSDIR[name] = to_check.as_posix()
            break

    if name not in OSDIR:
        raise UtilNotFoundError()


def get_os_dirs():
    """Return dict with paths to programs."""
    return OSDIR
