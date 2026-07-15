"""
Parametric Cost Ingestion & Audit Pipeline.
Engineered with Python 3.11+ compliance, Pandas Streaming Ingestion,
and Vectorized NumPy State-Space Calculations.
"""

import os
from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class ParametricCostModel:
    """
    Stores immutable configuration baselines for the cost validation parameters.
    Expected Cost = Fixed Base + (Hours * Labor Rate) + (Units * Material Rate)
    """

    fixed_base_cost: float
    labor_rate_per_hour: float
    material_rate_per_unit: float


class StreamingParametricAuditEngine:
    def __init__(self, model: ParametricCostModel) -> None:
        self.model = model

    def audit_csv_data_stream(
        self,
        file_path: str,
        chunk_size: int = 50_000,
        inflation_tolerance_pct: float = 0.20,
    ) -> dict[str, int | float | list[int]]:
        """
        Streams records from disk, strips associative metadata, and runs parallel calculations.

        Time Complexity: O(N) linear time driven by disk I/O and vector processing.
        Space Complexity: O(1) constant memory profile relative to total file size.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"Target audit source file not found at: {file_path}"
            )

        total_records_reviewed = 0
        total_anomalies_isolated = 0
        flagged_ledger_indices: list[int] = []
        total_unadjusted_overpricing_dollar = 0.0

        # Enforce O(1) Space Complexity by instantiating an engine-level data iterator
        # This prevents loading the whole file into RAM at once
        data_streamer = pd.read_csv(file_path, chunksize=chunk_size)

        for chunk_idx, frame in enumerate(data_streamer):
            # --- State-Space Restructuring Boundary ---
            # Extract row tracking markers from the Pandas index
            base_row_offsets = frame["row_id"].to_numpy()

            # Collapse the high-overhead Pandas tabular objects into pure linear NumPy vector spaces
            proposed_costs = frame["proposed_cost"].to_numpy()
            labor_hours = frame["labor_hours"].to_numpy()
            material_units = frame["material_units"].to_numpy()

            # Execute parallelized SIMD calculation across the isolated buffer
            expected_costs = (
                self.model.fixed_base_cost
                + (labor_hours * self.model.labor_rate_per_hour)
                + (material_units * self.model.material_rate_per_unit)
            )

            dollar_variance = proposed_costs - expected_costs
            percentage_deviation = dollar_variance / expected_costs

            # Construct the Boolean Anomaly Exception Mask
            anomaly_mask = (dollar_variance > 50000.0) & (
                percentage_deviation > inflation_tolerance_pct
            )

            # Accumulate running metrics metrics out of the vector block
            chunk_anomalies = np.sum(anomaly_mask)
            total_anomalies_isolated += chunk_anomalies
            total_records_reviewed += len(frame)
            total_unadjusted_overpricing_dollar += float(
                np.sum(dollar_variance[anomaly_mask])
            )

            # Capture actual ledger index positions that triggered the violation mask
            if chunk_anomalies > 0:
                flagged_ledger_indices.extend(
                    base_row_offsets[anomaly_mask].astype(int).tolist()
                )

            # Print an operational trace for the first chunk to show runtime execution
            if chunk_idx == 0 and chunk_anomalies > 0:
                print(
                    f"[Chunk 0 Ingestion Trace] Analyzed {len(frame):,} rows. Isolated {chunk_anomalies:,} anomalies."
                )

        return {
            "total_reviewed": total_records_reviewed,
            "total_anomalies": total_anomalies_isolated,
            "total_padded_exposure": total_unadjusted_overpricing_dollar,
            "flagged_rows": flagged_ledger_indices,
        }


# --- Environment Setup Helper ---
def generate_synthetic_csv(file_path: str, num_rows: int = 200_000) -> None:
    """Generates a structured CSV data asset on disk to simulate a corporate audit ledger."""
    print(f"Creating local data asset: {file_path} ({num_rows:,} records)...")
    np.random.seed(42)

    hours = np.random.uniform(50, 4000, size=num_rows)
    materials = np.random.uniform(100, 15000, size=num_rows)

    # Fundamental baseline: Cost = 10000 + 85*Hours + 12.5*Materials
    base_costs = 10000.0 + (hours * 85.0) + (materials * 12.50)
    # Inject deliberate pricing inflation modifiers
    inflation_vector = np.random.choice(
        [1.0, 1.05, 1.32], size=num_rows, p=[0.70, 0.20, 0.10]
    )
    proposed_costs = base_costs * inflation_vector

    df = pd.DataFrame(
        {
            "row_id": np.arange(num_rows),
            "labor_hours": hours,
            "material_units": materials,
            "proposed_cost": proposed_costs,
        }
    )
    df.to_csv(file_path, index=False)
    print("Data asset successfully written to disk.\n")


# --- Execution Sandbox ---
if __name__ == "__main__":
    target_csv = "contractor_proposals.csv"

    # 1. Enforce local environment requirements
    if not os.path.exists(target_csv):
        generate_synthetic_csv(target_csv, num_rows=250_000)

    # 2. Instantiate verified cost parameters
    government_baseline = ParametricCostModel(
        fixed_base_cost=10000.0, labor_rate_per_hour=85.0, material_rate_per_unit=12.50
    )

    audit_engine = StreamingParametricAuditEngine(model=government_baseline)

    # 3. Stream and audit the flat file asset
    print(f"Opening data stream connection to: {target_csv}")
    audit_summary = audit_engine.audit_csv_data_stream(
        file_path=target_csv,
        chunk_size=50000,  # The processing allocation window size
        inflation_tolerance_pct=0.20,
    )

    # 4. Present System Summary Report
    print(
        f"Total Ledger Population Ingested : {audit_summary['total_reviewed']:,} items"
    )
    print(
        f"Parametric Anomalies Isolated    : {audit_summary['total_anomalies']:,} items"
    )
    print(
        f"Total Unadjusted Cost Exposure   : ${audit_summary['total_padded_exposure']:,.2f}"
    )
    print(
        f"Calculated Leakage Ratio        : {(audit_summary['total_anomalies'] / audit_summary['total_reviewed']) * 100:.2f}%"
    )
    print(f"Sample Anomaly Row Indexes       : {audit_summary['flagged_rows'][:10]}...")
