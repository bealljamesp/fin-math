"""
Cost Estimate Verification & Anomaly Detection Pipeline.
Engineered using Python 3.11+ standards and vectorized performance layout.
"""

import functools
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class CostBaseline:
    base_unit_cost: float
    total_indirect_labor_pool: float
    historical_sales_velocity: float


class CostAnalysisEngine:
    def __init__(self, baseline: CostBaseline) -> None:
        self.baseline = baseline

    @functools.cache
    def calculate_theoretical_unit_cost(
        self, units_produced: int, labor_shift_pct: float
    ) -> float:
        """
        Calculates the theoretical GAAP product unit cost under absorption constraints.
        Leverages functools.cache for deterministic state-space memoization.
        """
        if units_produced <= 0:
            raise ValueError("Production volume must be greater than zero.")

        allocated_moh = self.baseline.total_indirect_labor_pool * labor_shift_pct
        unit_moh_allocation = allocated_moh / units_produced
        return self.baseline.base_unit_cost + unit_moh_allocation

    def audit_ledger_population(
        self,
        production_vector: np.ndarray,
        reported_operating_income: np.ndarray,
        labor_shift_vector: np.ndarray,
    ) -> dict[str, np.ndarray]:
        """
        Audits 100% of the reporting population using high-speed vectorized masks.

        Time Complexity: O(N) dominated by NumPy C-array array allocations.
        Space Complexity: O(N) for the memory allocation of tracking masks.
        """
        # Vectorized generation of theoretical unit costs across the state-space
        allocated_moh = self.baseline.total_indirect_labor_pool * labor_shift_vector
        theoretical_unit_costs = self.baseline.base_unit_cost + (
            allocated_moh / production_vector
        )

        # Calculate theoretical COGS and Operating Income assuming market demand is met
        theoretical_cogs = (
            self.baseline.historical_sales_velocity * theoretical_unit_costs
        )
        theoretical_revenue = (
            self.baseline.historical_sales_velocity * 100.0
        )  # Assumed static price
        unshifted_sga = self.baseline.total_indirect_labor_pool * (
            1.0 - labor_shift_vector
        )

        theoretical_operating_income = (
            theoretical_revenue - theoretical_cogs
        ) - unshifted_sga

        # Rigorous Anomaly Filter: Flag where reported operating income matches
        # the exact mathematical signature of an overproduction cushion.
        # Condition: Inventory Days build up while profit spikes beyond standard baseline bounds.
        income_variance = reported_operating_income - theoretical_operating_income
        inventory_build_units = (
            production_vector - self.baseline.historical_sales_velocity
        )

        # Boolean masks executing natively in C-velocity
        is_padded = (inventory_build_units > 2000) & (income_variance > 10000)

        return {
            "theoretical_unit_costs": theoretical_unit_costs,
            "variance_profiles": income_variance,
            "anomaly_flags": is_padded,
        }


# --- Execution Sandbox ---
if __name__ == "__main__":
    # Initialize baseline operational thresholds
    base_profile = CostBaseline(
        base_unit_cost=50.0,
        total_indirect_labor_pool=200000.0,
        historical_sales_velocity=10000.0,
    )

    engine = CostAnalysisEngine(baseline=base_profile)

    # 1. Generate the Synthetic Ledger Population (1 Million Rows)
    num_records = 1_000_000
    np.random.seed(42)  # Ensures the "randomness" is deterministic and repeatable

    sim_production = np.random.randint(10000, 25000, size=num_records)
    sim_labor_shift = np.random.uniform(0.1, 0.9, size=num_records)
    sim_reported_income = np.random.uniform(250000, 450000, size=num_records)

    # 2. Process the Audit Engine
    audit_results = engine.audit_ledger_population(
        production_vector=sim_production,
        reported_operating_income=sim_reported_income,
        labor_shift_vector=sim_labor_shift,
    )

    # 3. Extract and Inspect the Flagged Lines via Boolean Masking
    flags = audit_results["anomaly_flags"]
    total_flags = np.sum(flags)

    print(f"Engine Run Successful. Processed {num_records:,} contract lines.")
    print(f"Systemic Cost Anomalies Isolated: {total_flags:,} lines flagged.\n")

    # Isolate the exact data attributes for the flagged records using the boolean mask
    flagged_indices = np.where(flags)[0]  # Extracts the actual row numbers
    flagged_production = sim_production[flags]
    flagged_labor_shift = sim_labor_shift[flags]
    flagged_income = sim_reported_income[flags]
    flagged_variance = audit_results["variance_profiles"][flags]

    # 4. Print a Tabular Audit Preview of the First 5 Target Records
    print(
        f"{'Ledger Row':<10} | {'Units Produced':<14} | {'Labor Shift %':<13} | {'Reported Profit':<15} | {'Profit Padding':<14}"
    )
    print("-" * 78)

    preview_limit = min(5, total_flags)
    for i in range(preview_limit):
        print(
            f"{flagged_indices[i]:<10} | "
            f"{flagged_production[i]:<14,} | "
            f"{flagged_labor_shift[i] * 100:<12.1f}% | "
            f"${flagged_income[i]:<14,.2f} | "
            f"${flagged_variance[i]:<13,.2f}"
        )
