"""
Risk Architecture module for Value-at-Risk (VaR) and advanced metric modeling.
Implements Parametric and Stochastic Monte Carlo simulation frameworks.
"""

import numpy as np
import scipy.stats as stats


class ValueAtRiskEngine:
    """
    Computes portfolio-level down-side risk metrics across parametric
    and stochastic simulation state spaces.
    """

    def __init__(self, returns: np.ndarray) -> None:
        self.returns = np.asarray(returns)
        self.mean = np.mean(self.returns)
        self.std = np.std(self.returns)

    def compute_parametric_var(self, confidence_level: float = 0.95) -> float:
        """
        Calculates Parametric (Delta-Normal) Value-at-Risk.
        Assumes a symmetric normal distribution.

        Complexity: O(1) mathematical execution profile.
        """
        # Calculate the inverse cumulative distribution function (PPF)
        z_score = stats.norm.ppf(confidence_level)
        parametric_var = -(self.mean + z_score * self.std)
        return float(parametric_var)

    def compute_monte_carlo_var(
        self,
        current_volatility: float,
        confidence_level: float = 0.95,
        n_simulations: int = 10_000,
    ) -> float:
        """
        Calculates Stochastic Monte Carlo Value-at-Risk.
        Generates N forward-looking simulated paths using the current conditional volatility state.

        Complexity: O(n) memory/time profile relative to n_simulations.
        """
        rng = np.random.default_rng(seed=42)

        # Simulate forward asset shocks using random normal distributions
        simulated_shocks = rng.normal(0, 1, n_simulations)

        # Project forward paths utilizing our calculated conditional volatility step
        simulated_returns = self.mean + simulated_shocks * current_volatility

        # Isolate the worst-case quantile breakpoint in the lower tail
        monte_carlo_var = -np.percentile(
            simulated_returns, (1 - confidence_level) * 100
        )
        return float(monte_carlo_var)
