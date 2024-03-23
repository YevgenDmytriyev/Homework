# task1
def show_registration(username, password, modulename):
    users = [
        {
            "name": "Holly",
            "type": "Student",
            "password": "hunter",
            "modules": [
                {"title": "Computer basics", "completed": True},
                {"title": "Python basics", "completed": False}
            ]
        },
        {
            "name": "Peter",
            "type": "Student",
            "password": "pan",
            "modules": [
                {"title": "Computer basics", "completed": False}
            ]
        },
        {
            "name": "Luke",
            "type": "Student",
            "password": "skywalker",
            "modules": [
                {"title": "Computer basics", "completed": True}
            ]
        },
        {
            "name": "Janis",
            "type": "Teacher",
            "password": "joplin"
        }
    ]

    user = get_user(username, password)

    if user is None:
        print("You did not register to the module", modulename)
    elif user["type"] == "Teacher":
        print("You are a teacher")
    else:
        for module in user["modules"]:
            if module["title"] == modulename:
                print("You are registered to the module", modulename)
                return

        print("You did not register to the module", modulename)

def get_user(username, password):
    users = [
        {
            "name": "Holly",
            "type": "Student",
            "password": "hunter",
            "modules": [
                {"title": "Computer basics", "completed": True},
                {"title": "Python basics", "completed": False}
            ]
        },
        {
            "name": "Peter",
            "type": "Student",
            "password": "pan",
            "modules": [
                {"title": "Computer basics", "completed": False}
            ]
        },
        {
            "name": "Luke",
            "type": "Student",
            "password": "skywalker",
            "modules": [
                {"title": "Computer basics", "completed": True}
            ]
        },
        {
            "name": "Janis",
            "type": "Teacher",
            "password": "joplin"
        }
    ]

    for user in users:
        if user["name"] == username and user["password"] == password:
            return user

    return None

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)


# task2

def show_registration(username, password, modulename):
    users = [
        {
            "name": "Holly",
            "type": "Student",
            "password": "hunter",
            "modules": [
                {"title": "Computer basics", "completed": True},
                {"title": "Python basics", "completed": False}
            ]
        },
        {
            "name": "Peter",
            "type": "Student",
            "password": "pan",
            "modules": [
                {"title": "Computer basics", "completed": False}
            ]
        },
        {
            "name": "Luke",
            "type": "Student",
            "password": "skywalker",
            "modules": [
                {"title": "Computer basics", "completed": True}
            ]
        },
        {
            "name": "Anonymous",
            "type": "Student",
            "password": "password",
            "modules": [
                {"title": "Computer basics", "completed": True}
            ]
        },
        {
            "name": "Janis",
            "type": "Teacher",
            "password": "joplin"
        }
    ]

    user = get_user(username, password)

    if user is None:
        print(f"You did not register to the module {modulename}.")
    elif user["type"] == "Teacher":
        print("You are a teacher.")
    else:
        for module in user["modules"]:
            if module["title"] == modulename:
                print(f"You are registered to the module {modulename}.")
                return

        print(f"You did not register to the module {modulename}.")

def has_completed_module(username, password, modulename):
    user = get_user(username, password)

    if user is not None and user["type"] == "Teacher":
        return
    else:
        for module in user["modules"]:
            if module["title"] == modulename:
                if module["completed"]:
                    print(f"You have completed the module {modulename}.")
                else:
                    print(f"You did not complete the module {modulename}.")
                return

        print(f"You did not complete the module {modulename}.")

def get_user(username, password):
    users = [
        {
            "name": "Holly",
            "type": "Student",
            "password": "hunter",
            "modules": [
                {"title": "Computer basics", "completed": True},
                {"title": "Python basics", "completed": False}
            ]
        },
        {
            "name": "Peter",
            "type": "Student",
            "password": "pan",
            "modules": [
                {"title": "Computer basics", "completed": False}
            ]
        },
        {
            "name": "Luke",
            "type": "Student",
            "password": "skywalker",
            "modules": [
                {"title": "Computer basics", "completed": True}
            ]
        },
        {
            "name": "Anonymous",
            "type": "Student",
            "password": "password",
            "modules": [
                {"title": "Computer basics", "completed": True}
            ]
        },
        {
            "name": "Janis",
            "type": "Teacher",
            "password": "joplin"
        }
    ]

    for user in users:
        if user["name"] == username and user["password"] == password:
            return user

    return None

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)
has_completed_module(username, password, modulename)

