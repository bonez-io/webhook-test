"""Tiny app used to exercise the GitHub push-webhook reindex ladder.

greet() calls slugify() (cross-file CALLS edge); main() calls greet().
"""

from util import slugify


def greet(name: str) -> str:
    return f"hello, {slugify(name)}"


def main() -> None:
    print(greet("World"))


if __name__ == "__main__":
    main()
