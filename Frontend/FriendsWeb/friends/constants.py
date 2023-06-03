"""Friends Web - constants and exceptions are here."""
from helpers import base_dir, context


class WrongEnvironmentError(Exception):
    """Try to serve in a wrong environment."""
