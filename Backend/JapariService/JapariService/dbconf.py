"""Database config."""
from pathlib import Path
from collections import namedtuple

from JapariService.pathfinder import SECRETS_DIR


DB_PASSWORD = None
if (pass_file := Path(SECRETS_DIR, 'postgres_pass')).exists():
    with pass_file.open('r') as fl:
        DB_PASSWORD = fl.read().strip()

DB_HOST = 'japari-db.api'
DB_PORT = 5432
DB_USER = 'japari_service'

DataBaseConfig = namedtuple(
    'DataBaseConfig',
    field_names=('dbname', 'host', 'port', 'user', 'password'),
)

DEFAULT_DB = 'japari_park_default'
ACCOUNTS_DB = 'japari_park_accounts'
FRIENDS_DB = 'japari_friends'
FRIENDS_POSTS_DB = 'japari_friends_posts'


DB_CONF = {
    'default': DataBaseConfig(
        DEFAULT_DB, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD,
    ),
    'accounts': DataBaseConfig(
        ACCOUNTS_DB, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD,
    ),
    'friends': DataBaseConfig(
        FRIENDS_DB, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD,
    ),
    'friends-posts': DataBaseConfig(
        FRIENDS_POSTS_DB, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD,
    ),
}
