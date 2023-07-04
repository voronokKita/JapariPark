"""Print to tty."""
import sys


def write(msg: str):
    """Use the print if is a tty."""
    if sys.stdout.isatty():
        print(msg)
