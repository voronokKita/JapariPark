"""Japari Park: Friends Web - on startup configurations."""
from flask import Flask
from gunicorn.app.base import BaseApplication as GunicornWrapper
from gunicorn.arbiter import Arbiter

from friends.constants import FLASK_DIR, GUNICORN_OPTIONS
from helpers import context

CONTEXT = context.get_context()


# Configure Flask
APPLICATION = Flask('FriendsWeb', root_path=FLASK_DIR.as_posix())
APPLICATION.config.update(
    PROPAGATE_EXCEPTIONS=True,
    LOGGER_NAME='friends_flask_logger',
)

if CONTEXT.development or CONTEXT.autotest:
    APPLICATION.config.update(
        ENV='development',
        DEBUG=True,
        TESTING=True,
    )
else:
    APPLICATION.config.update(
        ENV='production',
        DEBUG=False,
        TESTING=False,
    )


# Configure Gunicorn
class GunicornApplication(GunicornWrapper):
    """
    An interface for Gunicorn.

    https://docs.gunicorn.org/en/stable/custom.html
    """

    link_to_arbiter: Arbiter

    def __init__(self, app=APPLICATION, options=GUNICORN_OPTIONS):
        self.options = options
        self.application = app
        super().__init__()

    def load_config(self):
        """Load the configuration."""
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        """Return a Flask application from __init__(app)."""
        return self.application

    # def run(self):
    #     self.link_to_arbiter = Arbiter(self)
    #     try:
    #         self.link_to_arbiter.run()
    #     except RuntimeError as e:
    #         print("\nError: %s\n" % e, file=sys.stderr)
    #         sys.stderr.flush()
    #         sys.exit(1)
    #
    # def main_stop(self, graceful=True):
    #     self.link_to_arbiter.stop(graceful)
