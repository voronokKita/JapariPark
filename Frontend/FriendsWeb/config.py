"""Base application and server configurations."""
from pathlib import Path
from base_dir import MANAGER_WORKDIR

# The final external address
HOST_IP = '127.0.0.1'
HOST_DOMAIN = 'localhost'
SITE_PORT = 5000

PROXY_SOCKET = Path('/tmp/friends.sock')


# Addresses for testing
WERKZEUG_TEST_PORT = 5050
MISC_TEST_PORT = 5030


# Servers config
SERVERS_CONFIGS_DIR = Path(MANAGER_WORKDIR, 'servers', 'configs')

# NGINX config
NGINX_CONFIG = {
    'write_initial_nginx_conf': True,
    'nginx_config_file': Path(SERVERS_CONFIGS_DIR, 'nginx.conf.template'),
    'nginx_pid_file': Path(MANAGER_WORKDIR, 'logs', 'servers', 'nginx.pid'),
    'nginx_logs_dir': Path(MANAGER_WORKDIR, 'logs', 'servers'),
    'nginx_logs': ('notice', 'error'),
    'write_nginx_server_conf': True,
    'nginx_server_file': Path(SERVERS_CONFIGS_DIR, 'friends.conf.template'),
    'nginx_server_filename': 'friends.conf',
}

# Gunicorn config
GUNICORN_CONFIG_FILE = Path(SERVERS_CONFIGS_DIR, 'gunicorn_configs.json')
