# register.py
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from database import newAccount, exist, accountCount
from initDatabase import *
import re

def register():

# Change the limit to the 10 accounts 
    if accountCount() >= 10:
        print("All permitted accounts have been created, please come back later")
        return None

    while True:
        username = usernameCheck(input("Enter Username: "))
        if username:
            break

    while True:
        password = passwordPrompt()
        if passwordCheck(password):
            break

    while True:
        firstName, lastName = nameCheck()
        if firstName is not None and lastName is not None:
            break
        else:
            return None
        
    university = pickUniversity()
    major = pickMajor()

    #Stores user info into database
    newAccount(username, password, firstName, lastName, university, major)

def usernameCheck(username):

    table = "UserLogin"

    if exist(table, "username", username):
        print("Username already exists")
        return 0
    else:
        return username

def passwordPrompt():
    while True:

        print("\nPassword must be between 8 and 12 characters containing at least one uppercase letter, one digit, and one special character\n")

        password = input("Enter Password: ")
        if passwordCheck(password):
            return password
        else:
            print("Invalid password")

def passwordCheck(password):

    if len(password) < 8 or len(password) > 12:
        print("Password must be between 8 and 12 characters")
        return False

    if not re.search(r"[A-Z]", password):
        print("Password must contain at least one uppercase letter")
        return False

    if not re.search(r"\d", password):
        print("Password must contain at least one digit")
        return False

    if not re.search(r"[!@#$%^&*()\-_=+[{\]};:'\",<.>/?]", password):
        print("Password must contain at least one special character")
        return False

    return True

def nameCheck():

    #while True:
        firstName = input("Enter first name: ").lower()
        lastName = input("Enter last name: ").lower()

        if exist("UserData", "firstName", firstName) and exist("UserData", "lastName", lastName):
            print("User already exists in the InCollege System")
            return None, None
        else:
            return firstName, lastName
        
def pickMajor():

    major = input("Enter Major: ").lower()

    return major

def pickUniversity():

    university = input("Enter University: ").lower()

    return university

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=