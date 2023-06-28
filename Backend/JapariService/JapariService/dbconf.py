"""Database config."""
import sys
from collections import namedtuple

from JapariService.pathfinder import SECRETS_DIR


DB_NAME = 'japari_park_database'
DB_HOST = 'japari-db.api'
DB_PORT = 5432
DB_USER = 'luckybot'


pass_file = SECRETS_DIR / 'postgres_pass'
if pass_file.exists():
    with pass_file.open('r') as fl:
        DB_PASSWORD = fl.read().strip()
else:
    DB_PASSWORD = None

DataBaseConfigs = namedtuple(
    'DataBaseConfigs',
    field_names=('dbname', 'host', 'port', 'user', 'password'),
)
DB_CONF = DataBaseConfigs(DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD)
