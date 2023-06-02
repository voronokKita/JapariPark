#!/usr/bin/env -S python -OO
"""Manager of the Japari Park: Friends Web."""
__author__ = 'Voronok Kita'
__copyright__ = 'Copyright (C) 2023 Voronok Kita'
__license__ = 'TODO'

import sys

import friends
from helpers import base_dir
from helpers.context import get_context
from tests import testrunner

BASE_DIR = base_dir.get_path()


if __name__ == '__main__':
    context = get_context()
    if context.autotest:
        testrunner.run(context.testpath)
    elif not context.gunicorn:
        friends.main.run_werkzeug_server()
    elif context.gunicorn:
        friends.main.run_gunicorn_server()

sys.exit(0)
