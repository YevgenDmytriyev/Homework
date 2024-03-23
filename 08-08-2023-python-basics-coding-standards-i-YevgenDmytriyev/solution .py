#task 1
first = "Python is a versatile and powerful programming language."
print(first)

#task 2
def greet():
    print("Hello World")

greet()

#task 3
def first():
    print("first")

def last():
    print("last")

first()
last()

#task 4
def greet(first, last):
    print(f"Hi {first} {last}")

greet("John",  "Smith")
greet("Mary",  "Jane")

#task 5
def greet(first="John", last="Doe"):
    print(f"Hello,{first}{last}")

greet("Jane", "Smith")
greet("John")

#task 6
import random

def function_check():
    luck = random.random()
    if luck < 0.5:
        print("Sorry")
    else:
        print("Congratulations")

function_check()

#task 7
def my_custom_validation_function(
        one, two, three, four, five, six, seven, eight, nine, ten):
    pass

my_custom_validation_function(
    True, True, True, True, True, False, False, False, False, False)

#task 8
def my_custom_validation_function(
        one=False, two=False, three=False, four=False, five=False,
        six=True, seven=True, eight=True, nine=True, ten=True):
    pass

my_custom_validation_function(
    one=True, two=True, three=True, four=True, five=True,
    six=False, seven=False, eight=False, nine=False, ten=False)

#task 9
def my_custom_validation_function(
        one=False, two=False, three=False, four=False, five=False,
        six=True, seven=True, eight=True, nine=True, ten=True):
    if (
        one and two and three and four and five
        and not six and not seven and not eight and not nine and not ten
    ):
        print("ok")

my_custom_validation_function(
    one=True, two=True, three=True, four=True, five=True,
    six=False, seven=False, eight=False, nine=False, ten=False)

#task 10
def check_arguments(**kwargs):
    # Checking arguments before the conditional
    first_five_true = all(value is True for value in list(kwargs.values())[:5])
    last_five_false = all(
        value is False for value in list(kwargs.values())[5:])

    if first_five_true and last_five_false:
        print("ok")  # arguments are ok
    else:
        print("not ok")

check_arguments(
    arg1=True, arg2=True, arg3=True, arg4=True,
    arg5=True, arg6=False, arg7=False, arg8=False,
    arg9=False, arg10=False)