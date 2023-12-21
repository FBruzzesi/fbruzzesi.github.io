import re

from datetime import datetime
from typing import Annotated, Final, Optional
from jinja2 import Template
from typer import Typer, Option

from callbacks import authors_callback, multi_value_callback

ALPHANUMERIC: Final[re.Pattern] = re.compile(r"\W+")

app = Typer(name="automation CLI", help="CLI for automating tasks")


@app.command()
def create_new(
    title: Annotated[str, Option(help="Post title")],
    authors: Annotated[
        str,
        Option(
            help="Post authors, must belong to the authors list in `.authors.yml`",
            callback=authors_callback,
        ),
    ],
    date: Annotated[str, Option(help="Post date")] = datetime.now().strftime(
        "%Y-%m-%d"
    ),
    tags: Annotated[
        Optional[str],
        Option(
            help="Tags",
            callback=multi_value_callback,
        ),
    ] = None,
    categories: Annotated[
        Optional[str],
        Option(
            help="Categories",
            callback=multi_value_callback,
        ),
    ] = None,
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
