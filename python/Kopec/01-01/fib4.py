import functools


@functools.cache
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1)


if __name__ == "__main__":
    print(fib4(50))  # Output: 12586269025
    # Note: This implementation is efficient for large n due to the use of functools.cache, which provides memoization to avoid redundant calculations.
    print(
        fib4.cache_info()
    )  # Print cache information to see the number of hits and misses in the cache.

    print(fib4(50))  # Output: 12586269025
    print(
        fib4.cache_info()
    )  # Print cache information again to see the increase in hits due to the previous call.

    print(fib4(60))  # Output: 12586269025
    print(
        fib4.cache_info()
    )  # Print cache information again to see the increase in hits due to the previous call.

    print(fib4(60))  # Output: 12586269025
    print(
        fib4.cache_info()
    )  # Print cache information again to see the increase in hits due to the previous call.

    print(fib4(60))  # Output: 12586269025
    print(
        fib4.cache_info()
    )  # Print cache information again to see the increase in hits due to the previous call.

    print(fib4(60))  # Output: 12586269025
    print(
        fib4.cache_info()
    )  # Print cache information again to see the increase in hits due to the previous call.

    print(fib4(60))  # Output: 12586269025
    print(
        fib4.cache_info()
    )  # Print cache information again to see the increase in hits due to the previous call.
