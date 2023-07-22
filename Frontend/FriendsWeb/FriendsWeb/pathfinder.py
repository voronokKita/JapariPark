"""Settings with absolute paths to the base directories."""
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

if BASE_DIR.as_posix() not in sys.path:
    sys.path.insert(0, BASE_DIR.as_posix())


TEMPLATES_DIR = BASE_DIR / 'templates'
STATIC_DIR = BASE_DIR / 'static'
SECRETS_DIR = BASE_DIR / 'secrets'
LOGS_DIR = BASE_DIR / 'mnt-logs'
