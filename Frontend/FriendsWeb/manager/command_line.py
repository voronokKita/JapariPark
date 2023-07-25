"""Argument Parser works."""
import argparse
from pathlib import Path


def get_parser() -> argparse.ArgumentParser:
    """Set up and return an argument parser."""
    top_parser = argparse.ArgumentParser(
        prog='friends/manage.py',
        description='FriendsWeb - a web frontend of Japari Park: Friends.',
        add_help=True,
    )
    subparsers = top_parser.add_subparsers(
        title='this program support different commands',
        description='use `[command] -h` for more help',
        required=True,
        dest='command',
    )

    # Command: runserver
    prod_parser = subparsers.add_parser(
        name='runserver',
        description='Run the application with a standalone server.',
        help='serve the application',
    )

    # Command: test [path]
    test_parser = subparsers.add_parser(
        name='test',
        description='Run the automated tests.',
        help='automatic testing',
    )
    test_parser.add_argument(
        'path',
        action='store',
        nargs='?',
        default='',
        help=("specify the path to the tests; path can be " +
              "relative (./) to the folder with manage.py or absolute (/)"),
    )
    return top_parser


def parse() -> argparse.Namespace:
    """
    Get the arguments from a command-line.

    :return: argparse.Namespace
    """
    return get_parser().parse_args()


def get_test_path(basedir: Path, path: str = '') -> Path | None:
    """
    Must resolve a path to tests as an absolute pathlib.Path object.

    :return: pathlib.Path OR None
    """
    if path != '':
        if path[0] == '/':
            return Path(path).resolve()
        elif path[:2] == './':
            return basedir / Path(path)
    return None
