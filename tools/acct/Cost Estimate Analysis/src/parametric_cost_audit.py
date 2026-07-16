"""
Generalized Parametric Cost Estimation and Proposal Inflation Audit Engine.
Engineered using Python 3.11+ standards and optimized vectorized execution loops.
"""

import functools
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ParametricCostModel:
    """
    Stores immutable cost parameters for the baseline estimation model.
    Expected Cost = Fixed Base Cost + (Labor Hours * Labor Rate) + (Material Units * Material Rate)
    """

    fixed_base_cost: float
    labor_rate_per_hour: float
    material_rate_per_unit: float


class ParametricAuditEngine:
    def __init__(self, model: ParametricCostModel) -> None:
        self.model = model

    @functools.cache
    def compute_single_expected_cost(self, hours: float, units: float) -> float:
        """
        Deterministic evaluation point using O(1) hash map memoization for repeated parameters.
        """
        return (
            self.model.fixed_base_cost
            + (hours * self.model.labor_rate_per_hour)
            + (units * self.model.material_rate_per_unit)
        )

    def audit_proposal_population(
        self,
        proposed_costs_vector: np.ndarray,
        labor_hours_matrix: np.ndarray,
        material_units_matrix: np.ndarray,
        inflation_tolerance_pct: float = 0.15,
    ) -> dict[str, np.ndarray]:
        """
        Processes 100% of proposal line items instantly via parallelized SIMD execution.

        Time Complexity: O(N) linear execution profile driven by continuous C-arrays.
        Space Complexity: O(N) spatial memory allocation for tracking masks.
        """
        # Vectorized generation of the parametric expected baseline
        # Mathematically mapping: Y_hat = Beta_0 + Beta_1 * X_1 + Beta_2 * X_2
        expected_costs = (
            self.model.fixed_base_cost
            + (labor_hours_matrix * self.model.labor_rate_per_hour)
            + (material_units_matrix * self.model.material_rate_per_unit)
        )

        # Calculate localized dollar variance and percentage deviation profiles
        dollar_variance = proposed_costs_vector - expected_costs
        percentage_deviation = dollar_variance / expected_costs

        # Structural Anomaly Mask: Flag where the proposal exceeds both the hard dollar threshold
        # and the allowable percentage tolerance.
        anomaly_flags = (dollar_variance > 50000.0) & (
            percentage_deviation > inflation_tolerance_pct
        )

        return {
            "expected_costs": expected_costs,
            "dollar_variances": dollar_variance,
            "percentage_deviations": percentage_deviation,
            "anomaly_flags": anomaly_flags,
        }


# --- Execution Sandbox ---
if __name__ == "__main__":
    # Define a verified historical baseline cost profile
    historical_baseline = ParametricCostModel(
        fixed_base_cost=10_000.0,  # Fixed structural overhead setup cost
        labor_rate_per_hour=85.0,  # Escalated engineering labor rate
        material_rate_per_unit=12.50,  # Certified material unit cost
    )

    audit_system = ParametricAuditEngine(model=historical_baseline)

    # Simulate an enterprise-scale proposal batch consisting of 1,000,000 line items
    num_proposals = 1_000_000
    np.random.seed(177)  # Deterministic seed allocation

    sim_labor_hours = np.random.uniform(100, 5000, size=num_proposals)
    sim_material_units = np.random.uniform(500, 20000, size=num_proposals)

    # Generate proposed costs containing clean data mixed with systematically inflated anomalies
    base_raw_costs = (
        historical_baseline.fixed_base_cost
        + (sim_labor_hours * historical_baseline.labor_rate_per_hour)
        + (sim_material_units * historical_baseline.material_rate_per_unit)
    )
    # Inject a random inflation modifier between 0.95 and 1.35 across the population
    inflation_modifier = np.random.uniform(0.95, 1.35, size=num_proposals)
    sim_proposed_costs = base_raw_costs * inflation_modifier

    # Execute full population analysis via vectorized audit engine
    results = audit_system.audit_proposal_population(
        proposed_costs_vector=sim_proposed_costs,
        labor_hours_matrix=sim_labor_hours,
        material_units_matrix=sim_material_units,
        inflation_tolerance_pct=0.20,  # 20% systemic tolerance limit
    )

    # Extract targeted data indices using boolean indexing
    flagged_mask = results["anomaly_flags"]
    total_anomalies = np.sum(flagged_mask)
    flagged_indices = np.where(flagged_mask)[0]

    print(
        f"Parametric Verification Complete. Reviewed {num_proposals:,} Cost Line Items."
    )
    print(f"Systemic Cost Inflation Anomalies Isolated: {total_anomalies:,} lines.\n")

    # Print Tabular Audit Trace for the first 5 flagged line items
    print(
        f"{'Item Index':<10} | {'Hours Billed':<12} | {'Units Billed':<12} | {'Proposed Cost':<15} | {'Expected Cost':<15} | {'Over-Pricing':<12}"
    )
    print("-" * 90)

    preview_count = min(5, total_anomalies)
    for i in range(preview_count):
        idx = flagged_indices[i]
        print(
            f"{idx:<10} | "
            f"{sim_labor_hours[idx]:<12,.0f} | "
            f"{sim_material_units[idx]:<12,.0f} | "
            f"${sim_proposed_costs[idx]:<14,.2f} | "
            f"${results['expected_costs'][idx]:<14,.2f} | "
            f"+{results['percentage_deviations'][idx] * 100:<10.1f}%"
        )
