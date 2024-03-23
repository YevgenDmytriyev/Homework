# test_date_utils.py

import unittest
from date_utils import get_future_date, is_weekend
from datetime import datetime, timedelta

class TestDateUtils(unittest.TestCase):
    def test_get_future_date(self):
        # Test get_future_date function
        current_date = datetime(2023, 9, 26)  # September 26, 2023
        future_date = get_future_date(current_date, 5)  # Adding 5 days
        expected_date = datetime(2023, 10, 1)  # October 1, 2023
        self.assertEqual(future_date, expected_date)

    def test_is_weekend(self):
        # Test is_weekend function
        weekend_date = datetime(2023, 9, 30)  # September 30, 2023 (Saturday)
        weekday_date = datetime(2023, 9, 28)  # September 28, 2023 (Thursday)
        
        self.assertTrue(is_weekend(weekend_date))  # Saturday is a weekend
        self.assertFalse(is_weekend(weekday_date))  # Thursday is not a weekend

if __name__ == '__main__':
    unittest.main()

# OUTPUT:

# dci-student  Exercise5  ➜ ( main)  ♥ 15:46  python3 -m unittest -v
# test_get_future_date (test_date_utils.TestDateUtils.test_get_future_date) ... ok
# test_is_weekend (test_date_utils.TestDateUtils.test_is_weekend) ... ok

# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK