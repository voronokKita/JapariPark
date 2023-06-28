"""
Recognizes a development context.

The context must be recognized as the dev context
if the program is executed from the **manage.py**.
"""
import __main__


MANAGER = ('__file__' in dir(__main__)
           and __main__.__file__.endswith('manage.py'))


def check() -> bool:
    """
    Check for a dev-mode.

    :returns: bool
    """
    return MANAGER
