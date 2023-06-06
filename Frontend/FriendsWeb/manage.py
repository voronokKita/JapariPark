#!/usr/bin/env -S python -OO
"""
Manager of the Japari Park: Friends Web.

In some cases it may ask for the user's password.
"""
__author__ = 'Voronok Kita'
__copyright__ = 'Copyright (C) 2023 Voronok Kita'
__license__ = 'TODO'

import sys

import base_dir
from helpers.context import CONTEXT

import config
from servers.gunicornd import configuration
from servers.nginxd.configuration import nginx_config_dir

from tests import testrunner

import friends


if __name__ == '__main__':
    if CONTEXT.in_production():
        friends.main.run_in_production()

    if CONTEXT.autotest:
        testrunner.run(CONTEXT.testpath)
    elif CONTEXT.dev_normal():
        friends.main.run_gunicorn_server_with_nginx()
    elif CONTEXT.dev_lite():
        friends.main.run_werkzeug_server()


sys.exit(0)
