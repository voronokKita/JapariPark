#!/usr/bin/env -S python -OO
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

from django.core.management import execute_from_command_line

base_dir = Path(__file__).resolve().parent.as_posix()
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JapariService.settings')
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
