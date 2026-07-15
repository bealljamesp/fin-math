def fib1(n: int) -> int:
    """Return the nth Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)


if __name__ == "__main__":
    print(fib1(10))  # Output: 55
    print(fib1(20))  # Output: 6765
    print(fib1(30))  # Output: 832040
    # Note: The above implementation is inefficient for large n due to repeated calculations.
