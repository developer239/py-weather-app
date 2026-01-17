"""Validation middleware using decorators."""

from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar

from flask import flash, redirect, url_for
from flask_wtf import FlaskForm

F = TypeVar("F", bound=Callable[..., Any])


def validate_form(
    form_class: type[FlaskForm],
    on_error: str,
) -> Callable[[F], F]:
    """
    Decorator that validates form before route executes.

    Args:
        form_class: The FlaskForm class to instantiate and validate
        on_error: Route name to redirect to on validation failure

    Returns:
        Decorated function that receives validated form as first argument
    """

    def decorator(f: F) -> F:
        @wraps(f)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            form = form_class()

            if not form.validate_on_submit():
                for errors in form.errors.values():
                    for error in errors:
                        flash(str(error), "error")
                return redirect(url_for(on_error))

            return f(form, *args, **kwargs)

        return wrapper  # type: ignore[return-value]

    return decorator
