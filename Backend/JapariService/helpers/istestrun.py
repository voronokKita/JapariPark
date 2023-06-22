"""
Recognizes a test context.

The context must be recognized as a test context
if the program is started with the "test" substring
in one of the arguments,
or if it is executed from the **manage.py**.
"""
import __main__
import sys


if any((True for arg in sys.argv if 'test' in arg)):
    TESTING = True
elif ('__file__' in dir(__main__)
      and __main__.__file__.endswith('manage.py')):
    TESTING = True
else:
    TESTING = False


def check() -> bool:
    """
    Check for a test-mode.

    :returns: bool
    """
    return TESTING
