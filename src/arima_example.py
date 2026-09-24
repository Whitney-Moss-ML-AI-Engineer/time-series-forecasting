"""ARIMA example using statsmodels."""
from statsmodels.tsa.arima.model import ARIMA
def fit_arima(series,order=(1,1,1),steps=7):
    model=ARIMA(series,order=order).fit()
    return model,model.forecast(steps=steps)
