"""Process an absolute path to the FriendsWeb directory."""
import sys
from pathlib import Path


MANAGER_WORKDIR = Path(__file__).resolve().parents[2]

path = MANAGER_WORKDIR.as_posix()
if path not in sys.path:
    sys.path.insert(0, path)


def get_path() -> Path:
    """
    Get a FriendsWeb path.

    :return: an absolute path to the manager.py folder
    """
    return MANAGER_WORKDIR
