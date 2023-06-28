"""
Recognizes a manager context.

The context must be recognized as the manager
if the program is executed from the **manage.py**.
"""
import __main__

MANAGER = ('__file__' in dir(__main__)
           and __main__.__file__.endswith('manage.py'))


def check() -> bool:
    """
    Check for a manager-mode.

    :returns: bool
    """
    return MANAGER
