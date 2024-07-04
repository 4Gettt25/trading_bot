import unittest
from src.data_fetcher import get_market_data

class TestDataFetcher(unittest.TestCase):
    def test_get_market_data(self):
        data = get_market_data('AAPL', '1h')
        self.assertFalse(data.empty)
        self.assertIn('close', data.columns)

if __name__ == '__main__':
    unittest.main()
