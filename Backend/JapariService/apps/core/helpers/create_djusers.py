"""Create some users from the start."""
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from JapariService.helpers import isdocker, istestrun, printer

BASE_DIR = settings.BASE_DIR
SECRETS_DIR = settings.SECRETS_DIR

User = get_user_model()


def get_superuser_pass():
    """
    Read and return superuser password.

    Will return "qwerty" if OSError.
    """
    if isdocker.check():
        passwordpath = SECRETS_DIR / 'django_superuser_pass'
    else:
        passwordpath = BASE_DIR / 'secrets' / '.django-superuser-pass.secret'

    try:
        with passwordpath.open('r') as fl:
            return fl.read().strip()
    except OSError:
        printer.write(('[ WARNING: Can not read superuser password, ' +
                       'using password "qwerty". ]'))
        return 'qwerty'


def create_superuser():
    """Create an admin, if not exists."""
    if User.objects.filter(username='admin').first():
        return
    printer.write(('[ WARNING: The "admin" superuser ' +
                   'not found - crating a new one. ]'))
    with transaction.atomic(using='default', durable=True):
        User.objects.create_superuser(
            'admin',
            email='admin@myproject.com',
            password=get_superuser_pass(),
        )


def run():
    """Create some users, if passable."""
    if istestrun.check():
        return
    create_superuser()
