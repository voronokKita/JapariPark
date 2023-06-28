"""
Recognizes a test context.

The context must be recognized as the test context
if the program is started with the "test" substring
in one of the arguments.
"""
import sys

TESTING = any((True for arg in sys.argv if 'test' in arg))


def check() -> bool:
    """
    Check for a test-mode.

    :returns: bool
    """
    return TESTING
