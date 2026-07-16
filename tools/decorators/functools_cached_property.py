# Use it when: You want to transform a class method into a property that computes its value exactly once, then caches it as a normal attribute for the lifespan of the object.

# This is ideal for data-heavy objects (like a ledger or portfolio) where calculating a metric (like variance or total risk) is computationally expensive, but the underlying data doesn't change after the object is created.

import functools

import numpy as np


class ContractLedger:
    def __init__(self, cost_array: list[float]) -> None:
        self.costs = np.array(cost_array)

    @functools.cached_property
    def heavy_statistical_variance(self) -> float:
        """Computes variance once. Subsequent accesses skip the math entirely."""
        print("Executing expensive variance calculation...")
        return float(np.var(self.costs))


# Execution
ledger = ContractLedger([100.5, 200.2, 300.8, 400.1])
print(ledger.heavy_statistical_variance)  # Prints message, calculates, returns value.
print(ledger.heavy_statistical_variance)  # Skips math, returns cached value instantly.
