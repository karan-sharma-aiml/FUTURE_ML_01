import numpy as np
from typing import Tuple
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
import tensorflow as tf

def set_seed(seed=42):
    np.random.seed(seed)
    tf.random.set_seed(seed)

def create_supervised(series: np.ndarray, n_lags=12) -> Tuple[np.ndarray, np.ndarray]:
    X, y = [], []
    for i in range(n_lags, len(series)):
        X.append(series[i-n_lags:i])
        y.append(series[i])
    return np.array(X), np.array(y)

def train_lstm(series, n_lags=12, epochs=200, val_ratio=0.2, seed=42):
    set_seed(seed)
    scaler = MinMaxScaler()
    split = int(len(series) * (1 - val_ratio))
    train_raw, val_raw = series[:split], series[split:]
    scaler.fit(train_raw.reshape(-1,1))
    train = scaler.transform(train_raw.reshape(-1,1)).flatten()
    val = scaler.transform(val_raw.reshape(-1,1)).flatten()

    Xtr, ytr = create_supervised(train, n_lags)
    Xva, yva = create_supervised(np.concatenate([train[-n_lags:], val]), n_lags)
    Xtr = Xtr[..., None]
    Xva = Xva[..., None]

    model = Sequential([
        LSTM(96, activation='tanh', input_shape=(n_lags, 1), return_sequences=True),
        Dropout(0.3),
        LSTM(64, activation='tanh'),
        Dropout(0.3),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    cb = [
        EarlyStopping(monitor='val_loss', patience=15, restore_best_weights=True),
        ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=7)
    ]
    model.fit(Xtr, ytr, epochs=epochs, batch_size=32, validation_data=(Xva, yva), verbose=0, callbacks=cb)
    return model, scaler

def forecast_lstm(model, scaler, history, steps=6, n_lags=12, mc_samples=50):
    scaled_hist = scaler.transform(history.reshape(-1, 1)).flatten().tolist()
    preds_scaled = []
    for _ in range(steps):
        x = np.array(scaled_hist[-n_lags:]).reshape(1, n_lags, 1)
        samples = [model(x, training=True).numpy()[0,0] for _ in range(mc_samples)]
        mean_pred = float(np.mean(samples))
        preds_scaled.append(mean_pred)
        scaled_hist.append(mean_pred)
    preds = scaler.inverse_transform(np.array(preds_scaled).reshape(-1, 1)).flatten()

    lc, uc = [], []
    scaled_hist = scaler.transform(history.reshape(-1, 1)).flatten().tolist()
    for _ in range(steps):
        x = np.array(scaled_hist[-n_lags:]).reshape(1, n_lags, 1)
        samples = [model(x, training=True).numpy()[0,0] for _ in range(mc_samples)]
        lc.append(np.percentile(samples, 5))
        uc.append(np.percentile(samples, 95))
        scaled_hist.append(np.mean(samples))
    lower = scaler.inverse_transform(np.array(lc).reshape(-1, 1)).flatten()
    upper = scaler.inverse_transform(np.array(uc).reshape(-1, 1)).flatten()

    return preds, lower, upper