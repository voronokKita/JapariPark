"""To give the individual tests some context."""
import sys
import pathlib


MANAGER_DIR = pathlib.Path(__file__).resolve().parents[1]

as_str = MANAGER_DIR.as_posix()
if as_str not in sys.path:
    sys.path.insert(0, as_str)
