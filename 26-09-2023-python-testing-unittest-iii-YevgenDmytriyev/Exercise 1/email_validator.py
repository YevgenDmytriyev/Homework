# email_validator.py
import re

class EmailValidator:
    def is_valid_email(self, email):
        # Regular expression for basic email validation
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

        