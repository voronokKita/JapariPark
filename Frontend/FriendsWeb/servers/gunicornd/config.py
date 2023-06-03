"""Gunicorn configurations."""
from gunicorn.app.base import BaseApplication as GunicornWrapper


class GunicornApplication(GunicornWrapper):
    """
    An interface for Gunicorn.

    https://docs.gunicorn.org/en/stable/custom.html
    """

    def __init__(self, app=None, options=None):
        self.application = app
        self.options = options or {}

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
