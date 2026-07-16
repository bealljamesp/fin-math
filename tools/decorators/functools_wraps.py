# Use it when: You are writing your own custom decorator.

# When you wrap a function inside another function, you accidentally destroy the original function's metadata (its name, docstrings, and type annotations are overwritten by the wrapper). @functools.wraps copies the original metadata back onto the wrapper.

import functools
from collections.abc import Callable
from typing import Any


def audit_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)  # Preserves the original identity of 'func'
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Executing audit check on: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@audit_logger
def verify_clearance(contractor_id: int) -> bool:
    """Check federal compliance registry."""
    return True


# Without @functools.wraps, this would print 'wrapper' and None
print(verify_clearance.__name__)  # Output: verify_clearance
print(verify_clearance.__doc__)  # Output: Check federal compliance registry.
