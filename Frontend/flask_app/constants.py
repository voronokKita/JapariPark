"""All the flask's constants and exceptions are here."""

import sys
from pathlib import Path


FLASK_DIR = Path(__file__).resolve().parent
FRONTEND_WORKDIR = FLASK_DIR.parent


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
PORT = 5656

MAX_CONTENT_LENGTH = 15 * 1024 * 1024
