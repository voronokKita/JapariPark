"""Check for the DB accessibility."""
import sys
import psycopg2

from JapariService.dbconf import DB_CONF
from JapariService.helpers import isdocker

NO_PASS = ("[ WARNING: a database password not found, " +
           "initializing the local database. ]")
NO_DOCKER = ("[ WARNING: running not in a container, " +
             "the local database will be initialized. ]")
NO_CONNECT = ("[ WARNING: can't connect to the remote database, " +
              "initializing the local database. ]")


if not isdocker.check():
    if sys.stdout.isatty():
        print(NO_DOCKER, end='\n\n')
    DATABASE_ONLINE = False
elif not DB_CONF.password:
    if sys.stdout.isatty():
        print(NO_PASS, end='\n\n')
    DATABASE_ONLINE = False
else:
    try:
        conn = psycopg2.connect(
            host=DB_CONF.host,
            port=DB_CONF.port,
            dbname=DB_CONF.dbname,
            user=DB_CONF.user,
            password=DB_CONF.password,
        )
        conn.close()
    except psycopg2.OperationalError:
        if sys.stdout.isatty():
            print(NO_CONNECT, end='\n\n')
        DATABASE_ONLINE = False
    else:
        DATABASE_ONLINE = True


def check() -> bool:
    """
    Check if the database is online.

    :returns: bool
    """
    return DATABASE_ONLINE
