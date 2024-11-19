# homePage.py
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from register import register
from login import login
from landingPage import landingPage
from usefulLinks import usefulLinks
from importantLinks import importantLinks
from initDatabase import *
from findSomeone import findPerson

def homePage():
    print("##############################################")
    print("#            Welcome to InCollege            #")
    print("#                                            #")
    print("#              By Team Montana               #")
    print("##############################################\n\n")

    print("\"InCollege has provided me with so many")
    print(" job opportunities and it has helped me ")
    print("  connect with so many students across  ")
    print("    so many different campuses\"     \n ")
    print("            -John Doe           \n")

    loop = True
    while loop:
        choice = input("Options: Login | Signup | Video | Find Someone | Useful Links | Important Links | Exit\nEnter Choice Here: ")

        if choice.lower() == "login":
            if(login()):
                landingPage()
        elif choice.lower() == "signup":
            register()
        elif choice.lower() == "video":
            print("\nVideo is now playing\n")
        elif choice.lower() == "find someone":
            findPerson()
        elif choice.lower() == "useful links":
            usefulLinks()
        elif choice.lower() == "important links":
            importantLinks()
        elif choice.lower() == "exit":
            loop = False
        else:
            print("\nInvalid input, please enter choice again\n")
    return 0

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=