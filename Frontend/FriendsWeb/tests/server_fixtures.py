"""Test-servers and fixtures."""
import pytest
import time
import threading
import subprocess
from werkzeug.serving import make_server, BaseWSGIServer

from tests.context import BASE_DIR
from FriendsWeb.settings import TESTPORT
from FriendsWeb.helpers import in_github_ci
from FriendsWeb.main import APP


def get_werkzeug_server():
    """Return BaseWSGIServer."""
    return make_server(
        host='::', port=TESTPORT,
        app=APP, processes=1,
        passthrough_errors=True,
    )


class WerkzeugThread(threading.Thread):
    """A thread to easily manage Werkzeug start and stop."""

    def __int__(self):
        threading.Thread.__init__(self)
        self.server = None

    def run(self):
        """Start serving."""
        self.server = get_werkzeug_server()
        self.server.serve_forever()

    def merge(self):
        """Shutdown the server and join the thread."""
        self.server.shutdown()
        threading.Thread.join(self, 5)


# !Deprecated
# @pytest.fixture(scope='session')
def werkzeug_server():
    """
    Run a server from a separate thread.

    Skip if in a GitHub workflow.
    """
    if in_github_ci.check():
        yield True
    else:
        server = WerkzeugThread()
        server.start()
        time.sleep(0.5)
        yield True
        server.merge()


@pytest.fixture(scope='session')
def gunicorn_server():
    """
    Run a server from a subprocess.

    Skip if in a GitHub workflow.
    """
    if in_github_ci.check():
        yield True
    else:
        bind = f'[::]:{TESTPORT}'
        command = f'python -m gunicorn FriendsWeb.wsgi:app -w 2 --bind {bind}'
        gunicorn_process = subprocess.Popen(
            command.split(),
            cwd=BASE_DIR.as_posix(),
            shell=False,
        )
        time.sleep(0.6)

        yield True
        gunicorn_process.terminate()
