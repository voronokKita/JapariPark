"""
Japari Park: Friends Web - main root.

The Flask APPLICATION instance must be used from here,
for all settings to work through import.
"""
import subprocess

from base_dir import MANAGER_WORKDIR
from config import WERKZEUG_TEST_PORT

from servers.gunicornd.wrapper import GunicornWrapper

from friends import constants, routes
from friends.config import APPLICATION


def run_in_production():
    """Run in a production environment."""
    pass


def run_werkzeug_server():
    """Run a Werkzeug mini-server through a Flask runner."""
    APPLICATION.run(host='0.0.0.0', port=WERKZEUG_TEST_PORT)


def run_gunicorn_server_with_nginx():
    """Run a normal server through a proxy."""
    subprocess.call(
        ['/usr/bin/sudo', '/usr/sbin/nginx'],
        cwd=MANAGER_WORKDIR.as_posix(), shell=False,
    )
    try:
        GunicornWrapper(app=APPLICATION).run()
    except (KeyboardInterrupt, Exception):
        pass
    finally:
        subprocess.call(
            ['/usr/bin/sudo', '/usr/sbin/nginx', '-s', 'quit'],
            cwd=MANAGER_WORKDIR.as_posix(), shell=False,
        )
