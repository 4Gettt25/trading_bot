import pandas as pd
from src.indicators import calculate_indicators
from src.signal_generator import generate_signals

def backtest_strategy(data, short_ma_window, long_ma_window, rsi_window):
    data = calculate_indicators(data, short_ma_window, long_ma_window, rsi_window)
    data = generate_signals(data, short_ma_window)
    # Implement backtesting logic to calculate returns based on generated signals
    # This can include calculating total returns, Sharpe ratio, drawdown, etc.
    return data
