import requests
import pandas as pd
from src.config import load_config

config = load_config()
headers = {'Authorization': f'Bearer {config["api_key"]}'}

def get_market_data(symbol, interval):
    endpoint = f'{config["base_url"]}/marketdata/{symbol}/history'
    params = {'interval': interval}
    response = requests.get(endpoint, headers=headers, params=params)
    data = response.json()
    return pd.DataFrame(data)
