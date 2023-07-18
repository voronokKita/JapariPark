"""Friends Web Exceptions are here."""


class WrongEnvironmentError(Exception):
    """Attempt to serve in a wrong environment."""


class ContextError(Exception):
    """Error: context is changed."""
