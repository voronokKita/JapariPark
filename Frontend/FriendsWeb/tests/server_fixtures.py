"""Test-servers and fixtures."""
import pytest
import time
import threading
import subprocess
from werkzeug.serving import make_server

from base_dir import MANAGER_WORKDIR
from config import WERKZEUG_TEST_PORT
from helpers.osdir import OSDIR
from friends.main import APPLICATION as app

from servers.nginxd import configuration
from servers.gunicornd.configuration import GUNICORN_OPTIONS


TEST_WERKZEUG_SERVER = make_server(
    host='0.0.0.0', port=WERKZEUG_TEST_PORT,
    app=app, processes=1,
    passthrough_errors=True,
)


class WerkzeugThread(threading.Thread):
    """A thread to easily manage Werkzeug start and stop."""

    server = TEST_WERKZEUG_SERVER

    def __int__(self):
        threading.Thread.__init__(self)

    def run(self):
        """Serve forever."""
        self.server.serve_forever()

    def merge(self):
        """Shutdown the server and join the thread."""
        self.server.shutdown()
        threading.Thread.join(self, 5)


@pytest.fixture(scope='session')
def werkzeug_server():
    """Run a server from a separate thread."""
    server = WerkzeugThread()
    server.start()
    time.sleep(0.2)
    yield True
    server.merge()


@pytest.fixture(scope='session')
def gunicorn_server():
    """Run a server from a subprocess."""
    command = ('python -m gunicorn friends.wsgi:app -w 1 --bind {BIND}'.
               format(BIND=GUNICORN_OPTIONS['bind']))
    gunicorn_process = subprocess.Popen(
        command.split(),
        cwd=MANAGER_WORKDIR.as_posix(),
        shell=False,
    )
    yield True
    gunicorn_process.terminate()


@pytest.fixture(scope='session')
def nginx_server():
    """Run a server from a subprocess."""
    subprocess.call(
        [OSDIR['sudo'], OSDIR['nginx']],
        cwd=MANAGER_WORKDIR.as_posix(),
        shell=False,
    )
    time.sleep(1)
    yield True
    subprocess.call(
        [OSDIR['sudo'], OSDIR['nginx'], '-s', 'quit'],
        cwd=MANAGER_WORKDIR.as_posix(),
        shell=False,
    )
