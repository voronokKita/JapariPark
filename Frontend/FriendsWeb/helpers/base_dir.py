"""Process an absolute path to the Friends directory."""
import sys
from pathlib import Path


MANAGER_WORKDIR = Path(__file__).resolve().parents[1]

posix = MANAGER_WORKDIR.as_posix()
if posix not in sys.path:
    sys.path.insert(0, posix)


def get_path() -> Path:
    """
    Get a FriendsWeb path.

    :return: an absolute path to the manager.py folder
    """
    return MANAGER_WORKDIR
