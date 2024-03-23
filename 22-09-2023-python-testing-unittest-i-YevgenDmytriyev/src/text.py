# src/text.py

def to_upper(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.upper()

def to_word_list_isupper(words):
    if not isinstance(words, list):
        raise TypeError("Input must be a list")
    return all(word.isupper() for word in words)
