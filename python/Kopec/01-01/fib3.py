from typing import Dict

memo: Dict[int, int] = {
    0: 0,
    1: 1,
}  # Initialize the memoization dictionary with base cases for Fibonacci numbers.


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = (
            fib3(n - 1) + fib3(n - 2)
        )  # Compute the Fibonacci number recursively and store it in the memoization dictionary.
    return memo[n]


if __name__ == "__main__":
    print(fib3(10))  # Output: 55
    print(fib3(20))  # Output: 6765
    print(fib3(30))  # Output: 832040
    # print(fib3(50))  # Output: 12586269025
    # Note: This implementation is efficient for large n due to memoization, which avoids redundant calculations.

print(memo)  # Print the memoization dictionary to see the stored Fibonacci numbers.
