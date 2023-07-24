"""Settings with absolute paths to the base directories."""
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

if BASE_DIR.as_posix() not in sys.path:
    sys.path.insert(0, BASE_DIR.as_posix())


TEMPLATES_DIR = BASE_DIR / 'templates'
STATIC_DIR = BASE_DIR / 'static'
LOGS_DIR = BASE_DIR / 'mnt-logs'

SECRETS_DIR = Path('/run/secrets').resolve()

CONFIGS_DIR = BASE_DIR / 'configs'
FLASK_CONFIG = CONFIGS_DIR / 'flask.conf.py'
