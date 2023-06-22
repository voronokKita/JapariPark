"""Process an absolute path to the base directories."""
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

if (base_dir := BASE_DIR.as_posix()) not in sys.path:
    sys.path.insert(0, base_dir)


STATIC_DIR = BASE_DIR / 'staticfiles'
LOGS_DIR = BASE_DIR / 'logs'
