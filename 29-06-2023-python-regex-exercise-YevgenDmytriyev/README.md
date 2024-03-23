[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/RToRA2cr)
# 29-06-2023-Python-Regex-exercise

These exercises cover various aspects of regular expressions in Python using the `re` module. 

Exercise 1:
Write a regex pattern that matches any string containing three consecutive digits.
```python
import re
strings = ["123", "abc456", "789xyz", "12", "1a2b3c"]

```

Exercise 2:
Write a regex pattern that matches any string containing only uppercase letters.
```python
import re
strings = ["HELLO", "WORLD", "123", "Hello", "UPPERCASE"]

```

Exercise 3:
Write a regex pattern that matches valid email addresses.
```python
import re
emails = ["test@example.com", "john.doe@gmail.com", "invalid_email", "user@domain", "abc@123.xyz"]

```

Exercise 4:
Write a regex pattern that matches any string containing a valid date in the format "DD-MM-YYYY".
```python
import re
dates = ["31-12-2022", "15-06-23", "02/05/2023", "2022-12-31", "01-13-2023"]

```

Exercise 5:
Write a regex pattern that matches any string containing a valid URL starting with "http://" or "https://".
```python
import re
urls = ["http://www.example.com", "https://www.google.com", "ftp://invalid-url.com", "https://sub.domain.co.uk", "http://localhost"]

```

Exercise 6:
Write a regex pattern that matches any string containing a valid phone number in the format "+XX-XXXXXXXXXX", where X represents a digit.
```python
import re
phone_numbers = ["+91-1234567890", "+44-9876543210", "+1-1234567890", "+12-9876543210", "+1-1234"]

```

Exercise 7:
Write a regex pattern that matches any string containing a valid IPv4 address in the format "XXX.XXX.XXX.XXX", where XXX represents a number between 0 and 255.
```python
import re
ip_addresses = ["192.168.0.1", "10.0.0.0", "256.0.0.0", "172.16.0.0", "127.0.0.1", "0.0.0.0"]

```

Exercise 8:
Write a regex pattern that matches any string containing a word that starts with a capital letter and is followed by one or more lowercase letters.
```python
import re
sentences = ["Hello, World!", "This is a Sentence.", "openAI", "python", "One Two Three"]

```

Exercise 9:
Write a regular expression pattern that matches any hexadecimal color code in the format "#RRGGBB". Test it on the following color codes: "#FF0000", "#00FF00", "#0000FF", "#123ABC".

To match hexadecimal color codes in the format "#RRGGBB", you can use the following regular expression pattern:

```python
import re
color_codes = ["#FF0000", "#00FF00", "#0000FF", "#123ABC", "#abc123", "#1234567"]

```

The pattern `#[0-9A-Fa-f]{6}` matches a "#" character followed by exactly six hexadecimal digits (0-9, A-F, a-f).

Output:
```
'#FF0000' is a valid hexadecimal color code
'#00FF00' is a valid hexadecimal color code
'#0000FF' is a valid hexadecimal color code
'#123ABC' is a valid hexadecimal color code
'#abc123' is an invalid hexadecimal color code
'#1234567' is an invalid hexadecimal color code
```


Exercise 10 (Optional):
Write a regular expression to validate a password with the following criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character (e.g., !@#$%^&*)
The  code Should include specific error messages for each validation criterion
```python
import re
passwords = ["Abcd1234!", "passWORD!123", "abc123", "Password", "12345678"]
```

``` Output
'Abcd1234!' is a valid password.
'passWORD!123' is a valid password.
'abc123' is an invalid password. Reason(s): Password must be at least 8 characters long, Password must contain at least one uppercase letter, Password must contain at least one special character (@$!%*#?&).
'Password' is an invalid password. Reason(s):  Password must contain at least one digit, Password must contain at least one special character (@$!%*#?&).
'12345678' is an invalid password. Reason(s): Password must contain at least one lowercase letter, Password must contain at least one uppercase letter, Password must contain at least one special character (@$!%*#?&).

```
