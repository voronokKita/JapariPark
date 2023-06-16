#!/usr/bin/env -S python -OO
"""Manager of the Japari Park: Friends Web."""
import sys
from pathlib import Path

base_dir = Path(__file__).resolve().parent.as_posix()
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)


if __name__ == '__main__':
    from helpers.context import CONTEXT
    from tests import testrunner
    from friends import main

    if CONTEXT.autotest:
        testrunner.run(CONTEXT.testpath)
    elif CONTEXT.dev_lite():
        main.run_werkzeug_server()
    else:
        main.run_gunicorn_server()


sys.exit(0)
