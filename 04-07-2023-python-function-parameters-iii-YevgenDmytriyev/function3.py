users = []

def register_user(username, password, email):
    user = {
        'username': username,
        'password': password,
        'email': email
    }
    users.append(user)
    print("User registered successfully!")

def login_user(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            print("Login successful!")
            return
    print("Invalid username or password.")

def change_password(username, old_password, new_password):
    for user in users:
        if user['username'] == username:
            if user['password'] == old_password:
                user['password'] = new_password
                print("Password changed successfully!")
                return
            else:
                print("Invalid password.")
                return
    print("User not found.")

# Additional Feature: Get user details
def get_user_details(username):
    for user in users:
        if user['username'] == username:
            return user
    return None

# Additional Feature: Get all registered users
def get_all_users():
    return users

# Testing the functions
register_user("john123", "pass123", "john@example.com")
register_user("emma456", "abc456", "emma@example.com")
register_user("james789", "xyz789", "james@example.com")

print(get_all_users())

login_user("john123", "pass123")
login_user("emma456", "wrongpass")
login_user("james789", "xyz789")

change_password("john123", "pass123", "newpass")
change_password("emma456", "wrongpass", "newpass")

print(get_user_details("john123"))
