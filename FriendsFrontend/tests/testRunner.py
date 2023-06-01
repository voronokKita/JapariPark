"""
Runs the specified tests.

My attempt to build flexible testing system that wraps around pytest.

Testing pyramid:
          5. Manual E2E test - with production environment  .\
        4. Manual tests - with test-settings and debuggers    .\
      3. Function tests (integration) - the ability of          .\
         the system to process requests and do certain tasks     .
    2. Serving tests - communications and accessibility           .\
  1. Unit tests - atomised functions                                .\
0. Base tests - resources and environment check                       .\
"""
import sys
import subprocess
from pathlib import Path

from helpers import base_dir

NO_TESTS_CODE = 5


def get_pyramid() -> tuple:
    """Construct the testing pyramid."""
    tests_dir = base_dir.get_path() / 'tests'
    return (
        {'name': 'BASE', 'path': tests_dir / 'base'},
        {'name': 'UNITS', 'path': tests_dir / 'units'},
        {'name': 'SERVING', 'path': tests_dir / 'serving'},
        {'name': 'FUNCTIONAL', 'path': tests_dir / 'functional'},
    )


def run_path(path: Path):
    """
    Run 'pytest path'.

    Will make a call to `sys.exit()` if test returns an error.

    :param path: a path to test
    """
    result = subprocess.run([sys.executable, '-m', 'pytest', path.as_posix()])
    if result.returncode != 0:
        sys.exit(result.returncode)


def run(path: Path = None, max_layer='functional'):
    """
    Run tests.

    If a **path** is given, test only on that path.

    Normally, should run tests in groups, folder by folder,
    from `base` up to `functional`.

    Can specify another **max_layer** to stop.

    Will make a call to `sys.exit()` if some test returns an error.

    :param path: a path to give to the pytest
    :param max_layer: a layer of the testing pyramid to stop
    """
    if path:
        run_path(path)
        return

    for layer in get_pyramid():
        print(f'[TEST LAYER {layer["name"]}]')
        result = subprocess.run(
            [sys.executable, '-m', 'pytest', layer['path'].as_posix()]
        )

        if result.returncode == NO_TESTS_CODE:
            pass
        elif result.returncode != 0:
            sys.exit(result.returncode)

        if layer['name'] == max_layer:
            break
