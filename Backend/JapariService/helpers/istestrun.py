"""Recognizes a test context."""
import __main__
import sys


def check() -> bool:
    """
    Check for a test-mode.

    The context must be recognized as a test context
    if the program is started with the "test" substring
    in one of the arguments,
    or if it is executed from the **manage.py**.

    :returns: bool
    """
    if any((True for arg in sys.argv if 'test' in arg)):
        return True
    elif ('__file__' in dir(__main__)
          and __main__.__file__.endswith('manage.py')):
        return True
    else:
        return False
