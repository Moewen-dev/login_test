import sqlite3
import hashlib
import sys
import os


class User:
    username = str
    email = str
    password_hash = str


if __name__ == '__main__':
    try:

        # init user database
        conn = sqlite3.connect("users.db")
        cur = conn.cursor()

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
            pw_hash = hashlib.sha512(password.encode())
            new_user.password_hash = pw_hash.hexdigest()
            return new_user

        def login():
            username = input("Username:\n")
            usernames = cur.execute("SELECT user_id, username FROM users").fetchall()
            for u in usernames:
                if u[1] == username:
                    password = hashlib.sha512(input("Password:\n").encode()).hexdigest()

                    db_pw = cur.execute(f"SELECT user_id, password_hash FROM users").fetchall()
                    for p in db_pw:
                        if p[1] == password:
                            return True
                        print("Wrong password\n")
                        return False
            print("User not found\n")
            return False


        def save(user):
            data = (user.username, user.email, user.password_hash)
            cur.execute('INSERT INTO users(username, email, password_hash) VALUES (?, ?, ?)', data)
            conn.commit()

        logged_in = False


        if cur.execute("SELECT name FROM sqlite_master").fetchone() != ('users',) :
            cur.execute('''CREATE TABLE users
            (user_id INTEGER PRIMARY KEY,
            username,
            email,
            password_hash)''')
            print(f"Created {cur.execute("SELECT name FROM sqlite_master").fetchone()}")

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_menu(logged_in)
            if not logged_in:
                try:
                    choice = input("Choice:\n")
                    match int(choice):
                        case 1:
                            n_user = signup()
                            save(n_user)
                            print(f"Successfully registered {n_user.username}\n")
                            input("")
                        case 2:
                            logged_in = login()
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

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Used the fast way out huh...\nBye")
        sys.exit(0)
