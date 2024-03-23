# task1
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)
countdown(5)

# task2
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(0))
print(factorial(1))
print(factorial(10))

# task3
def harmonic_sum(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonic_sum(n-1)

print(harmonic_sum(7))
print(harmonic_sum(4))