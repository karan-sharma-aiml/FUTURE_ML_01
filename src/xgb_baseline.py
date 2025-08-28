# src/xgb_baseline.py
import numpy as np
import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
import shap

def make_lag_features(df: pd.DataFrame, max_lag: int = 12) -> pd.DataFrame:
    """
    Create lag features for time series forecasting using XGBoost.
    Adds lag_1, lag_2, ... lag_max_lag columns.
    """
    df = df.copy()
    for l in range(1, max_lag + 1):
        df[f'lag_{l}'] = df['y'].shift(l)
    # add simple calendar features
    df['month'] = df['ds'].dt.month
    df['dow'] = df['ds'].dt.dayofweek
    return df.dropna()

def train_xgb(df: pd.DataFrame, max_lag: int = 12):
    """
    Train an XGBoost regressor on lag features.
    
    Args:
        df: DataFrame with columns ['ds','y']
        max_lag: number of lag features
    
    Returns:
        model: trained XGBRegressor
        rmse: float, RMSE on holdout set
        explainer, X_test, shap_values: for SHAP explainability
    """
    # make features
    df_feat = make_lag_features(df, max_lag=max_lag)
    X = df_feat.drop(columns=['ds','y'])
    y = df_feat['y']

    # train-test split (80/20)
    split = int(len(df_feat) * 0.8)
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    # define and fit model
    model = XGBRegressor(
        n_estimators=600,
        learning_rate=0.03,
        max_depth=6,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)

    # evaluate
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    # shap explainability
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)

    return model, rmse, (explainer, X_test, shap_values)
