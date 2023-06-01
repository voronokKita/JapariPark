"""Process an absolute path to the Friends directory."""
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

base_dir_str = BASE_DIR.as_posix()
if base_dir_str not in sys.path:
    sys.path.insert(0, base_dir_str)


def get_path() -> Path:
    """
    Get a FriendsWeb path.

    :return: an absolute path to the manager.py folder
    """
    return BASE_DIR