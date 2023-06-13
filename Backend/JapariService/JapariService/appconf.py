"""Base settings for Django applications."""
from .pathfinder import APPS_DIR


FRIENDS_DIR = APPS_DIR / 'friends'

APP_CONF = {
    'friends': {'dir': FRIENDS_DIR},
}
