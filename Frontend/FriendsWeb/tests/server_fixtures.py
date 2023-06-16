"""Test-servers and fixtures."""
import pytest
import time
import threading
import subprocess
from werkzeug.serving import make_server

from tests.context import BASE_DIR
from helpers.context import CONTEXT
from friends.settings import SITE_PORT, WERKZEUG_TESTPORT
from friends.main import APP


TEST_WERKZEUG_SERVER = make_server(
    host='0.0.0.0', port=WERKZEUG_TESTPORT,
    app=APP, processes=1,
    passthrough_errors=True,
)


class WerkzeugThread(threading.Thread):
    """A thread to easily manage Werkzeug start and stop."""

    server = TEST_WERKZEUG_SERVER

    def __int__(self):
        threading.Thread.__init__(self)

    def run(self):
        """Start serving."""
        self.server.serve_forever()

    def merge(self):
        """Shutdown the server and join the thread."""
        self.server.shutdown()
        threading.Thread.join(self, 5)


@pytest.fixture(scope='session')
def werkzeug_server():
    """Run a server from a separate thread."""
    if CONTEXT.in_github_ci:
        yield True
    else:
        server = WerkzeugThread()
        server.start()
        time.sleep(0.2)
        yield True
        server.merge()


@pytest.fixture(scope='session')
def gunicorn_server():
    """Run a server from a subprocess."""
    if CONTEXT.in_github_ci:
        yield True
    else:
        bind = f'0.0.0.0:{SITE_PORT}'
        command = f'python -m gunicorn friends.wsgi:app -w 2 --bind {bind}'
        gunicorn_process = subprocess.Popen(
            command.split(),
            cwd=BASE_DIR.as_posix(),
            shell=False,
        )
        time.sleep(0.2)
        yield True
        gunicorn_process.terminate()
