def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)


if __name__ == "__main__":
    print(fib2(4))  # Output: 3
    print(fib2(20))  # Output: 6765
    print(fib2(30))  # Output: 832040
    # Note: This implementation is also inefficient for large n due to repeated calculations.
