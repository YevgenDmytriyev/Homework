# task1
def validate_numeric(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                return "The input arguments must be numeric"
        for arg in kwargs.values():
            if not isinstance(arg, (int, float)):
                return "The input arguments must be numeric"
        return func(*args, **kwargs)
    return wrapper

@validate_numeric
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

print(sum(1, 2))
print(sum(1, "2"))
print(sum(a=1, b="a"))
print(sum(a=1, b=3.4))

# task2
def debug(func):
    def wrapper(*args, **kwargs):
        print("**********")
        if args:
            print(f"Positional arguments: {', '.join(str(arg) for arg in args)}")
        else:
            print("There are no positional arguments")
        if kwargs:
            print(f"Keyword arguments: {', '.join(f'{key}={value}' for key, value in kwargs.items())}")
        else:
            print("There are no keyword arguments")
        try:
            result = func(*args, **kwargs)
            print(f"Result: {result}")
            print("**********")
            return result
        except Exception as e:
            print(f"Exception: {e}")
            print("**********")
            return None
    return wrapper

@debug
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

sum(1, 2)
sum(a=1, b=2)
sum(1, "a")

# task3
def cache(func):
    def wrapper(*args, **kwargs):
        if not hasattr(func, "cache"):
            func.cache = {}
        key = (args, tuple(kwargs.items()))
        if key in func.cache:
            print("Using the cache")
            return func.cache[key]
        else:
            print("Calculating")
            result = func(*args, **kwargs)
            func.cache[key] = result
            return result
    return wrapper

@cache
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

print(sum(1, 2))
print(sum(1, 2))
print(sum(3, 2))
print(sum(3, 2))
print(sum(2, 1))



