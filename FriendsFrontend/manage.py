#!/usr/bin/env -S python -O
"""
Manager of the Japari Park: Friends frontend.

TODO normal argument parser
"""
__author__ = 'Voronok Kita'
__copyright__ = 'Copyright (C) 2023 Voronok Kita'
__license__ = 'TODO'
__version__ = 'dev'

import friends
import helpers

BASE_DIR = helpers.base_dir.get_path()


if __name__ == '__main__':
    context = helpers.context.get_context()
    if context.werkzeug:
        friends.main.run_werkzeug_server()
