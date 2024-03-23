# test_string_utils.py

import unittest
from string_utils import reverse_string, count_vowels, capitalize_first_letter

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")  # Test reversing a string

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)  # Test counting vowels in a string
        self.assertEqual(count_vowels("world"), 1)  # Test counting vowels in a different string
        self.assertEqual(count_vowels("Python"), 1)  # Test counting vowels in a string with capital letters
        self.assertEqual(count_vowels("12345"), 0)  # Test counting vowels in a string with no vowels

    def test_capitalize_first_letter(self):
        self.assertEqual(capitalize_first_letter("hello world"), "Hello world")  # Test capitalizing first letter
        self.assertEqual(capitalize_first_letter("a sentence."), "A sentence.")  # Test capitalizing first letter of a sentence
        self.assertEqual(capitalize_first_letter("12345"), "12345")  # Test capitalizing first letter of a string with no letters

if __name__ == '__main__':
    unittest.main()

# OUTPUT:

# dci-student  Exercise2  ➜ ( main)  ♥ 15:26  python3 -m unittest -v
# test_capitalize_first_letter (test_string_utils.TestStringUtils.test_capitalize_first_letter) ... ok
# test_count_vowels (test_string_utils.TestStringUtils.test_count_vowels) ... ok
# test_reverse_string (test_string_utils.TestStringUtils.test_reverse_string) ... ok

# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s

# OK