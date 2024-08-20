import pickle
import hashlib
import sys
import os


class User:
    username = str
    email = str
    password_hash = str


def print_menu(logged):
    menu_not_logged = """
    ------Login-test------
    | 1. Signup          |
    | 2. Login           |
    | 3. Exit            |
    ----------------------
    """
    if not logged:
        print(menu_not_logged)


def signup():
    new_user = User
    new_user.username = input("Username:\n")
    email = input("Email:\n")
    if input("Confirm Email:\n") == email:
        new_user.email = email
    else:
        print("Email confirmation failed")
        return False
    password = input("Password:\n")
    if input("Confirm Password:\n") != password:
        print("Password confirmation failed")
        return False
    passhash = hashlib.sha512(password.encode())
    new_user.password_hash = passhash.hexdigest()
    return new_user


def login(user):
    if user.username != input("Username:\n"):
        print("Wrong username")
        return False
    passhash = hashlib.sha512(input("Password:\n").encode())
    if user.password_hash != passhash.hexdigest():
        print("Wrong password")
        return False
    return True


def save(user):
    with open("user", 'wb') as file:
        pickle.dump(user, file)
    file.close()
    print(f"{user.username} saved")


def load():
    with open("user", 'rb') as file:
        user = pickle.load(file)
    file.close()
    print(user)
    return user


if __name__ == '__main__':

    logged_in = False

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_menu(logged_in)
        if not logged_in:
            try:
                choice = input("Choice:\n")
                match int(choice):
                    case 1:
                        current_user = signup()
                        save(current_user)
                        logged_in = True
                        input("")
                    case 2:
                        try:
                            current_user = load()
                        except FileExistsError:
                            print("Could not load userdata")
                            continue
                        logged_in = login(current_user)
                        input("")
                    case 3:
                        print("Bye!")
                        sys.exit(0)
            except ValueError:
                print("Invalid Choice")
                input("")
                continue
        else:
            print("Wow you logged in\nBye now :)")
            input("")
            sys.exit(0)
