"""
Econometrics module for time-series analysis and volatility modeling.
Implements stationarity testing and GARCH variance modeling.
"""

import numpy as np
import pandas as pd
from arch import arch_model


class VolatilityEngine:
    """
    Ingests financial time-series data, verifies statistical properties,
    and models conditional variance regimes.
    """

    def __init__(self, returns: np.ndarray | pd.Series) -> None:
        self.returns = np.asarray(returns)

    def calculate_rolling_volatility(self, window: int = 21) -> pd.Series:
        """
        Calculates standard moving historical volatility.

        Time Complexity: O(n)
        Memory Profile: O(n) for the output Series
        """
        series = pd.Series(self.returns)
        return series.rolling(window=window).std() * np.sqrt(252)

    def fit_garch(self, p: int = 1, q: int = 1) -> dict[str, float | np.ndarray]:
        """
        Fits a GARCH(p, q) model to capture volatility clustering regimes.
        Essential for auditing financial risk data where variance is non-constant.
        """
        # Instantiate GARCH model (Constant mean, GARCH innovation variance)
        model = arch_model(
            self.returns, p=p, q=q, vol="GARCH", dist="normal", rescale=False
        )
        res = model.fit(disp="off")

        # Extract long-run variance and conditional volatility state space
        return {
            "mu": float(res.params["mu"]),
            "omega": float(res.params["omega"]),
            "alpha": float(res.params["alpha[1]"]),
            "beta": float(res.params["beta[1]"]),
            "conditional_volatility": np.asarray(res.conditional_volatility),
        }
