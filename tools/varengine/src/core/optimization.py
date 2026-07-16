"""
Core module for memory-profile and execution-time optimization.
Demonstrates state-space restructuring using vectorized NumPy/Pandas operations.
"""

import numpy as np
import pandas as pd


class LedgerOptimizer:
    """
    Handles large-scale financial ledger processing and benchmarks
    row-by-row loops vs. vectorized memory-mapped operations.
    """

    def __init__(self, num_transactions: int = 1_000_000) -> None:
        self.num_transactions = num_transactions
        self._ledger_cache: list[dict[str, int | float]] | None = None
        self._df_cache: pd.DataFrame | None = None

    def generate_synthetic_ledger(self) -> list[dict[str, int | float]]:
        """
        Generates a synthetic contractor transaction ledger.

        Returns:
            list[dict[str, int | float]]: A list of transaction records.
        """
        if self._ledger_cache is not None:
            return self._ledger_cache

        print(f"Generating {self.num_transactions:,} synthetic ledger rows...")
        rng = np.random.default_rng(seed=42)

        # Vectorized generation to prevent generation bottlenecks
        billed_arr = rng.uniform(100.0, 5000.0, self.num_transactions)
        baseline_arr = rng.uniform(100.0, 4500.0, self.num_transactions)

        self._ledger_cache = [
            {
                "tx_id": i,
                "billed_amount": float(billed_arr[i]),
                "approved_baseline": float(baseline_arr[i]),
            }
            for i in range(self.num_transactions)
        ]
        return self._ledger_cache

    def get_dataframe(self) -> pd.DataFrame:
        """Converts the cached ledger into a structured Pandas DataFrame."""
        if self._df_cache is not None:
            return self._df_cache

        ledger_data = self.generate_synthetic_ledger()
        self._df_cache = pd.DataFrame(ledger_data)
        return self._df_cache

    def analyze_naive(
        self, ledger: list[dict[str, int | float]], threshold: float = 0.20
    ) -> list[int]:
        """
        Iterates row-by-row to flag over-billed contractor lines.

        Time Complexity: O(n)
        Memory Profile: O(n) for allocating the returned list
        """
        flagged_ids: list[int] = []
        for row in ledger:
            # Dynamic type-checking overhead occurs on every loop iteration
            variance = (row["billed_amount"] - row["approved_baseline"]) / row[
                "approved_baseline"
            ]
            if variance > threshold:
                flagged_ids.append(int(row["tx_id"]))
        return flagged_ids

    def analyze_vectorized(
        self, df: pd.DataFrame, threshold: float = 0.20
    ) -> np.ndarray:
        """
        Leverages C-compiled SIMD architectures to evaluate memory blocks at once.

        Time Complexity: O(n) at the hardware level, but executed natively in C
        Memory Profile: Highly optimized via contiguous array masking
        """
        # Restructure state-space into contiguous arrays
        billed: np.ndarray = df["billed_amount"].to_numpy()
        baseline: np.ndarray = df["approved_baseline"].to_numpy()
        tx_ids: np.ndarray = df["tx_id"].to_numpy()

        # Vectorized element-wise math calculation
        variances: np.ndarray = (billed - baseline) / baseline

        # Boolean masking operation (O(1) layout lookup)
        flagged_mask: np.ndarray = variances > threshold

        return tx_ids[flagged_mask]
