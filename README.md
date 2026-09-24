# Time-Series Forecasting Laboratory

A reproducible forecasting portfolio for statistical, machine-learning, and deep-learning models applied to temporal data.

## Core Workflow

**Business Question → Time Index → Data Quality → Exploratory Time-Series Analysis → Baseline → Statistical Model → Machine Learning Model → Deep Learning Model → Backtesting → Forecast Evaluation → Error Analysis → Uncertainty → Operational Decision**

The central rule is simple:

> **Time must remain in the correct order.**

Forecasting experiments should avoid future information leaking into model training or feature construction.

## Forecasting Horizons

Models can be evaluated across:

| Horizon | Example Application |
|---|---|
| 1 day | Short-term demand, price, risk |
| 1 week | Tactical planning |
| 1 month | Monthly planning |
| Quarterly | Business planning |
| 1 year | Strategic forecasting |
| 3 years | Long-range scenarios |
| 5 years | Strategic capacity planning |
| 10 years | Long-range scenario analysis |

Long-horizon forecasts should be treated as model-based scenarios with uncertainty, not guaranteed outcomes.

## Model Families

### Statistical
- Naive forecast
- Seasonal naive
- Moving average
- Exponential smoothing
- Simple exponential smoothing
- Holt
- Holt-Winters
- AR
- MA
- ARMA
- ARIMA
- SARIMA
- SARIMAX
- VAR
- State-space models

### Volatility
- Historical volatility
- ARCH
- GARCH
- EGARCH
- GJR-GARCH

### Machine Learning
- Linear regression
- Ridge
- LASSO
- Random Forest
- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost

### Deep Learning
- RNN
- LSTM
- GRU
- CNN-LSTM
- Temporal Convolutional Network
- Transformer
- Temporal Fusion Transformer concepts

## Time-Series Components

A time series may contain:

- **Trend** — long-term direction
- **Seasonality** — repeating pattern
- **Cycle** — broader recurring movement
- **Level** — baseline value
- **Noise** — unpredictable variation
- **Autocorrelation** — relationship with previous observations

A common decomposition is:

**Observed = Trend + Seasonality + Residual**

For multiplicative processes:

**Observed = Trend × Seasonality × Residual**

## Forecast Evaluation

### Regression Metrics

- MAE
- MSE
- RMSE
- MAPE
- sMAPE
- MASE
- R² where appropriate

### Financial/Risk Metrics

- Directional accuracy
- Volatility forecast error
- VaR exceedance rate
- CVaR error
- Maximum drawdown
- Sharpe ratio when evaluating a defined strategy

### Forecast Uncertainty

Where appropriate, report:
- Prediction intervals
- Confidence intervals
- Quantile forecasts
- Bootstrap intervals
- Monte Carlo intervals

## Validation Strategy

Do not randomly shuffle temporal observations for ordinary forecasting evaluation.

Preferred methods:
- Expanding-window validation
- Rolling-window validation
- Walk-forward validation
- TimeSeriesSplit
- Out-of-sample testing

Example:

**Train → Validate → Forecast → Move Window → Retrain → Forecast**

## Leakage Controls

Explicitly test for:

- Future target leakage
- Future feature leakage
- Improper normalization
- Look-ahead bias
- Overlapping labels
- Incorrect lag construction
- Data revision leakage
- Survivorship bias where financial data is used

## Feature Engineering

Examples:
- Lag variables
- Rolling mean
- Rolling median
- Rolling standard deviation
- Exponential moving average
- Momentum
- Rate of change
- Calendar features
- Seasonal indicators
- Volatility
- Difference transformations
- Log transformations
- Fourier/seasonal features

## Research Questions

1. How does forecasting accuracy change as the prediction horizon increases?
2. When does ARIMA outperform machine-learning models?
3. When does GARCH provide useful volatility information?
4. Can LSTM models improve over statistical baselines?
5. Do Transformers improve long-range temporal dependencies?
6. How does model performance change under regime shifts?
7. How much does feature engineering contribute relative to architecture changes?

## Technology Stack

Python, NumPy, Pandas, SciPy, statsmodels, arch, scikit-learn, XGBoost, LightGBM, CatBoost, PyTorch, TensorFlow/Keras, Matplotlib, Plotly, Optuna, MLflow, Jupyter, Google Colab.

## Repository Structure

| Directory | Purpose |
|---|---|
| data/ | Dataset documentation |
| preprocessing/ | Temporal cleaning and transformations |
| baselines/ | Naive and benchmark forecasts |
| statistical_models/ | Classical time-series models |
| volatility/ | Volatility models |
| machine_learning/ | ML forecasting |
| deep_learning/ | RNN/LSTM/GRU/Transformer models |
| feature_engineering/ | Temporal feature construction |
| validation/ | Walk-forward and rolling validation |
| evaluation/ | Forecast metrics |
| uncertainty/ | Prediction intervals |
| experiments/ | Controlled research |
| notebooks/ | Reproducible notebooks |
| src/ | Reusable code |
| tests/ | Automated tests |
| reports/ | Research reports |
| visualizations/ | Forecast figures |

## Research Standard

Every forecasting experiment should document:

- Forecast target
- Frequency
- Forecast horizon
- Data range
- Feature availability date
- Train/validation/test periods
- Baseline
- Model
- Hyperparameters
- Validation method
- Metrics
- Prediction intervals
- Error analysis
- Computational cost
- Limitations
- Reproducibility

## Author

**Whitney Moss** — Machine Learning Engineer | AI & Data Analyst | Data Scientist
