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

DB_DEFAULT = 'japari_park_default'
DB_ACCOUNTS = 'japari_park_accounts'
DB_FRIENDS = 'japari_friends'
DB_FRIENDS_POSTS = 'japari_friends_posts'


DB_CONF = {
    'default': DataBaseConfig(
        DB_DEFAULT, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD,
    ),
    'accounts': DataBaseConfig(
        DB_ACCOUNTS, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD,
    ),
    'friends': DataBaseConfig(
        DB_FRIENDS, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD,
    ),
    'friends-posts': DataBaseConfig(
        DB_FRIENDS_POSTS, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD,
    ),
}
