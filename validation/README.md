# Temporal Validation

Preferred methods:
- Expanding window
- Rolling window
- Walk-forward validation
- TimeSeriesSplit

Example:

Train [======] → Validate [==] → Forecast [→]
Move window → Retrain → Forecast

Never use future observations to construct training features.
