"""Simple forecasting baselines."""
import numpy as np
def naive_forecast(series,horizon=1): return np.repeat(series.iloc[-1],horizon)
def seasonal_naive(series,season_length,horizon=1): return np.resize(series.iloc[-season_length:].to_numpy(),horizon)
