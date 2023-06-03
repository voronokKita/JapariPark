#!/usr/bin/env -S python -OO
"""Manager of the Japari Park: Friends Web."""
__author__ = 'Voronok Kita'
__copyright__ = 'Copyright (C) 2023 Voronok Kita'
__license__ = 'TODO'

import sys

import config
import friends
from helpers import base_dir
from helpers.context import CONTEXT
from tests import testrunner

BASE_DIR = base_dir.get_path()


if __name__ == '__main__':
    if CONTEXT.autotest:
        testrunner.run(CONTEXT.testpath)
    elif not CONTEXT.development:
        friends.main.run_gunicorn_server_with_nginx()

    if CONTEXT.dev_normal():
        friends.main.run_gunicorn_server_with_nginx()
    elif CONTEXT.dev_lite():
        friends.main.run_werkzeug_server()
    elif CONTEXT.dev_noproxy():
        friends.main.run_gunicorn_server()
    elif CONTEXT.dev_liteproxy():
        friends.main.run_werkzeug_server_with_nginx()


sys.exit(0)
