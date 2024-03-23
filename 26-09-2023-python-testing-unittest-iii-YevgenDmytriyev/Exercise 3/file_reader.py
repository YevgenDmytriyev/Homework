# file_reader.py

class FileReader:
    def __init__(self, file_path):
        """
        Initialize the FileReader with the provided file path.

        Args:
            file_path (str): The path to the file to be read.
        """
        self.file_path = file_path

    def read_file(self):
        """
        Read and return the contents of the file.

        Returns:
            str: The contents of the file as a string, or None if the file is not found.
        """
        try:
            with open(self.file_path, 'r') as file:
                data = file.read()
            return data
        except FileNotFoundError:
            return None
