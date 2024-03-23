# src/test.py
import unittest
from text import to_upper, to_word_list_isupper

class TestText(unittest.TestCase):

    # Task 1: Check if to_upper returns "ABCDEF" when called with "abcdef"
    def test_to_upper(self):
        result = to_upper("abcdef")
        self.assertEqual(result, "ABCDEF")

    # Task 2: Check if to_word_list_isupper returns True when called with ['I', 'LOVE', 'YOU']
    def test_to_word_list_isupper_true(self):
        result = to_word_list_isupper(['I', 'LOVE', 'YOU'])
        self.assertTrue(result)

    # Task 3: Check if to_word_list_isupper returns False when called with ['i', 'LOVE', 'YOU']
    def test_to_word_list_isupper_false(self):
        result = to_word_list_isupper(['i', 'LOVE', 'YOU'])
        self.assertFalse(result)

    # Task 4: Check if to_upper raises a TypeError if called with a non-string argument
    def test_to_upper_type_error(self):
        with self.assertRaises(TypeError):
            to_upper(123)  # Passing an integer should raise a TypeError

    # Task 5: Check if to_word_list_isupper raises a TypeError if called with a non-list argument
    def test_to_word_list_isupper_type_error(self):
        with self.assertRaises(TypeError):
            to_word_list_isupper("This is not a list")  # This should now raise a TypeError

if __name__ == '__main__':
    unittest.main()

# Output:

# dci-student  src  ➜ ( main)  ♥ 14:02  python3 -m unittest -v
# test_to_upper (test.TestText.test_to_upper) ... ok
# test_to_upper_type_error (test.TestText.test_to_upper_type_error) ... ok
# test_to_word_list_isupper_false (test.TestText.test_to_word_list_isupper_false) ... ok
# test_to_word_list_isupper_true (test.TestText.test_to_word_list_isupper_true) ... ok
# test_to_word_list_isupper_type_error (test.TestText.test_to_word_list_isupper_type_error) ... ok

# ----------------------------------------------------------------------
# Ran 5 tests in 0.000s

# OK
