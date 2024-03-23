# string_utils.py

def reverse_string(s):
    """
    Reverse a given string.

    Args:
        s (str): The input string.

    Returns:
        str: The reversed string.
    """
    return s[::-1]

def count_vowels(s):
    """
    Count the number of vowels (a, e, i, o, u) in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def capitalize_first_letter(s):
    """
    Capitalize the first letter of a sentence.

    Args:
        s (str): The input sentence.

    Returns:
        str: The sentence with the first letter capitalized.
    """
    if len(s) == 0:
        return s
    return s[0].upper() + s[1:]
