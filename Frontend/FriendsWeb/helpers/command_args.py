"""Argument Parser works."""
import argparse

import base_dir

BASE_DIR = base_dir.get_path()


def get_parser() -> argparse.ArgumentParser:
    """Set up and return an argument parser."""
    top_parser = argparse.ArgumentParser(
        prog='friends/manage.py',
        description='Friends - an application for web-clients of Japari Park.',
        epilog='[End of Help]',
        add_help=True,
    )
    subparsers = top_parser.add_subparsers(
        title='this program should support 3 commands:',
        description='use `[command] -h` for more help',
        required=True,
        dest='command',
        help='= production, development or automated tests',
    )

    # Command: production env
    prod_parser = subparsers.add_parser(
        name='run',
        help='- normal mode, for E2E testing or production',
        description='Run the program in a production environment.',
        epilog='[End of Help]',
    )

    # Command: development manual testing
    dev_parser = subparsers.add_parser(
        name='dev',
        help='- manual testing (development), with flexible settings',
        description=('Run the program in a development environment. ' +
                     'Serve through Gunicorn + NGINX. ' +
                     'Use --lite to serve through Werkzeug.'),
        epilog='[End of Help]',
    )
    dev_parser.add_argument(
        '--lite',
        action='store_true',
        default=False,
        required=False,
        help='serve through a Werkzeug server',
    )

    # Command: auto testing
    test_parser = subparsers.add_parser(
        name='test',
        help='- automatic testing',
        description='Run the automated tests with appropriate settings.',
        epilog='[End of Help]',
    )
    test_parser.add_argument(
        'path',
        action='store',
        nargs='?',
        default='',
        help=('- specify the path to the tests; path can be ' +
              'absolute `/` or relative `./` to the manage.py folder'),
    )
    return top_parser


def parse() -> argparse.Namespace:
    """
    Get the arguments from a command-line.

    :return: argparse.Namespace
    """
    parser = get_parser()
    return parser.parse_args()
