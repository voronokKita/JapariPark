"""Process command-line arguments into a context object."""
import sys
from pathlib import Path

from helpers import base_dir, command_args

BASE_DIR = base_dir.get_path()


class Context:
    """
    Context of the working program.

    This object should be used in any program logic
    to determine the operating conditions.

    The code of the program should support 3 basic contexts:

    - Automatic testing;
      Either through the testing pyramid, or by passing on specific tests.
    - Manual testing (development);
      With flexible settings for testing and debuggers.
    - Normal operation, for E2E testing or production;
      With the right settings.

    :ivar bool indocker: running in a container?
    :ivar bool autotest: running automated tests?
    :ivar Path or None testpath: an absolute path to tests
    :ivar bool development: running in dev. environment?
    :ivar bool gunicorn: serving through Gunicorn?
    :ivar bool nginx: proxying through NGINX?
    """

    __slots__ = (
        'indocker', 'autotest', 'testpath',
        'development', 'gunicorn', 'nginx',
    )

    def __init__(self):
        self._in_docker()

        if 'manage.py' not in sys.argv[0]:
            # if manage.py != __main__:
            # handle just like the automated tests
            self._context_auto_testing()
            return

        args = command_args.parse()
        if args.command == 'run':
            self._context_production()
        elif args.command == 'dev':
            self._context_development(args)
        elif args.command == 'test':
            self._context_auto_testing(args.path)

    def __str__(self):
        st = ('Context(indocker={A}, autotest={B}, testpath={C}, ' +
              'development={D}, gunicorn={E}, nginx={F})')
        return st.format(
            A=self.indocker, B=self.autotest, C=self.testpath,
            D=self.development, E=self.gunicorn, F=self.nginx,
        )

    def _in_docker(self):
        """Check out for a container flag."""
        self.indocker = Path(BASE_DIR, 'indocker').exists()

    def _context_production(self):
        """Working in a normal mode: Gunicorn + NGINX."""
        self.autotest = False
        self.testpath = None
        self.development = False
        self.gunicorn = True
        self.nginx = True

    def _context_development(self, options):
        """
        Working in a dev mod.

        options.lite == must serve through a small Werkzeug test-server

        options.noproxy == must serve through Gunicorn without NGINX

        without options == normal dev-mode, Gunicorn + NGINX

        :param options: argparse.Namespace(lite=bool, noproxy=bool)
        """
        self.autotest = False
        self.testpath = None
        self.development = True

        if options.lite:
            self.gunicorn = False
            self.nginx = False
        elif options.noproxy:
            self.gunicorn = True
            self.nginx = False
        else:
            self.gunicorn = True
            self.nginx = True

    def _context_auto_testing(self, path: str = ''):
        """
        Working in an auto-test mod.

        :param path: optional path to tests
        """
        self.autotest = True
        self.development = True
        self.gunicorn = False
        self.nginx = False

        if path != '' and path[0] == '/':
            self.testpath = Path(path).resolve()
        elif path != '' and path[:2] == './':
            self.testpath = Path(BASE_DIR, Path(path)).resolve()
        else:
            self.testpath = None


CONTEXT = Context()


def get_context() -> Context:
    """
    Return context of the program.

    :returns: a Context instance
    """
    return CONTEXT
