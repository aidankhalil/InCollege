# landingPage.py
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from jobs import jobs
from findSomeone import findPerson
from database import loggedOut
from usefulLinks import usefulLinks
from importantLinks import importantLinks
from initDatabase import *
from networkPage import networkPage
from database import get_loggedIn_id, exist


def exitProgram():
    loggedOut()
    return

def useLinks():
    usefulLinks()

    landingPage()

def impLinks():
    importantLinks()

    landingPage()

def jobSearch():
    jobs()
    #print("\nUnder construction")

    landingPage()

# def findSomeone():
#     findPerson()
#     #print("\nUnder construction")

    landingPage()
def showNetwork():
    networkPage()

    landingPage()

def learnSkill():
    print("\n-=-=-=-=Skills Page=-=-=-=-\n\n1.Time Management \n2.Coding \n3.Marketing \n4.Communication \n5.Problem Solving \n6. Exit")

    option = -1
    validOptions=['1','2','3','4','5','6']
    while option not in validOptions:
      option = input("Skill you would like to learn: ")

    if option == '1':
        print("\nUnder Construction")
        learnSkill()
    elif option == '2':
        print("\nUnder Construction")
        learnSkill()
    elif option == '3':
        print("\nUnder Construction")
        learnSkill()
    elif option == '4':
        print("\nUnder Construction")
        learnSkill()
    elif option == '5':
        print("\nUnder Construction")
        learnSkill()
    elif option == '6':
        landingPage()
    else:
        print("Enter a number: ")
        learnSkill()
    pass

def landingPage():


        options = {
            1: jobSearch,
            2: learnSkill,
            3: useLinks,
            4: impLinks,
            5: showNetwork,
            6: exitProgram
        }
        print("\n-=-=-=-=Landing Page=-=-=-=-\n")

        # Notification
        logged_in_id = get_loggedIn_id()
        if exist("friendRequests", "receiver_id", logged_in_id):
            print("\U0001F514 Notification: You have a friend request. Go to 'Show My Network'-> 'Request List' to accept/reject\n")

        print("Menu:")
        print("1. Jobs")
        print("2. Learn a New Skill")
        print("3. Useful Links")
        print("4. Important Links")
        print("5. Show My Network")
        print("6. Logout")
        # Prompt the user to choose an action after login or registration (currently only jobsearch menu, which will print "in construction")
        choice = -1
        validOptions=[1,2,3,4,5,6]
        while choice not in validOptions:
            choice = userInput("Please enter a number to select an option: ")
        selected_option = options.get(choice)
        if selected_option:
            selected_option()
        else:
            print("Invalid choice.")

def userInput(prompt):
    while True:
        try:
            value = int(input(prompt))  # Prompt the user for input
            return value                # Return converted integer value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=