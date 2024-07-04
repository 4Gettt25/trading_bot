from src.trade_executor.py import execute_trade

def manage_risk(current_price, buy_price, stop_loss_percentage, take_profit_percentage, position_size):
    if current_price <= buy_price * (1 - stop_loss_percentage):
        execute_trade(-1, current_price, position_size)
    elif current_price >= buy_price * (1 + take_profit_percentage):
        execute_trade(-1, current_price, position_size)
