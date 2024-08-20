import pickle
import hashlib
import sys


def print_menu():
    menu = """
    ------Login-test------
    1. Signup
    2. Login
    3. Exit
    ----------------------
    """
    print(menu)


if __name__ == '__main__':
    while True:
        print_menu()
        choice = input("Choice:\n")
        match choice:
            case 1:
                print("TODO: Signin")
            case 2:
                print("TODO: Login")
            case 3:
                sys.exit(0)

