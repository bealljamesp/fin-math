def fib5(n: int) -> int:
    if n == 0:
        return n
    last: int = (
        0  # Initialize the variable to store the last Fibonacci number (F(n-2)).
    )
    next: int = (
        1  # Initialize the variable to store the next Fibonacci number (F(n-1)).
    )
    for _ in range(1, n):
        last, next = (
            next,
            last + next,
        )  # Update the last and next Fibonacci numbers iteratively.
    return (
        next  # Return the nth Fibonacci number, which is stored in the variable 'next'
    )


if __name__ == "__main__":
    print(fib5(100))  # Output: 55

    # Note: This implementation is efficient for large n due to its iterative approach, which avoids the overhead of recursive function calls and redundant calculations.
