import unittest
from app import rnd, max_num_in_list

class TestApp(unittest.TestCase):

    def test_rnd_correct_value(self):
        # Note: Testing randomized functions may not guarantee consistent results.
        # The test may pass sometimes and fail at other times due to randomization.
        result = rnd(2, 20)
        self.assertIn(result, range(2, 21), 'Returned value is not within the expected range')

    def test_rnd_no_out_of_range_value(self):
        # Note: Testing randomized functions may not guarantee consistent results.
        # The test may pass sometimes and fail at other times due to randomization.
        result = rnd(2, 20)
        self.assertGreaterEqual(result, 2, 'Returned value is less than the lower bound')
        self.assertLessEqual(result, 20, 'Returned value is greater than the upper bound')

    def test_max_num_in_list(self):
        self.assertEqual(max_num_in_list([2, 6, 8, 7, -1]), 8, 'Returned value is not the greatest value in max_num_in_list')

if __name__ == '__main__':
    unittest.main()

# output:
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s

# OK