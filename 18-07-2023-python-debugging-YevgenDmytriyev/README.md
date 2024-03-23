[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/PRyQJmlg)
# 18-07-2023-Python-debugging

We have Five tasks. Each code contains bugs in it. Let's debug these codes. You can add a comment describing the error and how to fix it.

Task 1:
--------------
The following code is intended to calculate the sum of all even numbers between 1 and a given `n`. However, there is a bug in the code. Debug it using `breakpoint()` and print statements.

```python
def calculate_sum(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            total += i
    return total

result = calculate_sum(10)
print(result)
```

Task 2:
--------------
The code below is an implementation of the factorial function. However, it contains a bug that causes an infinite loop. Use `breakpoint()` and print statements to identify and fix the bug.

```python
def factorial(n):
    result = 1
    for i in range(n, 2, -1):
        result *= i
    return result

result = factorial(5)
print(result)
```

Task 3:
--------------
The following code is supposed to find the maximum value in a list, but it's not returning the correct result. Debug the code using `breakpoint()` and print statements to fix the issue.

```python
def find_max(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

result = find_max([3, 8, 2, 5, 10])
print(result)
```

Task 4:
--------------
The code snippet below is meant to check if a number is prime or not. However, it returns incorrect results for some inputs. Use `breakpoint()` and print statements to debug the code and make it work correctly.

```python
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

result = is_prime(10)
print(result)
```

Task 5:
--------------
The following code is an implementation of the bubble sort algorithm to sort a list. However, it's not sorting the list correctly. Use `breakpoint()` and print statements to debug the code and fix the sorting algorithm.

```python
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

result = bubble_sort([4, 2, 7, 1, 3])
print(result)
```

