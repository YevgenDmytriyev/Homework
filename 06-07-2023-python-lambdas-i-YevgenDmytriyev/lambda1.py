# 1 Task
add15 = lambda x: x + 15

print(add15(1))
print(add15(-2))

# 2 Task
isOdd = lambda x: x % 2 != 0
isEven = lambda x: x % 2 == 0
getParity = lambda x, parity: (isOdd(x) and parity == 'odd') or (isEven(x) and parity == 'even')

print(isOdd(2), isEven(2))
print(isOdd(1), isEven(1))
print(getParity(2, 'odd'), getParity(2, 'even'))
print(getParity(1, 'odd'), getParity(1, 'even'))

# 3 Task
starts_with_p = lambda s: s.lower().startswith('p')

print(starts_with_p("Python"))
print(starts_with_p("JavaScript"))
print(starts_with_p("pirate"))

# 4 Task
numbers = [2, 4, 5, 7, 9, 14]
factor = 2

result = list(map(lambda x: x * factor, numbers))
print(result)
