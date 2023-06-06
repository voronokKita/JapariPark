"""Process command-line arguments into a context object."""
import os
import sys
from pathlib import Path

from base_dir import MANAGER_WORKDIR
from helpers import command_args


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
    :ivar bool in_github_ci: running in a GitHub container?
    :ivar bool autotest: running automated tests?
    :ivar Path | None testpath: an absolute path to tests
    :ivar bool development: running in dev. environment?
    :ivar bool gunicorn: serving through Gunicorn?
    :ivar bool nginx: proxying through NGINX?
    :ivar Path manager_workdir: an absolute path to the manager.py folder
    :ivar Path flask_dir: an absolute path to the flask app folder
    :ivar Path servers_dir: an absolute path to the servers module
    """

    __slots__ = (
        'indocker', 'in_github_ci',
        'autotest', 'testpath',
        'development', 'gunicorn', 'nginx',
        'manager_workdir', 'flask_dir', 'servers_dir',
    )

    def __init__(self):
        self._set_paths()
        self._in_docker()
        self._in_github_workflow()

        if 'manage.py' not in sys.argv[0]:
            # if manage.py != __main__:
            # handle just like the automated tests
            self._context_auto_testing()
            return

        args = command_args.parse()
        if args.command == 'run':
            self._context_production()
        elif args.command == 'dev':
            self._context_development(options=args)
        elif args.command == 'test':
            self._context_auto_testing(path=args.path)

    def __str__(self):
        if self.in_production():
            return 'Context(production)'
        elif self.autotest:
            return 'Context(auto-tests)'
        elif self.dev_lite(self):
            return 'Context(dev werkzeug)'
        else:
            return 'Context(dev gunicorn + nginx)'

    def __repr__(self):
        st = ('Context(indocker={D}, in_github_ci={CI}, ' +
              'autotest={AT}, development={DEV}, ' +
              'gunicorn={GU}, nginx={NX}, ' +
              'workdir={CWD})')
        return st.format(
            D=self.indocker,
            CI=self.in_github_ci,
            AT=self.autotest,
            DEV=self.development,
            GU=self.gunicorn,
            NX=self.nginx,
            CWD=self.manager_workdir.as_posix(),
        )

    def in_production(self):
        """Return True if not in development and not autotests."""
        return not self.autotest and not self.development

    @in_dev_context
    def dev_normal(self):
        """Return True if in a normal dev env."""
        return self.gunicorn and self.nginx

    @in_dev_context
    def dev_lite(self):
        """Return True if in a dev --lite env."""
        return not self.gunicorn and not self.nginx

    def _set_paths(self):
        self.manager_workdir = MANAGER_WORKDIR
        self.flask_dir = MANAGER_WORKDIR / 'friends'
        self.servers_dir = MANAGER_WORKDIR / 'servers'

        if not all((
            self.manager_workdir.exists(),
            self.flask_dir.exists(),
            self.servers_dir.exists(),
        )):
            raise ContextError('ERROR: paths are changed')

    def _in_docker(self):
        """Check out for a container flag."""
        self.indocker = Path(self.manager_workdir, 'indocker').exists()

    def _in_github_workflow(self):
        """Check out for a GitHub environment."""
        ci = os.environ.get('GITHUB_ACTIONS')
        self.in_github_ci = ci is not None

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

        :param options: argparse.Namespace(lite=bool)
        """
        self.autotest = False
        self.testpath = None
        self.development = True

        if options.lite:
            self.gunicorn = False
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
            self.testpath = Path(self.manager_workdir, Path(path))
        else:
            self.testpath = None


CONTEXT = Context()


def get_context() -> Context:
    """
    Return context of the program.

    :returns: a Context instance
    """
    return CONTEXT
