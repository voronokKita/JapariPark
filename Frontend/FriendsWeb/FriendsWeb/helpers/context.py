"""Process an application context into a context object."""
import collections

from FriendsWeb.pathfinder import DIRS
from FriendsWeb.settings import DEBUG
from FriendsWeb.helpers import (
    isdocker, in_github_ci,
    istestrun, ismanage,
)


class Context:
    """
    Context of the working program.

    This object combines all the key information
    about the context of the program.

    :ivar bool indocker: running in a container?
    :ivar bool in_github_ci: running in a GitHub workflow?
    :ivar bool autotest: running automated tests?
    :ivar bool run_from_manager: running from a manage.py
    :ivar bool debug: running in development mode?
    :ivar collections.namedtuple dirs: an object with base paths
    """

    __slots__ = (
        'indocker', 'in_github_ci',
        'autotest', 'run_from_manager',
        'dirs', 'debug',
    )

    def __init__(self):
        self.indocker = isdocker.check()
        self.in_github_ci = in_github_ci.check()
        self.autotest = istestrun.check()
        self.run_from_manager = ismanage.check()
        self.debug = DEBUG
        self.dirs = DIRS


CONTEXT = Context()


def get_context() -> Context:
    """
    Return context of the program.

    :returns: a Context instance
    """
    return CONTEXT
