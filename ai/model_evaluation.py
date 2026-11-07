def interpret_regression_metrics(m): return f"MAE={m['mae']:.2f}; R²={m['r2']:.3f}. Validate on a time-based/external holdout before operational use."
