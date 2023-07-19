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
from FriendsWeb.pathfinder import TEMPLATES_DIR

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
        'bind': f'0.0.0.0:{TESTPORT}',
        'workers': 2,
        'reload': True,
        'reload_extra_files': [TEMPLATES_DIR.as_posix()],
        'preload_app': False,
        'daemon': False,
        'timeout': 10,
        'graceful_timeout': 5,
        'keepalive': 5,
        'accesslog': '-',
        'errorlog': '-',
        'loglevel': 'info',
        'access_log_format': '%(t)s: %(m)s %(U)s %(s)s - %(h)s %(a)s',
    }
    try:
        GunicornWrapper(app=APP, options=options).run()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        raise err
