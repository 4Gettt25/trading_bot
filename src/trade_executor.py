import requests
from src.config import load_config
from src.logger import setup_logger

config = load_config()
headers = {'Authorization': f'Bearer {config["api_key"]}'}
logger = setup_logger()

def execute_trade(signal, price, position_size):
    order = {
        'symbol': config['symbol'],
        'quantity': position_size,
        'side': 'buy' if signal == 1 else 'sell',
        'type': 'market',
        'time_in_force': 'gtc'
    }
    try:
        response = requests.post(f'{config["base_url"]}/orders', headers=headers, json=order)
        logger.info(f'Order placed: {response.json()}')
    except Exception as e:
        logger.error(f'Error executing trade: {e}')
