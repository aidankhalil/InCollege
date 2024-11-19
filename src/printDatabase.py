# printDatabase.py
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
import sqlite3
from initDatabase import *

def print_database():
    connection = global_conn
    cursor = connection.cursor()

    # Fetch data from UserLogin table
    cursor.execute("SELECT * FROM UserLogin")
    print("UserLogin:")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fetch data from UserData table
    cursor.execute("SELECT * FROM UserData")
    print("\nUserData:")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fetch data from JobListing table
    cursor.execute("SELECT * FROM JobListing")
    print("\nJobListing:")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fetch data from LoggedIn table
    cursor.execute("SELECT * FROM LoggedIn")
    print("\nLoggedIn:")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fetch data from Friends table
    cursor.execute("SELECT * FROM Friends")
    print("\nFriends:")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fetch data from Profiles table
    cursor.execute("SELECT * FROM Profiles")
    print("\nProfiles:")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


# Call the function to print the database
print_database()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=