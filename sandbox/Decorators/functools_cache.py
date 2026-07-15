# use @functools.cache when you are executing a pure, deterministic function (same inputs always yield the identical output) that is either computationally expensive or repeatedly called with overlapping parameters, and you want to optimize lookups to O(1) constant time by storing results in an unbounded memoization hash map.
#
# Unlike @functools.lru_cache, @functools.cache does not impose a limit on the number of cached entries, making it suitable for scenarios where memory usage is not a concern and you want to maximize the performance benefits of memoization.


import functools


# Example usage
@functools.cache
def compute_contractor_score(contractor_id: int) -> float:
    # Simulates an expensive computation
    return float(contractor_id * 0.95)


# Execution
print(compute_contractor_score(1))  # Cached after first call
print(compute_contractor_score(2))  # Cached after first call
print(compute_contractor_score(1))  # Retrieved from cache
