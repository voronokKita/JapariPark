#!/usr/bin/env -S python -OO
"""Automate migrations."""
import sys
import subprocess
from pathlib import Path

pt = sys.executable
workdir = Path(__file__).resolve().parent

commands = (
    [pt, 'manage.py', 'makemigrations'],
    [pt, 'manage.py', 'migrate'],
    [pt, 'manage.py', 'migrate', '--database=japari_park_accounts'],
    [pt, 'manage.py', 'migrate', '--database=japari_friends'],
    [pt, 'manage.py', 'migrate', '--database=japari_friends_posts'],
)

for cmd in commands:
    subprocess.call(cmd, executable=sys.executable,
                    cwd=workdir.as_posix(), shell=False)
    print()