# task 3
def show_registration(username, password, modulename):
    users = [
        {
            "name": "Peter",
            "type": "Student",
            "password": "pan",
            "modules": [
                {"title": "Computer basics", "completed": False},
            ]
        },
        {
            "name": "Luke",
            "type": "Student",
            "password": "skywalker",
            "modules": [
                {"title": "Computer basics", "completed": True},
            ]
        },
        {
            "name": "Anonymous",
            "type": "Student",
            "password": "password",
            "modules": [
                {"title": "Python basics", "completed": False}
            ]
        },
        {
            "name": "Janis",
            "type": "Teacher",
            "password": "joplin"
        }
    ]

    user = get_user(username, password)

    if user is None:
        print(f"You did not register to the module {modulename}.")
    elif user["type"] == "Teacher":
        print("You are a teacher.")
    else:
        for module in user["modules"]:
            if module["title"] == modulename:
                print(f"You are registered to the module {modulename}.")
                return

        print(f"You did not register to the module {modulename}.")

def has_completed_module(username, password, modulename):
    user = get_user(username, password)

    if user is not None and user["type"] == "Teacher":
        return
    else:
        for module in user["modules"]:
            if module["title"] == modulename:
                if module["completed"]:
                    print(f"You have completed the module {modulename}.")
                else:
                    print(f"You did not complete the module {modulename}.")
                return

        print(f"You did not complete the module {modulename}.")

def get_user(username, password):
    users = [
        {
            "name": "Peter",
            "type": "Student",
            "password": "pan",
            "modules": [
                {"title": "Computer basics", "completed": False},  
            ]
        },
        {
            "name": "Luke",
            "type": "Student",
            "password": "skywalker",
            "modules": [
                {"title": "Computer basics", "completed": True}
            ]
        },
        {
            "name": "Anonymous",
            "type": "Student",
            "password": "password",
            "modules": [
                {"title": "Python basics", "completed": False}
            ]
        },
        {
            "name": "Janis",
            "type": "Teacher",
            "password": "joplin"
        }
    ]

    for user in users:
        if user["name"] == username and user["password"] == password:
            return user

    return None

def may_enroll(username, password, modulename):
    modules = [
        {"name": "Computer basics"},
        {"name": "Python basics", "requirement": "Computer basics"},
        {"name": "Django", "requirement": "Python basics"},
        {"name": "PHP", "requirement": "Computer basics"}
    ]

    user = get_user(username, password)

    if is_anonymous(user) and has_no_requirement(modulename, modules):
        return True
    elif is_student(user) and not is_registered_to_module(modulename, user):
        if has_no_requirement(modulename, modules):
            return True
        requirement = get_requirement(modulename, modules)
        if requirement and meets_requirement(requirement, user):
            return True

    return False

def is_anonymous(user):
    return user is None

def is_student(user):
    return user and user["type"] == "Student"

def is_registered_to_module(modulename, user):
    if user:
        for module in user.get("modules", []):
            if module["title"] == modulename:
                return True
    return False

def has_no_requirement(modulename, modules):
    for module in modules:
        if module["name"] == modulename and "requirement" not in module:
            return True
    return False

def get_requirement(modulename, modules):
    for module in modules:
        if module["name"] == modulename and "requirement" in module:
            return module["requirement"]
    return None

def meets_requirement(requirement, user):
    for module in user.get("modules", []):
        if module["title"] == requirement and module["completed"]:
            return True
    return False

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)
has_completed_module(username, password, modulename)

if may_enroll(username, password, modulename):
    print(f"You may register to the module {modulename}.")
else:
    print(f"You may not register to the module {modulename}.")


