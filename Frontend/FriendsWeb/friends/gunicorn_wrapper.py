"""
An interface to Gunicorn.

https://docs.gunicorn.org/en/stable/custom.html
"""
from gunicorn.app.base import BaseApplication


class GunicornWrapper(BaseApplication):
    """Interface to set up and run a server from a script."""

    def __init__(self, app=None, options=None):
        self.application = app
        defaults = {'bind': '127.0.0.1:8080', 'workers': 2, 'timeout': 1}
        self.options = options or defaults

        super().__init__()

    def load_config(self):
        """Load the configuration."""
        for key, value in self.options.items():
            if key in self.cfg.settings and value is not None:
                self.cfg.set(key.lower(), value)

    def load(self):
        """Return an application from __init__()."""
        return self.application
