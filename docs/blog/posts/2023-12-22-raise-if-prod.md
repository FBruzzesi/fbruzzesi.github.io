---
draft: false
date: 2023-12-22
authors:
  - fbruzzesi
categories:
  - TIL
  - Python
tags:
  - Python
  - Decorators
  - TIL
---

# ❗Raise if... "prod"

Last weekend I was meeting with a former colleague of mine and we were discussing about some python code, as one does during a weekend.

<!-- more -->

While going through some high level code and architecture, he explained to me how they are using a python decorator called `non_prod_only` to raise an exception if a certain piece of code is run in production.

The idea is very simple, but effective at the same time. Whenever you decorate a function with `@non_prod_only`, you prevent your future self (that will be pushing to `main`) to remember that such functionality shouldn't end up in production.

And even if it does, you will get a *nice exception* that will save you from running the function.

## The decorator

Naive implementation of such decorator would be something along the following lines:

```py
import os
from functools import wraps

def is_prod():
    return os.environ.get("ENV", "").lower() in {"prod", "production"} # (1)

def non_prod_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_prod():
            raise Exception("This function is not allowed in production environment") # (2)
        return func(*args, **kwargs)
    return wrapper
```

1. Replace with whatever equivalent way you have to detect prod!
2. Please have some imagination and write a much more creative custom `Exception`!

## The larger picture

Now, in the larger scheme of things, a decorator such as `non_prod_only` is **far away** from the perfect solution to saving you from all the production troubles.

Yet, I still believe that there is a lot of value in abstracting its idea to a more general `raise_if` decorator, aiming at customization and flexibility.

```py
from functools import wraps

def raise_if(condition, exception = Exception, message = ""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if condition():
                raise exception(message)
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

<img src="../../../../../images/2023-12-22-raise-if-prod/confused.gif" width=230 height=230 align="right">

Oh gosh! That's a lot of nested functions! Let's break it down:

1. `raise_if` is a function that takes a `condition`[^1] and returns a decorator
2. The decorator takes a function `func` and returns a wrapper
3. The wrapper checks the `condition` and:
    * raises an `exception` if it is `True`
    * otherwise, it returns the result of `func`

If you want to read more about decorators with arguments, I wrote about it in the [deczoo documentation][deczoo].

## Type Annotation

Since many people (me included) are big fans of type annotations, let's try to add them to our `raise_if` decorator:

```py
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

def raise_if(
  condition: Callable[[], bool],
  exception: Exception = Exception,
  message: str = ""
  ):
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            if condition():
                raise exception(message)
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

[^1]: In this implementation `condition` is a callable that takes no arguments and returns a boolean value. It is evaluated at runtime, so it can be as complex as you want it to be.

[deczoo]: https://fbruzzesi.github.io/deczoo/decorators/advanced/#decorators-with-arguments

<img src="../../../../../images/written-by-human.svg" align="right">
