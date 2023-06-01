"""
To give the individual tests some context.

Must be imported in all the tests, in order to
make it possible to run them from any place.
"""
import sys
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parents[2]

dir_str = BASE_DIR.as_posix()
if dir_str not in sys.path:
    sys.path.insert(0, dir_str)
