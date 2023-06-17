"""FriendsWeb settings."""
from pathlib import Path

from friends.pathfinder import BASE_DIR


SITE_DOMAIN = 'friends.japari-park.fun'
SITE_PORT = 8080

WERKZEUG_TESTPORT = 5001
GUNICORN_TESTPORT = 5002
