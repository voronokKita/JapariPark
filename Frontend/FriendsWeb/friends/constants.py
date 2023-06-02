"""Friends Web - constants and exceptions are here."""
from helpers import base_dir


HOST = '0.0.0.0'
PORT = 5000


MANAGER_WORKDIR = base_dir.get_path()
FLASK_DIR = MANAGER_WORKDIR / 'friends'


GUNICORN_OPTIONS = {
    'bind': f'{HOST}:{PORT}',
    'timeout': 1,
}
