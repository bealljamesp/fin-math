# Use it when: You need memoization (like @functools.cache), but you are handling an infinite stream of data and must enforce a strict memory cap to prevent cache growth from causing an out-of-memory error.

# While @functools.cache is unbounded, lru_cache (Least Recently Used) drops the oldest cached entries when the cache hits your specified maxsize threshold, maintaining a constant memory profile.

import functools


# Enforces a hard limit of 128 cached items in memory
@functools.lru_cache(maxsize=128)
def fetch_contractor_score(contractor_id: int) -> float:
    # Simulates an expensive database read
    return float(contractor_id * 0.95)
