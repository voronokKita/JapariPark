"""Process command-line arguments into a context object."""
import sys
from pathlib import Path
from helpers import base_dir


class Context:
    """
    Context of the working program.

    This object should be used in any program logic
    to determine the operating conditions.
    """

    __slots__ = (
        'indocker', 'testing', 'production',
        'e2e', 'werkzeug', 'gunicorn', 'nginx',
    )

    def __init__(
        self, indocker=False, testing=False, production=False,
        e2e=False, werkzeug=False, gunicorn=False, nginx=False,
    ):
        self.indocker = indocker

        self.testing = testing
        self.e2e = e2e
        self.production = production

        self.werkzeug = werkzeug
        self.gunicorn = gunicorn
        self.nginx = nginx


docker_flag = Path(base_dir.get_path(), 'indocker').exists()
len_sys_argv = len(sys.argv)
if len_sys_argv == 1:
    CONTEXT = Context(indocker=docker_flag, testing=True, werkzeug=True)
elif (len_sys_argv == 3
      and sys.argv[1] == 'testwith'
      and sys.argv[2] == 'werkzeug'):
    CONTEXT = Context(indocker=docker_flag, testing=True, werkzeug=True)
else:
    CONTEXT = Context()


def get_context() -> Context:
    """
    Return context of the program.

    :returns: a Context instance
    """
    return CONTEXT
