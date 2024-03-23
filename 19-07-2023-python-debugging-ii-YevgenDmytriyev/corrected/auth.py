# Task 1
# auth.py 
def authenticate_user():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if username == "admin" and password == "password":  # Corrected the 'or' to 'and'
        return True
    else:
        print("Please enter valid credentials!")
        return authenticate_user()  # Recursive call if credentials are wrong
# Testing the function (to be commented out in the final version)
authenticate_user()