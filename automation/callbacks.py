from typing import Final, Optional
import yaml

AUTHORS_PATH: Final[str] = "docs/blog/.authors.yml"


def split_on(value: str, separator: str = ",") -> tuple[str, ...]:
    return tuple(item.strip() for item in value.split(separator))


def multi_value_callback(value: Optional[str] = None) -> Optional[tuple[str, ...]]:
    """Callback for multi-value options, split the value on commas if it exists."""
    return split_on(value, ",") if value else None


def authors_callback(value: str) -> tuple[str, ...]:
    """Callback for authors option, split the value on commas and validating that the authors exist in the authors list.

    The authors list is defined in `docs/blog/.authors.yml`.
    """
    with open(AUTHORS_PATH, "r") as stream:
        authors = yaml.safe_load(stream).get("authors", {})
        allowed_authors = set(authors.keys())

    input_authors = split_on(value, ",")

    for author in input_authors:
        if author not in allowed_authors:
            raise ValueError(f"Author `{author}` not found in authors list")

    return input_authors
