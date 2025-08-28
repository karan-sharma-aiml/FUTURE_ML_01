import warnings
warnings.filterwarnings("ignore")

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

from src.data_processing import preprocess_data
from src.prophet_model import train_prophet_full
from src.lstm_model import train_lstm, forecast_lstm
from src.backtesting import rolling_origin_backtest
from src.utils import evaluate
from src.xgb_baseline import train_xgb
import shap

st.set_page_config(page_title="Sales Forecasting Pro", layout="wide")
st.title("🚀 AI-Powered Sales Forecasting Dashboard — Advanced")


# Helpers & Caching
@st.cache_data
def load_csv(file):
    return pd.read_csv(file)

@st.cache_data
def prep(df):
    return preprocess_data(df)

# Sidebar Controls
with st.sidebar:
    st.header("⚙ Settings")
    uploaded = st.file_uploader("CSV with columns: ds,y", type="csv")
    horizon = st.number_input("Forecast Horizon", 3, 36, 12, step=1)
    n_lags = st.number_input("LSTM Lags", 6, 48, 12, step=1)
    epochs = st.number_input("LSTM Epochs", 50, 500, 200, step=10)
    cp_scale = st.slider("Prophet changepoint_prior_scale", 0.01, 1.0, 0.5, 0.01)
    do_cv = st.checkbox("Run rolling backtest (Prophet)", value=True)
    initial = st.number_input("CV initial window (rows)", 12, 2000, 36, step=1)
    step = st.number_input("CV step", 1, 24, 3, step=1)

# Load Data
if uploaded:
    raw = load_csv(uploaded)
else:
    st.info("Using sample dataset: data/sample_sales.csv")
    raw = pd.read_csv("data/sample_sales.csv")

df, inferred_freq = prep(raw)

df['ds'] = pd.to_datetime(df['ds'])
df = df.sort_values('ds').reset_index(drop=True)

st.write(f"*Detected frequency*: {inferred_freq} | Rows: {len(df)}")

st.subheader("🔍 Preview")
st.dataframe(df.head())

# Prophet Forecast
st.subheader("🔮 Prophet Forecast")
prophet_model, forecast = train_prophet_full(df, periods=horizon, freq=inferred_freq, changepoint_prior_scale=cp_scale)

fig1 = px.line(forecast, x="ds", y="yhat", title="Prophet: Forecast & Uncertainty")
fig1.add_scatter(x=df['ds'], y=df['y'], mode="lines", name="Actual")

if 'yhat_lower' in forecast.columns and 'yhat_upper' in forecast.columns:
    fig1.add_scatter(x=forecast['ds'], y=forecast['yhat_lower'], mode="lines", name="Lower", line=dict(dash='dot'))
    fig1.add_scatter(x=forecast['ds'], y=forecast['yhat_upper'], mode="lines", name="Upper", line=dict(dash='dot'))

st.plotly_chart(fig1, use_container_width=True)

# In-sample metrics
hist_dates = df['ds'].tail(horizon)
in_sample = forecast[forecast['ds'].isin(hist_dates)]
y_true = df[df['ds'].isin(in_sample['ds'])]['y'].values
y_pred = in_sample['yhat'].values

if len(y_true) > 0 and len(y_true) == len(y_pred):
    mae, rmse, mape_, smape_ = evaluate(y_true, y_pred)
    st.write(f"*Prophet* → MAE: {mae:.2f} | RMSE: {rmse:.2f} | MAPE: {mape_:.2f}% | sMAPE: {smape_:.2f}%")
else:
    st.write("ℹ Not enough overlap to compute in-sample metrics for the chosen horizon.")

# Prophet Components
st.subheader("📉 Prophet Components (Trend & Seasonality)")
try:
    comp_fig = prophet_model.plot_components(forecast)
    st.pyplot(comp_fig)
except KeyError as e:
    st.info("Showing manual trend and yearly seasonality plots")

    import plotly.graph_objects as go

    if 'trend' not in forecast.columns:
        forecast['trend'] = forecast['yhat']

    fig_trend = go.Figure()
    fig_trend.add_trace(go.Scatter(
        x=forecast['ds'],
        y=forecast['trend'],
        mode='lines',
        name='Trend',
        line=dict(color='blue')
    ))
    fig_trend.update_layout(title='Trend Component (approx)', xaxis_title='Date', yaxis_title='Value')
    st.plotly_chart(fig_trend, use_container_width=True)

    if 'yearly' in forecast.columns:
        fig_yearly = go.Figure()
        fig_yearly.add_trace(go.Scatter(
            x=forecast['ds'],
            y=forecast['yearly'],
            mode='lines',
            name='Yearly Seasonality',
            line=dict(color='green')
        ))
        fig_yearly.update_layout(title='Yearly Seasonality', xaxis_title='Date', yaxis_title='Value')
        st.plotly_chart(fig_yearly, use_container_width=True)

# LSTM Forecast
st.subheader("🤖 LSTM Forecast (MC-Dropout Uncertainty)")

series = df['y'].values
lstm_model, scaler = train_lstm(series, n_lags=n_lags, epochs=epochs)
n_lags_adj = min(n_lags, len(df))
last_vals = df['y'].values[-n_lags_adj:]

