#!/usr/bin/env python
"""Manager of the Japari Park: Friends Web."""
import sys
from pathlib import Path

BASEDIR = Path(__file__).resolve().parent
if BASEDIR.as_posix() not in sys.path:
    sys.path.insert(0, BASEDIR.as_posix())


if __name__ == '__main__':
    import manager
    from FriendsWeb import main
    from tests import testrunner

    args = manager.command_line.parse()
    if args.command == 'test':
        testrunner.run(
            manager.command_line.get_test_path(BASEDIR, args.path),
        )
    elif args.command == 'runserver':
        main.run_gunicorn_server()


sys.exit(0)
