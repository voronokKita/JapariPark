"""Inside a GitHub workflow."""
import os

GITHUB_CI = os.environ.get('GITHUB_ACTIONS') is not None


def check() -> bool:
    """
    Check for a GitHub workflow.

    :returns: bool
    """
    return GITHUB_CI
