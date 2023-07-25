"""Print to tty."""
import sys


def write(msg: str = ''):
    """Use the print if stdout to tty."""
    if sys.stdout.isatty():
        print(msg)
