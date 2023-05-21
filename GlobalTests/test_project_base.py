"""Some base tests."""

import sys
import pytest
import pathlib

PROJECT_DIR = pathlib.Path(__file__).resolve().parents[1]

as_str = PROJECT_DIR.as_posix()
if as_str not in sys.path:
    sys.path.insert(0, as_str)


def test_pytest_works():
    """Asser pytest works."""
    assert 2 + 2 == 4
    with pytest.raises(ZeroDivisionError):
        blank = 2 / 0


class TestBase:
    """Test base."""

    def test_base_files(self):
        """Test base files."""
        files = {
            PROJECT_DIR / 'TODO.txt',
            PROJECT_DIR / 'Development History.txt',
            PROJECT_DIR / 'cover.jpeg',
            PROJECT_DIR / 'README.md',
            PROJECT_DIR / 'Pipfile',

            PROJECT_DIR / 'Frontend',
            PROJECT_DIR / 'Backend',

            PROJECT_DIR / 'SphinxDocs',
        }
        for path in files:
            assert path.exists() is True
