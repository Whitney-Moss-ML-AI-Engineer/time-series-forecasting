"""Convenience ARIMA example."""
from statsmodels.tsa.arima.model import ARIMA
def forecast_arima(series,order=(1,1,1),horizon=7):
    fitted=ARIMA(series,order=order).fit()
    return fitted.forecast(horizon)
