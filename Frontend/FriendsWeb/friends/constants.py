"""Friends Web - constants and exceptions are here."""
from helpers import base_dir


APPLICATION_HOST = '0.0.0.0'
APPLICATION_PORT = 5000


MANAGER_WORKDIR = base_dir.get_path()
FLASK_DIR = MANAGER_WORKDIR / 'friends'


MAX_CONTENT_LENGTH = 15 * 1024 * 1024
