"""FriendsWeb settings."""
from pathlib import Path
from FriendsWeb.pathfinder import BASE_DIR


# main contex switch
DEBUG = True
TESTPORT = 5001


SITE_DOMAIN = 'friends.japari-park.fun'
SITE_PORT = 8080

BACKEND_URL = 'http://japari-service.rest:80/friends'
