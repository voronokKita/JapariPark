"""Process command-line arguments into a context object."""
import os
import sys
from pathlib import Path

from helpers import command_args


class ContextError(Exception):
    """Error: context is changed."""


def in_dev_context(func):
    """Return False if not in a development env or if in autotests."""
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

    :ivar Path base_dir: an absolute path to the manager.py folder
    """

    __slots__ = (
        'indocker', 'in_github_ci',
        'autotest', 'testpath',
        'development', 'gunicorn',
        'base_dir',
    )

    def __init__(self):
        self._set_paths()
        self._in_docker()
        self._in_github_workflow()

        if 'manage.py' not in sys.argv[0]:
            if any((True for arg in sys.argv if 'test' in arg)):
                self._context_auto_testing()
            else:
                # if manage.py != __main__ and not test:
                # most likely this is a direct call to
                # the wsgi interface from a normal server
                self._context_production()
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
            return 'Context(dev gunicorn)'

    def __repr__(self):
        st = ('Context(indocker={D}, in_github_ci={CI}, ' +
              'autotest={AT}, development={DEV}, ' +
              'gunicorn={GU}, workdir={CWD})')
        return st.format(
            D=self.indocker,
            CI=self.in_github_ci,
            AT=self.autotest,
            DEV=self.development,
            GU=self.gunicorn,
            CWD=self.base_dir.as_posix(),
        )

    def in_production(self):
        """Return True if not in development and not in autotests."""
        return not self.autotest and not self.development

    @in_dev_context
    def dev_normal(self):
        """Return True if in a normal dev env."""
        return self.gunicorn

    @in_dev_context
    def dev_lite(self):
        """Return True if in a dev --lite env."""
        return not self.gunicorn

    def _set_paths(self):
        """Resolve paths."""
        self.base_dir = Path(__file__).resolve().parents[1]

    def _in_docker(self):
        """Check out for a container flag."""
        self.indocker = Path(self.base_dir, 'indocker').exists()

    def _in_github_workflow(self):
        """Check out for a GitHub environment."""
        self.in_github_ci = os.environ.get('GITHUB_ACTIONS') is not None

    def _context_production(self):
        """Working in a normal mode: Gunicorn + NGINX."""
        self.autotest = False
        self.testpath = None
        self.development = False
        self.gunicorn = True

    def _context_development(self, options):
        """
        Working in a dev mod.

        :param options: argparse.Namespace(lite=bool)
        """
        self.autotest = False
        self.testpath = None
        self.development = True
        self.gunicorn = not options.lite

    def _context_auto_testing(self, path: str = ''):
        """
        Working in an auto-test mod.

        :param path: optional path to tests
        """
        self.autotest = True
        self.development = True
        self.gunicorn = False

        if path != '' and path[0] == '/':
            self.testpath = Path(path).resolve()
        elif path != '' and path[:2] == './':
            self.testpath = Path(self.base_dir, Path(path))
        else:
            self.testpath = None


CONTEXT = Context()


def get_context() -> Context:
    """
    Return context of the program.

    :returns: a Context instance
    """
    return CONTEXT
