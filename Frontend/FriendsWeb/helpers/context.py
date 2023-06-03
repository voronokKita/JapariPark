"""Process command-line arguments into a context object."""
import sys
from pathlib import Path

from helpers import base_dir, command_args

MANAGER_WORKDIR = base_dir.get_path()


class ContextError(Exception):
    """Error: context is changed."""


def in_dev_context(func):
    """Return False if not in a development env or in autotests."""
    def wrapper(self, *args, **kwargs):
        if self.development and not self.autotest:
            return func(self, *args, **kwargs)
        return False
    return wrapper


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
    :ivar Path manager_workdir: an absolute path to the manager.py folder
    :ivar Path flask_dir: an absolute path to the flask app folder
    :ivar Path gunicorn_dir: an absolute path to the server config folder
    :ivar Path nginx_dir: an absolute path to the proxy-server config folder
    """

    __slots__ = (
        'indocker', 'autotest', 'testpath',
        'development', 'gunicorn', 'nginx',
        'manager_workdir', 'flask_dir',
        'gunicorn_dir', 'nginx_dir',
    )

    def __init__(self):
        self._set_paths()
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

    @in_dev_context
    def dev_lite(self):
        """Return True if in a dev --lite env."""
        return not self.gunicorn and not self.nginx

    @in_dev_context
    def dev_noproxy(self):
        """Return True if in a dev --noproxy env."""
        return self.gunicorn and not self.nginx

    @in_dev_context
    def dev_liteproxy(self):
        """Return True if in a dev --liteproxy env."""
        return self.nginx and not self.gunicorn

    @in_dev_context
    def dev_normal(self):
        """Return True if in a dev env."""
        return self.gunicorn and self.nginx

    def _set_paths(self):
        self.manager_workdir = MANAGER_WORKDIR
        self.flask_dir = MANAGER_WORKDIR / 'friends'
        self.gunicorn_dir = MANAGER_WORKDIR / 'servers' / 'gunicornd'
        self.nginx_dir = MANAGER_WORKDIR / 'servers' / 'nginxd'

        if not all((
            self.manager_workdir.exists(),
            self.flask_dir.exists(),
            self.gunicorn_dir.exists(),
            self.nginx_dir.exists(),
        )):
            raise ContextError('ERROR: paths are changed')

    def _in_docker(self):
        """Check out for a container flag."""
        self.indocker = Path(self.manager_workdir, 'indocker').exists()

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

        options.liteproxy == must serve through Werkzeug with NGINX

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
        elif options.liteproxy:
            self.gunicorn = False
            self.nginx = True
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
            self.testpath = Path(self.manager_workdir, Path(path)).resolve()
        else:
            self.testpath = None


CONTEXT = Context()


def get_context() -> Context:
    """
    Return context of the program.

    :returns: a Context instance
    """
    return CONTEXT
