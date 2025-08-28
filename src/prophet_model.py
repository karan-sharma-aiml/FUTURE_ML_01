from prophet import Prophet
import pandas as pd

def fit_prophet(train: pd.DataFrame,
                seasonality_mode="multiplicative",
                changepoint_prior_scale=0.5):
    m = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False,
        seasonality_mode=seasonality_mode,
        changepoint_prior_scale=changepoint_prior_scale,
        interval_width=0.9,
        uncertainty_samples=1000    # Ye kaafi important hai confidence intervals ke liye
    )
    # India ke holidays add karne ki koshish
    try:
        m.add_country_holidays(country_name='IN')
    except Exception:
        pass

    # Optional regressors jo future predict karne me madad karte hain
    for reg in ['is_weekend','is_festival','rolling_3','rolling_6']:
        if reg in train.columns:
            m.add_regressor(reg)

    # Model ko fit karo data ke sath jisme 'ds', 'y' columns hona chahiye
    m.fit(train[['ds', 'y'] + [c for c in train.columns if c not in ['ds', 'y']]])
    return m

def prophet_predict(m, future_df: pd.DataFrame):
    fcst = m.predict(future_df)
    # Ye extensions forecast dataframe me important columns ko include karta hai,
    # taki streamlit me components plot karne par errors naa aayein
    expected_cols = ['ds', 'yhat', 'yhat_lower', 'yhat_upper', 'trend', 'trend_lower', 'trend_upper', 'yearly', 'weekly']
    # Sirf available columns return karo
    return fcst[[c for c in expected_cols if c in fcst.columns]]

def train_prophet_full(df: pd.DataFrame, periods=6, freq='M', **kwargs):
    # Model ko train karo
    m = fit_prophet(df, **kwargs)
    # Future dataframe banayo, jis me history bhi included ho
    future = m.make_future_dataframe(periods=periods, freq=freq, include_history=True)
    # Regressors ke future values fill karo, agar present hain toh
    for reg in ['is_weekend','is_festival','rolling_3','rolling_6']:
        if reg in df.columns:
            future[reg] = df[reg].reindex(future.index, method='ffill')
    # Forecast predict karo enough columns ke sath
    forecast = prophet_predict(m, future)
    return m, forecast
