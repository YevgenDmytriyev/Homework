[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/DER1QznL)
# 26-09-2023-python-testing-unittest-III




# Python Unit Testing Exercises

In this set of exercises, you'll practice unit testing in Python using the `unittest` framework. Each exercise focuses on a different scenario, and you'll use various assertion methods provided by `unittest`.

## Exercise 1: Testing an Email Validator

Imagine you have an `EmailValidator` class that checks the validity of email addresses. Create unit tests for this class using assertions like `assertTrue`, `assertFalse`, and `assertRegex`.

```python
# email_validator.py

import re

class EmailValidator:
    def is_valid_email(self, email):
        # Regular expression for basic email validation
        
```

```python
# test_email_validator.py

import unittest
from email_validator import EmailValidator

class TestEmailValidator(unittest.TestCase):
    def setUp(self):
        

    def test_valid_email(self):
        

    def test_invalid_email_missing_at(self):
        

    def test_invalid_email_missing_dot(self):
        

    def test_invalid_email_special_characters(self):
        

    def test_invalid_email_multiple_at_symbols(self):
        

    def test_valid_email_with_subdomain(self):
        

    def test_valid_email_with_underscore(self):
        

    def test_valid_email_with_numbers(self):
        

    def test_valid_email_with_hyphen(self):
       

if __name__ == '__main__':
    unittest.main()

```

## Exercise 2: Testing a String Manipulation Module

Create unit tests for a module that performs various string manipulations, such as reversing a string, counting the number of vowels, and capitalizing the first letter of a sentence. Use assertion methods like `assertEqual`, `assertTrue`, and `assertIn`.

```python
# string_utils.py

def reverse_string(s):
    # Implement the function

def count_vowels(s):
    # Implement the function

def capitalize_first_letter(s):
    # Implement the function
```

```python
# test_string_utils.py

import unittest
from string_utils import reverse_string, count_vowels, capitalize_first_letter

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        # Add test cases here

    def test_count_vowels(self):
        # Add test cases here

    def test_capitalize_first_letter(self):
        # Add test cases here

if __name__ == '__main__':
    unittest.main()
```

## Exercise 3: Testing a File Reader Class

Create unit tests for a class that reads and processes data from a file using assertions like `assertIsNone`, `assertIsNotNone`, and `assertIsInstance`.

```python
# file_reader.py

class FileReader:
    def __init__(self, file_path):
        # Implement the constructor

    def read_file(self):
        # Implement the method
```

```python
# test_file_reader.py

import unittest
from file_reader import FileReader

class TestFileReader(unittest.TestCase):
    def test_read_file_exists(self):
        # Add test cases here

    def test_read_file_not_found(self):
        # Add test cases here

if __name__ == '__main__':
    unittest.main()
```


### Exercise 4: Testing a Factorial Calculator Function

Create unit tests for a Python function that calculates the factorial of a number. The function should return the factorial of a non-negative integer. Use various assertion methods like `assertEqual`, `assertRaises`, and `assertIsInstance`.

```python
# factorial.py

def factorial(n):
    
```

```python
# test_factorial.py

import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_0(self):

    def test_factorial_1(self):

    def test_factorial_5(self):

    def test_factorial_negative(self):

    def test_factorial_large_number(self):

    def test_the_output_instance_is_int(self):

if __name__ == '__main__':
    unittest.main()
```


## Exercise 5: Testing a Date Utility Module

Create unit tests for a module that provides date-related utility functions. Use assertions like `assertGreater`, `assertLess`, and `assertIsInstance` to test different aspects of date manipulation.

```python
# date_utils.py

from datetime import datetime, timedelta

def get_future_date(days):
    # Implement the function

def is_weekend(date):
    # Implement the function
```

```python
# test_date_utils.py

import unittest
from date_utils import get_future_date, is_weekend

class TestDateUtils(unittest.TestCase):
    def test_get_future_date(self):
        # Add test cases here

    def test_is_weekend(self):
        # Add test cases here

if __name__ == '__main__':
    unittest.main()
```


