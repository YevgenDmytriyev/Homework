# task1

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subject_marks.sort(key=lambda x: x[1])
print(subject_marks)

# task2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

# task3
def protected(func):
    def wrapper():
        username = input("Username: ")
        password = input("Password: ")
        
        if username == "admin" and password == "admin":
            func()
        else:
            print("You are not authorized")
    
    return wrapper

def public():
    print("Hello World!")

@protected
def private():
    print("Welcome, admin!")

public()
private()


# task4
def wrap_with(tag):
    return lambda func: lambda *args, **kwargs: f"<{tag}>{func(*args, **kwargs)}</{tag}>"

@wrap_with("p")
def get_custom_html_greeting(first_name, last_name):
    return f"<em>Hello, <strong>{first_name} {last_name}</strong>!</em>"

print(get_custom_html_greeting("James", "Brown"))
