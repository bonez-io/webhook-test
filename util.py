"""Small helpers — kept separate so cross-file CALLS edges show up in the graph."""


def slugify(text: str) -> str:
    """Lowercase, trim, and dash-separate — used by app.greet."""
    return text.strip().lower().replace(" ", "-")
