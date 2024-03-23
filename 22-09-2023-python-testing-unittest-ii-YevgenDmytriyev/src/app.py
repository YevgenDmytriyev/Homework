from random import randrange

# function will return random number between start and end parameter where end is included
def rnd(start, end):
    return randrange(start, end + 1)  # Include 'end' in the range

# function should return the highest number in a list
def max_num_in_list(numbers):
    if not numbers:
        return None  # Return None for an empty list
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
