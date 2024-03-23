# test_email_validator.py

import unittest
from email_validator import EmailValidator

class TestEmailValidator(unittest.TestCase):
    def setUp(self):
        self.validator = EmailValidator()

    def test_valid_email(self):
        self.assertTrue(self.validator.is_valid_email("example@example.com"))

    def test_invalid_email_missing_at(self):
        self.assertFalse(self.validator.is_valid_email("example.com"))

    def test_invalid_email_missing_dot(self):
        self.assertFalse(self.validator.is_valid_email("example@examplecom"))

    def test_invalid_email_special_characters(self):
        self.assertFalse(self.validator.is_valid_email("ex@ample#example.com"))

    def test_invalid_email_multiple_at_symbols(self):
        self.assertFalse(self.validator.is_valid_email("ex@ample@example.com"))

    def test_valid_email_with_subdomain(self):
        self.assertTrue(self.validator.is_valid_email("user@sub.example.com"))

    def test_valid_email_with_underscore(self):
        self.assertTrue(self.validator.is_valid_email("user_name@example.com"))

    def test_valid_email_with_numbers(self):
        self.assertTrue(self.validator.is_valid_email("user123@example.com"))

    def test_valid_email_with_hyphen(self):
        self.assertTrue(self.validator.is_valid_email("user-name@example.com"))

if __name__ == '__main__':
    unittest.main()


# # OUTPUT:
# dci-student  Exercise1  ➜ ( main)  ♥ 15:18  python3 -m unittest -v
# test_invalid_email_missing_at (test_email_validator.TestEmailValidator.test_invalid_email_missing_at) ... ok
# test_invalid_email_missing_dot (test_email_validator.TestEmailValidator.test_invalid_email_missing_dot) ... ok
# test_invalid_email_multiple_at_symbols (test_email_validator.TestEmailValidator.test_invalid_email_multiple_at_symbols) ... ok
# test_invalid_email_special_characters (test_email_validator.TestEmailValidator.test_invalid_email_special_characters) ... ok
# test_valid_email (test_email_validator.TestEmailValidator.test_valid_email) ... ok
# test_valid_email_with_hyphen (test_email_validator.TestEmailValidator.test_valid_email_with_hyphen) ... ok
# test_valid_email_with_numbers (test_email_validator.TestEmailValidator.test_valid_email_with_numbers) ... ok
# test_valid_email_with_subdomain (test_email_validator.TestEmailValidator.test_valid_email_with_subdomain) ... ok
# test_valid_email_with_underscore (test_email_validator.TestEmailValidator.test_valid_email_with_underscore) ... ok

# ----------------------------------------------------------------------
# Ran 9 tests in 0.001s

# OK