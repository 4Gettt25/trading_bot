import time
from src.config import load_config
from src.data_fetcher import get_market_data
from src.indicators import calculate_indicators
from src.signal_generator import generate_signals
from src.trade_executor import execute_trade
from src.risk_manager import manage_risk
from src.logger import setup_logger

def main():
    config = load_config()
    logger = setup_logger()
    
    # Initial setup
    position_size = config['position_size']
    buy_price = None
    
    while True:
        try:
            data = get_market_data(config['symbol'], config['interval'])
            data = calculate_indicators(data, config['short_ma_window'], config['long_ma_window'], config['rsi_window'])
            data = generate_signals(data, config['short_ma_window'])

            last_signal = data['Position'].iloc[-1]
            current_price = data['close'].iloc[-1]

            if last_signal == 1 and buy_price is None:
                execute_trade(1, current_price, position_size)
                buy_price = current_price
            elif last_signal == -1 and buy_price is not None:
                execute_trade(-1, current_price, position_size)
                buy_price = None
            elif buy_price is not None:
                manage_risk(current_price, buy_price, config['stop_loss_percentage'], config['take_profit_percentage'], position_size)

            time.sleep(3600)  # Sleep for 1 hour
        except Exception as e:
            logger.error(f'Error in main loop: {e}')
            time.sleep(60)  # Wait for 1 minute before retrying

if __name__ == "__main__":
    main()
