# login.py
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from database import exist, tables, storeLoggedInUser
from initDatabase import *

def login():
    username = input("Enter Username: ")
    log = isLoggedIn(username)
    #print(log)

    if not exist("UserLogin", "username", username):
        print("\nUsername does not exist\n")
        return 0

    password = input("Enter Password: ")
    connection = global_conn
    cursor = connection.cursor()
    cursor.execute("SELECT password FROM UserLogin WHERE username = ?;", (username,))
    storedPassword = cursor.fetchone()

    if storedPassword is None:
        print("\nUsername does not exist\n")
        return 0

    if password != storedPassword[0]:
        print("\nIncorrect password\n")
        return 0

    print("You have successfully logged in")

    return 1

def isLoggedIn(username):
    connection = global_conn
    cursor = connection.cursor()
    cursor.execute("SELECT UserData.firstName, UserData.lastName FROM UserData WHERE UserData.id = (SELECT id FROM UserLogin WHERE username = ?)", (username,))
    loggedIn = cursor.fetchone()

    if loggedIn is None:
        return None

    storeLoggedInUser(loggedIn)
    return loggedIn

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=