"""
NGINX configurations.

On each run, the script will overwrite the server config file
from a template.

When first run on a new system, the script will try to
find the nginx settings folder, set write permission for it,
and write down initial settings into `nginx.conf`.

Setting permissions may require a password.

The script will then touch the `conf_is_set_flag` file.
This file can be deleted if you want to automatically update `nginx.conf`;
but it is better to change the settings manually.
"""
import getpass
import subprocess
from pathlib import Path

from config import (
    HOST_DOMAIN, SITE_PORT,
    PROXY_SOCKET, NGINX_CONFIG,
)


class NginxConfigNotFound(Exception):
    """Can't find a nginx config dir."""


def resolve_config_path():
    """
    Resolve an NGINX config path.

    By default, the configuration file is named nginx.conf and
    placed in the directory `/usr/local/nginx/conf`,
    `/etc/nginx`, or `/usr/local/etc/nginx`.

    :raises: NginxConfigNotFound
    """
    path_a = Path('/etc/nginx')
    path_b = Path('/usr/local/nginx/conf')
    path_c = Path('/usr/local/etc/nginx')

    if path_a.exists():
        return path_a
    elif path_b.exists():
        return path_b
    elif path_c.exists():
        return path_c
    else:
        raise NginxConfigNotFound()


def check_permissions(nginx_dir: Path):
    """Check out for permissions to write in nginx dir."""
    ls_result = subprocess.run(
        ['/usr/bin/ls', '-ld', nginx_dir.as_posix()],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=False, text=True,
    )
    if 'drwxrwxrwx' not in ls_result.stdout:
        subprocess.call(
            ['/usr/bin/sudo', '/usr/bin/chmod', '-R', '777',
             nginx_dir.as_posix()],
        )


def make_error_logs() -> str:
    """Generate a block with logs."""
    logs_dir = NGINX_CONFIG['nginx_logs_dir']
    log_path_list = []
    for lvl in NGINX_CONFIG['nginx_logs']:
        log_row = ('error_log  {DIR}/nginx_{LVL}.log   {LVL}; '.
                   format(DIR=logs_dir, LVL=lvl))
        log_path_list.append(log_row)

    return '\n'.join(log_path_list)


def make_main_nginx_config(nginx_dir: Path | str) -> str:
    """Fill an initial config template with data."""
    with NGINX_CONFIG['nginx_config_file'].open('r') as fl:
        template = fl.read()
    return template.format(
        USER=getpass.getuser(),
        ERROR_LOGS=make_error_logs(),
        PID_FILE=NGINX_CONFIG['nginx_pid_file'],
        NGINX_DIR=nginx_dir,
        ACCESS_LOG_DIR=NGINX_CONFIG['nginx_logs_dir'],
        FRIENDS_SERVER_CONF_FILE=Path(
            nginx_dir, 'site-available',
            NGINX_CONFIG['nginx_server_filename'],
        ),
    )


def make_application_config() -> str:
    """Fill a server config template with data."""
    with NGINX_CONFIG['nginx_server_file'].open('r') as fl:
        template = fl.read()
    return template.format(
        PORT=SITE_PORT,
        DOMAIN=HOST_DOMAIN,
        PROXY_SOCKET=PROXY_SOCKET,
    )


def make_config_backup(path: Path):
    """Backup an old configs."""
    if path.exists():
        path.rename(path.with_suffix('.backup.old'))


def process_main_config_file(nginx_dir: Path):
    """Process a config template and put it in the right place."""
    conf_is_set_flag = nginx_dir / 'conf_is_set_flag'
    if (conf_is_set_flag.exists()
            or not NGINX_CONFIG['write_initial_nginx_conf']):
        return

    nginx_conf_file = nginx_dir / 'nginx.conf'
    make_config_backup(nginx_conf_file)

    text = make_main_nginx_config(nginx_dir)
    with nginx_conf_file.open('w') as fl:
        fl.write(text)

    conf_is_set_flag.touch()


def process_server_config_file(nginx_dir: Path):
    """Process a config template and put it in the right place."""
    if not NGINX_CONFIG['write_nginx_server_conf']:
        return

    site_available_dir = nginx_dir / 'site-available'
    site_available_dir.mkdir(exist_ok=True)

    server_conf_file = Path(
        site_available_dir, NGINX_CONFIG['nginx_server_filename'],
    )
    text = make_application_config()
    with server_conf_file.open('w') as fl:
        fl.write(text)


nginx_config_dir = resolve_config_path()

check_permissions(nginx_config_dir)
process_main_config_file(nginx_config_dir)
process_server_config_file(nginx_config_dir)
