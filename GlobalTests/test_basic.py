"""Japari Park - basic tests."""

from GlobalTests.context import PROJECT_DIR


class TestBase:
    """Test project basic files."""

    __slots__ = ()

    def test_base_files(self):
        """Test core files not removed somehow."""
        files = {
            PROJECT_DIR / 'TODO.txt',
            PROJECT_DIR / 'Devlogs.txt',
            PROJECT_DIR / 'cover.jpeg',
            PROJECT_DIR / 'cover2.png',
            PROJECT_DIR / 'README.md',
            PROJECT_DIR / 'LICENSE',

            PROJECT_DIR / '.gitignore',
            PROJECT_DIR / 'pyproject.toml',

            PROJECT_DIR / 'Pipfile',
            PROJECT_DIR / 'requirements.txt',
            PROJECT_DIR / 'requirements_test.txt',

            PROJECT_DIR / 'setup.cfg',
            PROJECT_DIR / '.github' / 'workflows',

            PROJECT_DIR / 'FriendsFrontend',
            PROJECT_DIR / 'Backend',
            PROJECT_DIR / 'Database',
            PROJECT_DIR / 'SphinxDocs',
            PROJECT_DIR / 'additions' / 'git-hooks',
        }
        for path in files:
            assert path.exists() is True
