# python automation/__main__.py --title "XYZ"
import re

from datetime import datetime
from typing import Annotated, Final, Optional
import yaml

from jinja2 import Template
from typer import Typer, Option

ALPHANUMERIC: Final[re.Pattern] = re.compile(r"\W+")
AUTHORS_PATH: Final[str] = "docs/blog/.authors.yml"


def split_on(value: str, separator: str = ",") -> tuple[str, ...]:
    """Split a string on a separator and return a tuple of the items."""
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


app = Typer(name="automation CLI", help="CLI for automating tasks")

TITLE_OPTION = Annotated[str, Option(help="Post title")]
AUTHORS_OPTION = Annotated[str, Option(help="Authors, must be in `.authors.yml`", callback=authors_callback)]
DATE_OPTION = Annotated[str, Option(help="Post date")]
TAGS_OPTION = Annotated[Optional[str], Option(help="Tags", callback=multi_value_callback)]
CATEGORIES_OPTION = Annotated[Optional[str], Option(help="Categories", callback=multi_value_callback)]


@app.command()
def create_new(
    title: TITLE_OPTION,
    authors: AUTHORS_OPTION = "fbruzzesi",
    date: DATE_OPTION = datetime.now().strftime("%Y-%m-%d"),
    tags: TAGS_OPTION = None,
    categories: CATEGORIES_OPTION = None,
):
    """Create a new post in `docs/blog/posts` with the given title, authors, date, tags and categories."""

    values = {
        "title": title,
        "authors": authors,
        "date": date,
        "tags": tags,
        "categories": categories,
    }

    with open("automation/template.md", "r") as source:
        template = Template(source.read(), trim_blocks=True)

    parsed_title = re.sub(ALPHANUMERIC, " ", title).replace(" ", "-").lower()

    with open(f"docs/blog/posts/{date}-{parsed_title}.md", "w") as destination:
        destination.write(template.render(values))


if __name__ == "__main__":
    app()
