"""Added in rung 2 to exercise an incremental reindex of a NEW file."""

from util import slugify


def shout(text: str) -> str:
    """Calls slugify — a fresh cross-file CALLS edge should appear in the graph."""
    return slugify(text).upper()
