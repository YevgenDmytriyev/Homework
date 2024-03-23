# test_file_reader.py

import unittest
from file_reader import FileReader

class TestFileReader(unittest.TestCase):
    def test_read_file_exists(self):
        file_path = "existing_file.txt"
        reader = FileReader(file_path)
        data = reader.read_file()

        # Check that the data is not None when the file exists
        self.assertIsNotNone(data)

        # Check that the data is a string (or the expected data type)
        self.assertIsInstance(data, str)

        # You can add more specific assertions based on the expected content of the file
        # Example: self.assertEqual(data, "Expected file content")

    def test_read_file_not_found(self):
        file_path = "non_existing_file.txt"
        reader = FileReader(file_path)
        data = reader.read_file()

        # Check that the data is None when the file is not found
        self.assertIsNone(data)

if __name__ == '__main__':
    unittest.main()

# OUTPUT:

# dci-student  Exercise3  ➜ ( main)  ♥ 15:38  python3 -m unittest -v
# test_read_file_exists (test_file_reader.TestFileReader.test_read_file_exists) ... ok
# test_read_file_not_found (test_file_reader.TestFileReader.test_read_file_not_found) ... ok

# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK