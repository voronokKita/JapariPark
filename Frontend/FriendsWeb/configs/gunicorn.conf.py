import sys

bind = '0.0.0.0:80'


# Debugging
reload = False


# Logging
accesslog = './mnt-logs/gunicorn/access.log'
access_log_format = '%(t)s: %(m)s %(U)s %(s)s - %(h)s %(a)s'
errorlog = './mnt-logs/gunicorn/errors.log'
loglevel = 'warning'
# syslog_addr = monitor


# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190


# Server Hooks
def when_ready(server):
    if sys.stdout.isatty():
        print('[Note: you can write some server hooks]')


# Server Mechanics
pidfile = './mnt-logs/gunicorn/gunicorn.pid'
preload_app = True
daemon = False
forwarded_allow_ips = '*'
proxy_allow_ips = '*'


# Server Socket
backlog = 1024


# Worker Processes
workers = 2
worker_class = 'sync'
worker_connections = 500
max_requests = 1000
max_requests_jitter = 50
timeout = 30
graceful_timeout = 10
keepalive = 5
