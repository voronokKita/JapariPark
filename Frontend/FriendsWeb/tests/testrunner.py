"""
Runs the specified tests.

My attempt to build flexible testing system that wraps around pytest.

Testing pyramid:
  0. Base tests - resources and environment check.
  1. Unit tests - atomised functions.
  2. Serving tests - communications and accessibility.
  3. Function tests (integration) - the ability of the system
     to process requests and do certain tasks.
  4. Manual tests - with test-settings and debuggers.
  5. Manual E2E test - with production environment.

"""
import os
import sys
import subprocess
from pathlib import Path

import base_dir

BASE_DIR = base_dir.get_path()
NO_TESTS_EXIT_CODE = 5


def get_pyramid() -> tuple:
    """Construct the testing pyramid."""
    tests_dir = BASE_DIR / 'tests'
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
    process = subprocess.run(
        [sys.executable, '-m', 'pytest', path.as_posix()],
        shell=False, cwd=BASE_DIR.as_posix(),
    )
    if 0 < process.returncode < NO_TESTS_EXIT_CODE:
        sys.exit(process.returncode)


def run(path: Path = None, max_layer='functional'):
    """
    Run tests.

    If a **path** is given, run tests only on that path.

    Normally, should run tests in groups, folder by folder,
    from `base` up to `functional`.

    Can specify another **max_layer** to stop.

    :param path: a path to give to pytest
    :param max_layer: a layer of the testing pyramid to stop
    """
    if path:
        run_path(path)
        return

    terminal = False
    tsize = None
    if sys.stdout.isatty():
        terminal = True
        tsize = os.get_terminal_size()

    for layer in get_pyramid():
        if terminal:
            print()
            print(f'[[ TESTING LAYER {layer["name"]} ]]'.center(tsize.columns))

        run_path(layer['path'])
        if layer['name'] == max_layer:
            break
