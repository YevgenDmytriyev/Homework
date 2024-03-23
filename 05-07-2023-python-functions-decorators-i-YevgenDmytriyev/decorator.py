# task 1
def make_bold(func):
    def wrapper():
        return "<strong>" + func() + "</strong>"
    return wrapper

@make_bold
def get_html_greeting():
    return "Hello, World!"

print(get_html_greeting())

# task 2
def make_bold(func):
    def wrapper(*args, **kwargs):
        return "<strong>" + func(*args, **kwargs) + "</strong>"
    return wrapper

@make_bold
def get_html_greeting():
    return "Hello, World!"

@make_bold
def get_custom_html_greeting(first, last):
    return "Hello, " + first + " " + last + "!"

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
print(get_html_greeting())

# task 3
def make_bold(func):
    def wrapper(*args, **kwargs):
        return "<strong>" + func(*args, **kwargs) + "</strong>"
    return wrapper

def make_italics(func):
    def wrapper(*args, **kwargs):
        return "<em>" + func(*args, **kwargs) + "</em>"
    return wrapper

def make_paragraph(func):
    def wrapper(*args, **kwargs):
        return "<p>" + func(*args, **kwargs) + "</p>"
    return wrapper

@make_bold
def get_full_name(first, last):
    return first + " " + last

@make_paragraph
@make_italics
def get_custom_html_greeting(first, last):
    return "Hello, " + get_full_name(first, last) + "!"

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))

# task 4
def wrap_with(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"<{tag}>" + func(*args, **kwargs) + f"</{tag}>"
        return wrapper
    return decorator

@wrap_with(tag="strong")
def get_full_name(first, last):
    return first + " " + last

@wrap_with(tag="p")
@wrap_with(tag="em")
def get_custom_html_greeting(first, last):
    return "Hello, " + get_full_name(first, last) + "!"

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
