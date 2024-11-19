# findSomeone.py
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from database import exist
from initDatabase import *

def findPerson():

    loop = True
    while loop:
        print("\n-=-=-=-=Welcome to the connection page=-=-=-=-\n")
        choice = input("Options: Find | Exit\nEnter choice here: ")

        if choice.lower() == "find":
            inputName()
        elif choice.lower() == "exit":
            loop = False
        else:
            print("\nInvalid input, please enter choice again\n")



def inputName():

    loop = True
    while loop:

        firstName = input("Enter their first name: ").lower()
        lastName = input("Enter their last name: ").lower()
        if exist("UserData", "firstName", firstName) and exist("UserData", "lastName", lastName):
            print("\nThey are a part of the InCollege system\n")
        else:
            print("\nThey are not yet a part of the InCollege system\n")

        choice = input("To find another user enter 'Find' or 'Exit' to exit\nEnter choice here: ")
        if choice.lower() == "exit":
            loop = False
        elif choice.lower() != "find":
            print("\nInvalid input, please enter choice again\n")

    return 0

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=