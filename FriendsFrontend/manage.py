#!/usr/bin/env -S python -O
"""Manager of the Japari Park: Friends Frontend."""
__author__ = 'Voronok Kita'
__copyright__ = 'Copyright (C) 2023 Voronok Kita'
__license__ = 'TODO'

import friends
from helpers import base_dir
from helpers import context

BASE_DIR = base_dir.get_path()


if __name__ == '__main__':
    context = context.get_context()
    if not context.gunicorn:
        friends.main.run_werkzeug_server()
