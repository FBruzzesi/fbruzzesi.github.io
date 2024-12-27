---
draft: false
date: 2024-05-07
comments: true
authors:
  - fbruzzesi
categories:
  - Tips
  - Programming
  - Python
---

# Pytest: does not raise

If you took the wise decision to test your codebase, you probably stumbled upon [pytest][pytest-docs] as the defacto tool that offers a large suite of features and extensions.

However, there is a neat trick I like to use when testing, and I often get the _"Wow! TIL about that!"_ reaction when introducing it.

<!-- more -->

Let's start with the basics and build upon on why you may want to use such trick in the first place.

## Parametrization

Pytest allows to [parametrize tests][pytest-parametrize] i.e. _"allows one to define multiple sets of arguments and fixtures at the test function or class"_.

Let's see a naive example in which we pass a set of three different inputs `(a, b, expected)`:

```py
import pytest


def my_sum(a, b):  # (1)
  """Sums a and b"""
  return a+b


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        ("1", "2", "12"),
        ((1,2), (3,4), (1,2,3,4)),
    ],
)
def test_sum(a, b, expected):
    """Tests expected behavior"""
    assert my_sum(a, b) == expected
```

1. A very fancy function, am I right?!

This way of defining function inputs and expected output is quite typical, and it avoids to write a test for each input.

## Testing Exceptions

There are times you want to test that a given exception is raised if a certain condition is met. pytests allows to check for that as well

```py title="Testing Exception"
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, "2"),
        (1, (1,2)),
        ("a", (3,4)),
    ],
)
def test_type_error(a, b):
    """Tests TypeError is raised"""
    with pytest.raises(TypeError):
        my_sum(a, b)
```

This is fine, so what's the issue with it?

There are cases in which you would like to test different types of error, ending up creating a single test function for each case.
To avoid the infinite growth of test functions, one can parametrize the `Exception` as well (I will show that in a moment).

But wouldn't it be nice and clean if also the expected behavior case could be treated in the same way instead of having a different test function?
Say no more! Enter: `does_not_raise`.

## `does_not_raise` context

!!! warning "Some public apologies"
    I really tried to dig deep to find when and how I came across this trick in the first place, but I couldn't manage to figure it out.
    I am honestly sorry for that 😞

Given the above behavior, all we need is a context that does... literally nothing! Lo and behold, python standard library offers that as [contextlib.nullcontext][nullcontext].

Let's rewrite the two example above as a unique test:

```py title="Unique suite"
from contextlib import nullcontext as does_not_raise

import pytest


@pytest.mark.parametrize(
    "a, b, expected, context, err_msg",
    [
        (1, 2, 3, does_not_raise(), ""),
        ("1", "2", "12", does_not_raise(), ""),
        ((1, 2), (3, 4), (1, 2, 3, 4), does_not_raise(), ""),
        (1, "2", None, pytest.raises(TypeError), "unsupported operand type"),
        (1, (1, 2), None, pytest.raises(TypeError), "unsupported operand type"),
        ("a", (3, 4), None, pytest.raises(TypeError), "unsupported operand type"),
    ],
)
def test_sum(a, b, expected, context, err_msg):
    """Tests `my_sum` function"""

    with context as exc_info:
        assert my_sum(a, b) == expected

    if exc_info:  # (1)
        assert err_msg in str(exc_info.value)
```

1. `exc_info` contains the error message generated inside the context. Thereafter we check that some message is contained in there.

I don't know about you, but I find it significantly simpler and cleaner to be able to keep all the cases and functionalities, including exceptions, of a given function or methods within the same parametrization.

!!! info "Why `does_not_raise`"
    The only reason to import `nullcontext` as `does_not_raise` is to keep the verb somewhat aligned with the `pytest.raises(...)` context 😁

<img src="../../../../../images/written-by-human.svg" align="right">

[pytest-docs]: https://docs.pytest.org/
[pytest-parametrize]: https://docs.pytest.org/how-to/parametrize.html#pytest-mark-parametrize-parametrizing-test-functions
[nullcontext]: https://docs.python.org/3/library/contextlib.html#contextlib.nullcontext
