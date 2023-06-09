"""Process an absolute path to the base directories."""
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

if (basedir := BASE_DIR.as_posix()) not in sys.path:
    sys.path.insert(0, basedir)

SECRETS_DIR = Path('/run/secrets').resolve()

APPS_DIR = BASE_DIR / 'apps'

COREAPP_DIR = APPS_DIR / 'core'
ACCOUNTS_DIR = APPS_DIR / 'accounts'
FRIENDS_DIR = APPS_DIR / 'friends'
