import math
# Task 1
def calculate_sum(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0: # This condition checks for odd numbers 
            total += i
    return total
print(calculate_sum(6))
"""The condition i % 2 != 0 checks if the number is odd. 
To get the sum of even numbers, we need to change this condition
to check for even numbers, which is i % 2 == 0."""

# Task 2
def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result
print(factorial(2))
"""The loop for i in range(n, 2, -1) should run from nn to 1 (both inclusive) to calculate the factorial.
The range function is missing the end value of 1, which causes the loop to never reach 2.
The correct loop should be for i in range(n, 0, -1):."""

# Improved Task 3
def find_max_improved(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value
result3 = find_max_improved([3, 8, 2, 5, 10])
print(result3)

# Improved Task 4
def is_prime_improved(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):  # Check up to the square root of the number
        if number % i == 0:
            return False
    return True
result4 = is_prime_improved(10)
print(result4)

# Improved Task 5
def bubble_sort_improved(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break  # If no two elements were swapped by inner loop, then the list is sorted
    return lst
result5 = bubble_sort_improved([4, 2, 7, 1, 3])
print(result5)
