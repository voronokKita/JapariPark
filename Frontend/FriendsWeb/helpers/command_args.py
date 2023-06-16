"""Argument Parser works."""
import argparse


def get_parser() -> argparse.ArgumentParser:
    """Set up and return an argument parser."""
    top_parser = argparse.ArgumentParser(
        prog='friends/manage.py',
        description='FriendsWeb - a web frontend of Japari Park: Friends.',
        add_help=True,
    )
    subparsers = top_parser.add_subparsers(
        title='this program should support 3 commands:',
        description='use `[command] -h` for more help',
        required=True,
        dest='command',
        help='= production, development or automated tests',
    )

    # Command: run; production env
    prod_parser = subparsers.add_parser(
        name='run',
        help='- normal mode, for E2E testing',
        description='Run the program in a production environment.',
    )

    # Command: dev [--lite]; development manual testing
    dev_parser = subparsers.add_parser(
        name='dev',
        help='- manual testing (development), with flexible settings',
        description=('Run the program in a development environment. ' +
                     'Will serve through Gunicorn. ' +
                     'Use --lite to serve through Werkzeug.'),
    )
    dev_parser.add_argument(
        '--lite',
        action='store_true',
        default=False,
        required=False,
        help='serve through a Werkzeug mini-server',
    )

    # Command: test [path]; auto testing
    test_parser = subparsers.add_parser(
        name='test',
        help='- automatic testing',
        description='Run the automated tests with appropriate settings.',
    )
    test_parser.add_argument(
        'path',
        action='store',
        nargs='?',
        default='',
        help=("- specify the path to the tests; path can be " +
              "relative `./` to the folder with manage.py or absolute `/`"),
    )
    return top_parser


def parse() -> argparse.Namespace:
    """
    Get the arguments from a command-line.

    :return: argparse.Namespace
    """
    parser = get_parser()
    return parser.parse_args()
