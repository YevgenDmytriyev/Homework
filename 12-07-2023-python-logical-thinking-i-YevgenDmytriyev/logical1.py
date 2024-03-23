# 1 task
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}

if username == valid["username"] and password == valid["password"]:
    print(f"Welcome, {username}!")
else:
    print("Credentials are invalid")

# 2  task
import datetime

def isweekend(date=datetime.datetime.now().date()):
    return date.weekday() == 5 or date.weekday() == 6

print(isweekend(datetime.date(2021, 8, 6)))  # False
print(isweekend(datetime.date(2021, 8, 7)))  # True
print(isweekend(datetime.date(2021, 8, 8)))  # True
print(isweekend(datetime.date(2021, 8, 9)))  # False

# 3 task
import datetime

def isweekend(date=datetime.datetime.now().date()):
    return date.weekday() == 5 or date.weekday() == 6

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}
today = datetime.date(2021, 8, 7) #(2021, 8, 6)

if username == valid["username"] and password == valid["password"] or isweekend(today):
    print(f"Welcome, {username}!")
else:
    print("Credentials are invalid")
    
# 4 task
def get_user(username, password):
    users = [
        {"name": "Holly", "password": "hunter"},
        {"name": "Peter", "password": "pan"},
        {"name": "Janis", "password": "joplin"}
    ]

    for user in users:
        if user["name"] == username and user["password"] == password:
            return user

    return None

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
user = get_user(username, password)

if user is None:
    print("An error occurred. You are not authorized.")

# 5 task
def get_user(username, password):
    users = [
        {"name": "Holly", "type": "Student", "password": "hunter"},
        {"name": "Peter", "type": "Student", "password": "pan"},
        {"name": "Janis", "type": "Teacher", "password": "joplin"}
    ]

    for user in users:
        if user["name"] == username and user["password"] == password:
            return user

    return None

def show_offers(username, password):
    user = get_user(username, password)
    if user and user["type"] == "Teacher":
        return
    print("We have great courses to offer you!")

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
show_offers(username, password)