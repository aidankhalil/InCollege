# usefulLinks.py
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from register import register
import sqlite3
from initDatabase import *

def usefulLinks():
    print("\n-=-=-=-=Useful Links Page=-=-=-=-\n")

    loop = True
    while loop:
        choice = input("Options: General | Browse | Business Solutions | Directories | Exit\nEnter choice here: ")

        if choice.lower() == "general":
            general()
        elif choice.lower() == "browse":
            print("\nUnder Construction\n")
        elif choice.lower() == "business solutions":
            print("\nUnder Construction\n")
        elif choice.lower() == "directories":
            print("\nUnder Construction\n")
        elif choice.lower() == "exit":
            loop = False
        else:
            print("\nInvalid input, please enter choice again\n")

def general():
    print("\n-=-=-=-=General Page=-=-=-=-\n")

    loop = True
    while loop:

        connection = global_conn
        cursor = connection.cursor()
        cursor.execute("SELECT EXISTS(SELECT 1 FROM LoggedIn LIMIT 1);")
        isLoggedIn = cursor.fetchone()[0]

        choice = input("Options: Signup | Help Center | About | Press | Blog | Careers | Developers | Exit\nEnter choice here: ")

        if choice.lower() == "signup":
            if isLoggedIn == 1:
                print("\nYou are already logged in!\n")
            else:
                register()
        elif choice.lower() == "help center":
            print("\nWe're here to help\n")
        elif choice.lower() == "about":
            print("\nIn College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide\n")
        elif choice.lower() == "press":
            print("\nIn College Pressroom: Stay on top of the latest news, updates, and reports\n")
        elif choice.lower() == "blog":
            print("\nUnder construction\n")
        elif choice.lower() == "careers":
            print("\nUnder construction\n")
        elif choice.lower() == "developers":
            print("\nUnder construction\n") 
        elif choice.lower() == "exit":
            loop = False
        else:
            print("\nInvalid input, please enter choice again\n")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=