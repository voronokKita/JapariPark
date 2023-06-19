"""
Runs the specified tests.

My attempt to build flexible testing system that wraps around pytest.

Testing pyramid:
  0. Base tests - resources and environment check.
  1. Unit tests - atomised functions.
  2. Function tests (integration) - the ability to do certain tasks.
  3. Serving tests - communications and accessibility,
     the ability of the system to process requests.
  4. Manual tests - with test-settings and debuggers.
  5. Manual E2E test - with production environment.
"""
import os
import sys
import subprocess
from pathlib import Path

from tests.context import BASE_DIR
from helpers.context import CONTEXT

NO_TEST_FOUND_EXIT_CODE = 5


def get_pyramid() -> tuple:
    """Construct the testing pyramid."""
    tests_dir = BASE_DIR / 'tests'
    return (
        {'name': 'BASE', 'path': tests_dir / 'base'},
        {'name': 'UNITS', 'path': tests_dir / 'units'},
        {'name': 'FUNCTIONAL', 'path': tests_dir / 'functional'},
        {'name': 'SERVING', 'path': tests_dir / 'serving'},
    )


def run_path(path: Path):
    """
    Run 'pytest path'.

    Will make a call to `sys.exit()` if test returns an error.

    :param path: a path to test
    """
    cmd = [
        sys.executable, '-m',
        'pytest', '-v',
        path.as_posix(),
        '-W', 'ignore::DeprecationWarning',
    ]
    result = subprocess.run(cmd, shell=False, cwd=BASE_DIR.as_posix())
    if 0 < result.returncode < NO_TEST_FOUND_EXIT_CODE:
        sys.exit(result.returncode)


def run(path: Path = None):
    """
    Run tests.

    Normally, should run tests in groups, folder by folder,
    from `base` up to `serving`.
    If a **path** is given, run tests only on that path.

    :param path: a path to give to pytest
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
        if CONTEXT.in_github_ci and layer['name'] == 'SERVING':
            continue

        if terminal:
            print()
            print(f'[[ TESTING LAYER {layer["name"]} ]]'.center(tsize.columns))

        run_path(layer['path'])
