"""
Pgadmin configs.

https://www.pgadmin.org/docs/pgadmin4/latest/config_py.html#config-py
"""
import logging


LOGIN_BANNER = '☆’.･.･:★’.･.･:☆    (´• ω •`)ﾉﾞ Hello!    ☆’.･.･:★’.･.･:☆'

# ~ Log settings ~ #
CONSOLE_LOG_LEVEL = logging.WARNING
FILE_LOG_LEVEL = logging.WARNING

CONSOLE_LOG_FORMAT = '[%(asctime)s - %(levelname)s, %(name)s]: %(message)s'
FILE_LOG_FORMAT = '[%(asctime)s - %(levelname)s, %(name)s]: %(message)s'

LOG_FILE = '/JapariPGA/logs/pgadmin.log'

LOG_ROTATION_SIZE = 10  # In MBs
LOG_ROTATION_AGE = 1440  # In minutes
LOG_ROTATION_MAX_LOG_FILES = 5  # Maximum number of backups to retain


# ~ User account and settings storage ~ #
ALLOW_SAVE_PASSWORD = False

# ~ Auth ~ #
MAX_LOGIN_ATTEMPTS = 10
