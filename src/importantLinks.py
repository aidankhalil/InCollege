# importantLinks.py
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
import sqlite3
from initDatabase import *
def importantLinks():
    print("\n-=-=-=-=Important Links Page=-=-=-=-\n")

    loop = True
    while loop:
        choice = input("Options: Copyright Notice | About | Accessibility | User Agreement | Privacy Policy | Cookie Policy | Copyright Policy | Brand Policy | Guest Controls | Languages | Exit\nEnter choice here: ")

        if choice.lower() == "copyright notice":
            print("\nThis is my copyright notice\n")

        elif choice.lower() == "about":
            print("\nThis is my about page\n")

        elif choice.lower() == "accessibility":
            print("\nthis is my accessibility page\n")

        elif choice.lower() == "user agreement":
            print("\nThis is my user agreement page\n")

        elif choice.lower() == "privacy policy":
            print("\nThis is my privacy policy\n")

        elif choice.lower() == "cookie policy":
            print("\nThis is my cookie policy\n")

        elif choice.lower() == "copyright policy":
            print("\nThis is my copyright policy\n")

        elif choice.lower() == "brand policy":
            print("\nThis is my brand policy\n")

        elif choice.lower() == "guest controls":
            #Options provide signed in user w/ ability to turn off InCollege Email, SMS, targeted Advert features
            #Options are initially turned on when account created
            #Settings/changes should be saved when program exits and starts again 
            guest_controls()

        elif choice.lower() == "languages":
            language()
        elif choice.lower() == "exit":
            loop = False
        else:
            print("\nInvalid input, please enter choice again\n")

    return

def language():
    connection = global_conn
    cursor = connection.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM LoggedIn LIMIT 1);")
    isLoggedIn = cursor.fetchone()[0]
    #Options for logged in users, select english or spanish
    if isLoggedIn != 1:
        print("You are not logged in, please log in to change language settings")
        return
        
    print("\n-=-=-=-=Languages Page=-=-=-=-\n")
    # is to connect to the database and retrieve the information about the currrent user
    # Get the first and last name from the LoggedIn table
    cursor.execute("SELECT * FROM LoggedIn LIMIT 1")
    first, last  = cursor.fetchone()
    # Find out the current language prefference of the logged in user
    display_language(cursor, first, last) 
    loop = True
    while loop:
        choice = input("Options: English | Spanish | Exit\nEnter choice here: ")

        if choice.lower() == "english":
            cursor.execute("UPDATE UserData SET language = ? WHERE firstName = ? AND lastName = ?", ("English",first,last))
            connection.commit()
            # print the current language prefference
            print() # new line for prettiness
            display_language(cursor, first, last)  
        elif choice.lower() == "spanish":
            cursor.execute("UPDATE UserData SET language = ? WHERE firstName = ? AND lastName = ?", ("Spanish",first,last)) 
            connection.commit()
            # print the current language prefference
            print() # new line for prettiness
            display_language(cursor, first, last)    
        elif choice.lower() == "exit":
            loop = False
        else:
            print("\nInvalid input, please enter choice again\n")

def display_language(cursor, first, last):
        # print the current language prefference
        cursor.execute("SELECT language FROM UserData WHERE firstName = ? AND lastName = ?", (first,last))
        curr_value = cursor.fetchone()[0]
        print(f"Your current language is set to {curr_value}")

def guest_controls():
    connection = global_conn
    cursor = connection.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM LoggedIn LIMIT 1);")
    isLoggedIn = cursor.fetchone()[0]
    #Options for logged in users, select english or spanish
    if isLoggedIn != 1:
        print("You are not logged in, please log in to change control settings")
        return
    
    print("\n-=-=-=-=Guest Controls Page=-=-=-=-\n")
    # Get the First and Last name of the loggedIn user
    cursor.execute("SELECT * FROM LoggedIn LIMIT 1")
    first, last  = cursor.fetchone()
    # get current values of email, sms, ad
    email, sms, ad = display_toggle(cursor, first, last)

    loop = True
    while loop:
        choice = input("Options: Email | SMS | Advertising | Exit\nEnter choice to toggle here: ")

        if choice.lower() == "email":
            cursor.execute("UPDATE UserData SET email = ? WHERE firstName = ? AND lastName = ?", (0 if email == 1 else 1, first, last))
            connection.commit()
            # print the current email prefference
            print() # new line for prettiness
            email, sms, ad = display_toggle(cursor, first, last)  
        elif choice.lower() == "sms":
            cursor.execute("UPDATE UserData SET sms = ? WHERE firstName = ? AND lastName = ?", (0 if sms == 1 else 1,first,last)) 
            connection.commit()
            # print the current sms prefference
            print() # new line for prettiness
            email, sms, ad = display_toggle(cursor, first, last)   
        elif choice.lower() == "advertising":
            cursor.execute("UPDATE UserData SET ad = ? WHERE firstName = ? AND lastName = ?", (0 if ad == 1 else 1,first,last)) 
            connection.commit()
            # print the current ad prefference
            print() # new line for prettiness
            email, sms, ad = display_toggle(cursor, first, last) 
        elif choice.lower() == "exit":
            loop = False
        else:
            print("\nInvalid input, please enter choice again\n")

def display_toggle(cursor, first, last):
    cursor.execute("SELECT email, sms, ad FROM UserData WHERE firstName = ? AND lastName = ?", (first,last))
    email, sms, ad = cursor.fetchone()
    print(f"{'InCollege Email is':<30}{('On' if email == 1 else 'Off'):>5}")
    print(f"{'SMS is':<30}{('On' if sms == 1 else 'Off'):>5}")
    print(f"{'Targeted Advertising is':30}{('On' if ad == 1 else 'Off'):>5}")
    return email, sms, ad
        
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=