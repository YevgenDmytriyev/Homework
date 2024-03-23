# test_factorial.py

import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_0(self):
        result = factorial(0)
        self.assertEqual(result, 1)  # 0! is defined as 1

    def test_factorial_1(self):
        result = factorial(1)
        self.assertEqual(result, 1)  # 1! is 1

    def test_factorial_5(self):
        result = factorial(5)
        self.assertEqual(result, 120)  # 5! is 120

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)  # Factorial of a negative number should raise a ValueError

    def test_factorial_large_number(self):
        result = factorial(10)
        self.assertEqual(result, 3628800)  # 10! is 3628800

    def test_the_output_instance_is_int(self):
        result = factorial(3)
        self.assertIsInstance(result, int)  # Ensure that the output is an integer

if __name__ == '__main__':
    unittest.main()


# OUTPUT:

# dci-student  Exercise4  ➜ ( main)  ♥ 15:43  python3 -m unittest -v
# test_factorial_0 (test_factorial.TestFactorial.test_factorial_0) ... ok
# test_factorial_1 (test_factorial.TestFactorial.test_factorial_1) ... ok
# test_factorial_5 (test_factorial.TestFactorial.test_factorial_5) ... ok
# test_factorial_large_number (test_factorial.TestFactorial.test_factorial_large_number) ... ok
# test_factorial_negative (test_factorial.TestFactorial.test_factorial_negative) ... ok
# test_the_output_instance_is_int (test_factorial.TestFactorial.test_the_output_instance_is_int) ... ok

# ----------------------------------------------------------------------
# Ran 6 tests in 0.000s

# OK