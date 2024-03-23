#!/usr/bin/env python
from typing import Union, Callable

def compare_to_seven(value: Union[int, str, Callable]) -> str:
    """
    Compare the given value to the number 7 and return a string description of the comparison.
    """
    try:
        # Check if the value is a function
        if callable(value):
            return "Function is not comparable to 7."
        
        # Convert string to integer
        if isinstance(value, str):
            value_int = int(value)
        else:
            value_int = value
        
        if value_int > 7:
            return f"{value} is higher than 7."
        elif value_int < 7:
            return f"{value} is lower than 7."
        else:
            return f"{value} is 7."
    except ValueError:
        return f"{value} is not comparable to 7."

# Test the function with a sample input to ensure it works correctly
compare_to_seven("8")
