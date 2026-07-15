from typing import Generator


def fib6(n: int) -> Generator[int, None, None]:
    """Generate Fibonacci numbers up to the nth Fibonacci number."""
    yield 0  # Yield the first Fibonacci number (F(0)).
    if n > 0:
        yield 1  # Yield the second Fibonacci number (F(1)).
    last: int = (
        0  # Initialize the variable to store the last Fibonacci number (F(n-2)).
    )
    next: int = (
        1  # Initialize the variable to store the next Fibonacci number (F(n-1)).
    )
    for _ in range(
        1, n
    ):  # Loop from 1 to n-1 to generate Fibonacci numbers up to F(n).
        last, next = (
            next,
            last + next,
        )  # Update the last and next Fibonacci numbers iteratively.
        yield next  # Yield the current Fibonacci number.


if __name__ == "__main__":
    for fib_number in fib6(10):
        print(fib_number)  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    # Note: This implementation is efficient for generating Fibonacci numbers up to n due to its iterative approach and use of a generator, which allows for lazy evaluation and reduced memory usage.
