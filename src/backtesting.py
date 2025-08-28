# src/backtesting.py
import numpy as np
import pandas as pd
from typing import Callable, Dict, List, Tuple
from sklearn.metrics import mean_absolute_error, mean_squared_error

def _mape(y_true, y_pred):
    eps = 1e-9
    return np.mean(np.abs((y_true - y_pred) / (np.abs(y_true) + eps))) * 100

def _smape(y_true, y_pred):
    eps = 1e-9
    return 100 * np.mean(2 * np.abs(y_pred - y_true) / (np.abs(y_true) + np.abs(y_pred) + eps))

def coverage(y_true, lower, upper):
    return np.mean((y_true >= lower) & (y_true <= upper)) * 100

def rolling_origin_backtest(
    df: pd.DataFrame,
    horizon: int,
    initial: int,
    step: int,
    fit_func: Callable[[pd.DataFrame], Dict],
    predict_func: Callable[[Dict, pd.DatetimeIndex], pd.DataFrame],
    has_interval: bool = True,
) -> pd.DataFrame:
    """
    df: must contain ['ds','y'] sorted by ds
    fit_func: returns a model state dict
    predict_func: given state + future dates -> DataFrame with columns ['ds','yhat', 'yhat_lower','yhat_upper'] if has_interval else without bounds
    """
    df = df.sort_values('ds').copy()
    n = len(df)
    rows = []
    start = initial
    while start + horizon <= n:
        train = df.iloc[:start].copy()
        test = df.iloc[start:start+horizon].copy()
        state = fit_func(train)
        future_idx = test['ds']
        pred = predict_func(state, future_idx)

        merged = test[['ds','y']].merge(pred, on='ds', how='left')
        mae = mean_absolute_error(merged['y'], merged['yhat'])
        rmse = mean_squared_error(merged['y'], merged['yhat'], squared=False)
        mape = _mape(merged['y'].values, merged['yhat'].values)
        smape = _smape(merged['y'].values, merged['yhat'].values)
        cov = coverage(merged['y'], merged.get('yhat_lower', merged['yhat']),
                       merged.get('yhat_upper', merged['yhat'])) if has_interval else np.nan

        rows.append({
            'fold_end': future_idx.max(),
            'MAE': mae, 'RMSE': rmse, 'MAPE': mape, 'sMAPE': smape, 'Coverage%': cov
        })
        start += step
    return pd.DataFrame(rows)
