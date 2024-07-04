import unittest
import pandas as pd
from src.indicators import calculate_indicators

class TestIndicators(unittest.TestCase):
    def test_calculate_indicators(self):
        data = pd.DataFrame({'close': [1, 2, 3, 4, 5]})
        data = calculate_indicators(data, 2, 3, 1)
        self.assertIn('SMA50', data.columns)
        self.assertIn('SMA200', data.columns)
        self.assertIn('RSI', data.columns)

if __name__ == '__main__':
    unittest.main()
