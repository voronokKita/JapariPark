"""To give atomized tests some context."""
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

if BASE_DIR.as_posix() not in sys.path:
    sys.path.insert(0, BASE_DIR.as_posix())
