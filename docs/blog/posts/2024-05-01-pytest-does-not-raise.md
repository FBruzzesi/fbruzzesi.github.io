---
draft: true
date: 2024-05-01
authors:
  - fbruzzesi
categories:
  - Tips
  - Programming
  - Python
---

# Pytest: does not raise

If you decided to move forward and test your codebase, you probably stumbled upon [pytest][pytest-docs] as the defacto tool that offers a large suite of features and extensions.

However, there is a neat trick I like to use when testing, and often get the "TIL about that" reaction when introducing it.

<!-- more -->

## Parametrization

Pytest allows to [parametrize tests][pytest-parametrize] i.e. _"allows one to define multiple sets of arguments and fixtures at the test function or class"_.

Let's see a naive example in which we pass a set of three different inputs `(a, b, expected)`:

```py
import pytest

@pytest.mark.parametrize(
  "a,b,expected",
  [
    (1, 2, 3),
    ("1", "2", "12"),
    ((1,2), (3,4), (1,2,3,4))
  ]
)
def test_sum(a, b, expected):
    assert a + b == expected
```

This way of defining some function input and its expected output is quite typical.

## Testing Exceptions

## `does_not_raise`


<img src="../../../../../images/written-by-human.svg" align="right">

[pytest-docs]: https://docs.pytest.org/
[pytest-parametrize]: https://docs.pytest.org/how-to/parametrize.html#pytest-mark-parametrize-parametrizing-test-functions
