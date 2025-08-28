# src/data_processing.py
import pandas as pd
import numpy as np

def preprocess_data(df: pd.DataFrame):
    df = df.copy()
    df['ds'] = pd.to_datetime(df['ds'])
    df = df.sort_values('ds')
    df['y'] = pd.to_numeric(df['y'], errors='coerce').interpolate('linear')

    # infer frequency (D/W/M)
    inferred = pd.infer_freq(df['ds'])
    df['month'] = df['ds'].dt.month
    df['quarter'] = df['ds'].dt.quarter
    df['dayofweek'] = df['ds'].dt.dayofweek
    df['is_weekend'] = df['dayofweek'].isin([5,6]).astype(int)

    # rolling stats as regressors
    df['rolling_3'] = df['y'].rolling(3, min_periods=1).mean()
    df['rolling_6'] = df['y'].rolling(6, min_periods=1).mean()
    df['lag_1'] = df['y'].shift(1)
    df['lag_3'] = df['y'].shift(3)
    df['lag_6'] = df['y'].shift(6)

    # simple festive proxy (Q4 spikes)
    df['is_festival'] = df['month'].isin([10,11,12]).astype(int)

    df = df.dropna().reset_index(drop=True)
    return df, inferred or 'M'