preds, lo, hi = forecast_lstm(
    lstm_model, scaler, last_vals,
    steps=horizon, n_lags=n_lags_adj, mc_samples=60
)
future_idx = pd.date_range(df['ds'].max(), periods=horizon+1, freq=inferred_freq)[1:]
lstm_df = pd.DataFrame({'ds': future_idx, 'yhat': preds, 'lower': lo, 'upper': hi})

fig2 = px.line(lstm_df, x="ds", y="yhat", title="LSTM Forecast")
fig2.add_scatter(x=df['ds'], y=df['y'], mode="lines", name="Actual")
fig2.add_scatter(x=lstm_df['ds'], y=lstm_df['lower'], mode="lines", name="Lower", line=dict(dash='dot'))
fig2.add_scatter(x=lstm_df['ds'], y=lstm_df['upper'], mode="lines", name="Upper", line=dict(dash='dot'))
st.plotly_chart(fig2, use_container_width=True)

# Combined Forecast
st.subheader("📊 Combined: Prophet vs LSTM (future only)")
future_prophet = forecast[forecast['ds'] > df['ds'].max()].tail(horizon)[['ds','yhat']].rename(columns={'yhat':'Prophet'})
combined = lstm_df.merge(future_prophet, on='ds', how='left')
fig3 = px.line(combined, x="ds", y=["Prophet","yhat"], title="Prophet vs LSTM (future)")
st.plotly_chart(fig3, use_container_width=True)

# ---------- Rolling Backtest (Prophet) ----------
if do_cv:
    st.subheader("🧪 Rolling-Origin Backtest (Prophet)")

    # Defensive input check
    st.write(f"Data rows: {len(df)} | Initial window: {initial} | Step: {step} | Horizon: {horizon}")

    # Ensure initial+step+horizon < len(df), adjust if needed
    valid = True
    if len(df) < (initial + horizon):
        st.warning("Data length is too small for initial window and horizon. Adjust sliders!")
        valid = False

    def fit_func(train_df):
        m, _ = train_prophet_full(train_df, periods=0, freq=inferred_freq, changepoint_prior_scale=cp_scale)
        return {'model': m, 'train': train_df}

    def predict_func(state, future_idx):
        future = pd.DataFrame({'ds': future_idx})
        for reg in ['is_weekend', 'is_festival', 'rolling_3', 'rolling_6']:
            if reg in state['train'].columns:
                future[reg] = state['train'][reg].iloc[-1]
        fc = state['model'].predict(future)
        cols = ['ds', 'yhat']
        if 'yhat_lower' in fc.columns and 'yhat_upper' in fc.columns:
            cols += ['yhat_lower', 'yhat_upper']
        return fc[cols]

    if valid:
        try:
            cvres = rolling_origin_backtest(
                df[['ds', 'y', 'is_weekend', 'is_festival', 'rolling_3', 'rolling_6']],
                horizon=int(min(horizon, 12)),
                initial=int(initial),
                step=int(step),
                fit_func=fit_func,
                predict_func=predict_func,
                has_interval=True
            )
            st.write("CV result preview:")
            st.dataframe(cvres)
            if not cvres.empty and 'MAE' in cvres.columns:
                st.write(
                    "CV Mean → MAE: {:.2f} | RMSE: {:.2f} | MAPE: {:.2f}% | sMAPE: {:.2f}% | Coverage: {:.1f}%".format(
                        cvres['MAE'].mean(), cvres['RMSE'].mean(), cvres['MAPE'].mean(), cvres['sMAPE'].mean(),
                        cvres['Coverage%'].mean()
                    )
                )
            else:
                st.warning("Backtest output empty ya metrics column missing! Initial/step/horizon ko data size ke hisaab se adjust karo.")
        except Exception as e:
            st.warning(f"Backtest skipped: {e}")
    else:
        st.warning("Adjust your initial, horizon and step parameters so they fit your data length!")

   
# XGBoost SHAP
st.subheader("🪄 XGBoost Baseline with SHAP Explainability")
try:
    model, rmse_xgb, (explainer, Xte, shap_values) = train_xgb(df[['ds','y']].copy())
    st.write(f"*XGBoost RMSE (holdout):* {rmse_xgb:.2f}")

    fig_bar = plt.figure(figsize=(8,6))
    shap.summary_plot(shap_values, Xte, plot_type="bar", show=False)
    st.pyplot(fig_bar)
    plt.close(fig_bar)

    fig_bee = plt.figure(figsize=(8,6))
    shap.summary_plot(shap_values, Xte, show=False)
    st.pyplot(fig_bee)
    plt.close(fig_bee)
except Exception as e:
    st.warning(f"XGBoost/SHAP section skipped: {e}")

# Downloads
st.download_button(
    "💾 Download Prophet Forecast CSV",
    forecast[['ds','yhat'] + (['yhat_lower','yhat_upper'] if {'yhat_lower','yhat_upper'}.issubset(forecast.columns) else [])]
        .to_csv(index=False).encode(),
    "prophet_forecast.csv",
    "text/csv"
)
st.download_button(
    "💾 Download LSTM Forecast CSV",
    lstm_df.to_csv(index=False).encode(),
    "lstm_forecast.csv",
    "text/csv"
)
