from ta import trend, momentum

def calculate_indicators(data, short_ma_window, long_ma_window, rsi_window):
    data['SMA50'] = trend.sma_indicator(data['close'], window=short_ma_window)
    data['SMA200'] = trend.sma_indicator(data['close'], window=long_ma_window)
    data['RSI'] = momentum.rsi(data['close'], window=rsi_window)
    return data
