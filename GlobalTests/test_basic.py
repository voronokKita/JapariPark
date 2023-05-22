"""Some base tests."""

import pytest
from GlobalTests.context import PROJECT_DIR


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
            PROJECT_DIR / '.gitignore',
            PROJECT_DIR / 'Pipfile',
            PROJECT_DIR / 'requirements.txt',
            PROJECT_DIR / 'requirements_test.txt',

            PROJECT_DIR / 'setup.cfg',
        }
        for path in files:
            assert path.exists() is True
