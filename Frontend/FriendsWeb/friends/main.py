"""
Japari Park: Friends Web - the root file.

The Flask APPLICATION instance must be used from here,
for all the settings to work through imports.

Includes a set of functions to run various
application configurations manually;
intended for testing.
"""
import sys

from friends.urls import APP

from friends.gunicorn_wrapper import GunicornWrapper
from friends.settings import GUNICORN_TESTPORT, WERKZEUG_TESTPORT


def print_warning(func):
    """Warn about potential risks."""
    def wrapper(*args, **kwargs):
        if sys.stdout.isatty():
            wrn = ("[WARNING: Don't use this start method in a production, " +
                   "- use the WSGI interface]")
            print(wrn, end='\n\n')
        return func(*args, **kwargs)
    return wrapper


@print_warning
def run_werkzeug_server():
    """Run a Werkzeug mini-server through a Flask runner."""
    APP.run(
        host='::', port=WERKZEUG_TESTPORT,
        debug=True, load_dotenv=False,
    )


@print_warning
def run_gunicorn_server():
    """Run a normal server."""
    options = {
        'bind': f'[::]:{GUNICORN_TESTPORT}',
        'workers': 2, 'timeout': 1,
    }
    try:
        GunicornWrapper(app=APP, options=options).run()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        raise err
