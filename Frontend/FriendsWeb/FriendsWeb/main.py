"""
Japari Park: Friends Web - the root file.

The Flask APPLICATION instance must be used from here,
for all the settings to work through imports.

Includes a set of functions to run various
application configurations manually;
intended for testing.
"""
from FriendsWeb.urls import APP

from FriendsWeb.helpers import printer
from FriendsWeb.helpers.gunicorn_wrapper import GunicornWrapper
from FriendsWeb.settings import TESTPORT, DEBUG

if DEBUG:
    printer.write('[Running in a debug mode]')


def print_warning(func):
    """Warn about potential risks."""
    def wrapper(*args, **kwargs):
        wrn = ("[WARNING: Don't use this start method in a production, " +
               "- use the WSGI interface]\n")
        printer.write(wrn)
        return func(*args, **kwargs)
    return wrapper


@print_warning
def run_werkzeug_server():
    """Run a Werkzeug mini-server through a Flask runner."""
    APP.run(
        host='::', port=TESTPORT,
        debug=True, load_dotenv=False,
    )


@print_warning
def run_gunicorn_server():
    """Run a normal server."""
    options = {
        'bind': f'[::]:{TESTPORT}',
        'workers': 2, 'timeout': 1,
    }
    try:
        GunicornWrapper(app=APP, options=options).run()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        raise err
