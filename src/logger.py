import logging

def setup_logger():
    logger = logging.getLogger('trading_bot')
    handler = logging.FileHandler('logs/trading_bot.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
