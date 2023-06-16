"""Japari Park - basic tests."""
import pathlib

PROJECT_DIR = pathlib.Path(__file__).resolve().parents[1]


class TestBase:
    """Test project basic files."""

    __slots__ = ()

    def test_base_files(self):
        """Test that core files not removed somehow."""
        files = {
            PROJECT_DIR / 'cover.jpeg',
            PROJECT_DIR / 'cover2.png',
            PROJECT_DIR / 'README.md',
            PROJECT_DIR / 'LICENSE',

            PROJECT_DIR / '.gitignore',
            PROJECT_DIR / 'pyproject.toml',

            PROJECT_DIR / 'docker-compose.yaml',

            PROJECT_DIR / 'Pipfile',
            PROJECT_DIR / 'requirements.txt',

            PROJECT_DIR / 'setup.cfg',
            PROJECT_DIR / '.github' / 'workflows' / 'test_master_branch.yml',

            PROJECT_DIR / 'Frontend',
            PROJECT_DIR / 'Backend',
            PROJECT_DIR / 'Database',
            PROJECT_DIR / 'SphinxDocs',
            PROJECT_DIR / 'additions' / 'git-hooks',
        }
        for path in files:
            assert path.exists() is True
