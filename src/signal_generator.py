import numpy as np

def generate_signals(data, short_ma_window):
    data['Signal'] = 0
    data['Signal'][short_ma_window:] = np.where(data['SMA50'][short_ma_window:] > data['SMA200'][short_ma_window:], 1, 0)
    data['Position'] = data['Signal'].diff()
    return data
