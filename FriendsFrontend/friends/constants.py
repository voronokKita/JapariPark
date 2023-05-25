"""Friends' frontend constants and exceptions are here."""

import sys
from pathlib import Path


FLASK_WORKDIR = Path(__file__).resolve().parent
MANAGER_DIR = FLASK_WORKDIR.parent

TESTING = False
PRODUCTION_TESTING = False
for arg in sys.argv:
    if 'production_tests' in arg:
        PRODUCTION_TESTING = True
        break
    elif 'test' in arg:
        TESTING = True
        break


HOST = '127.0.0.1'
PORT = 5000

MAX_CONTENT_LENGTH = 15 * 1024 * 1024
