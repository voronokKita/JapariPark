"""Settings with absolute paths to the base directories."""
import sys
from pathlib import Path
from collections import namedtuple


BASE_DIR = Path(__file__).resolve().parents[1]

if BASE_DIR.as_posix() not in sys.path:
    sys.path.insert(0, BASE_DIR.as_posix())


STATIC_DIR = BASE_DIR / 'staticfiles'
TEMPLATES_DIR = BASE_DIR / 'templates'
SECRETS_DIR = BASE_DIR / 'secrets'
LOGS_DIR = BASE_DIR / 'mnt-logs'


Dirs = namedtuple(
    'Dirs',
    field_names=(
        'basedir', 'staticfiles', 'templates',
        'secrets', 'logs',
    ),
)

DIRS = Dirs(
    BASE_DIR, STATIC_DIR, TEMPLATES_DIR,
    SECRETS_DIR, LOGS_DIR,
)
