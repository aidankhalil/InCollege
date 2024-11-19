# database.py
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
import os
import sqlite3
from initDatabase import *

global_conn = sqlite3.connect("montana.db")

def tables(connection=global_conn):
    # User Login info
    connection.execute("""CREATE TABLE IF NOT EXISTS UserLogin 
    (id INTEGER PRIMARY KEY, 
    username TEXT, 
    password TEXT);""")  

    # User Data info
    connection.execute("""CREATE TABLE IF NOT EXISTS UserData 
    (id INTEGER PRIMARY KEY, 
    firstName TEXT, 
    lastName TEXT UNIQUE,
    language TEXT DEFAULT "English" NOT NULL,
    email INTEGER DEFAULT 1,
    sms INTEGER DEFAULT 1,
    ad INTEGER  DEFAULT 1,
    major TEXT,
    university TEXT);""")

    # Job/Internship info
    connection.execute("""CREATE TABLE IF NOT EXISTS JobListing 
    (jobPostId INTEGER PRIMARY KEY, --A unique value for each job listing
    position TEXT NOT NULL, 
    description TEXT NOT NULL, 
    employer TEXT NOT NULL, 
    location TEXT NOT NULL, 
    salary TEXT NOT NULL,
    posterFirstName TEXT NOT NULL,
    posterLastName TEXT NOT NULL);""")

    # Current Logged In User
    connection.execute(("""CREATE TABLE IF NOT EXISTS LoggedIn 
    (fName TEXT,
    lName);"""))

    # Friend Requests info
    connection.execute(
        """CREATE TABLE IF NOT EXISTS FriendRequests
        (sender_id INTEGER,
        receiver_id INTEGER,
        FOREIGN KEY(sender_id) REFERENCES UserData(id),
        FOREIGN KEY(receiver_id) REFERENCES UserData(id),
        PRIMARY KEY(sender_id, receiver_id));"""
    )

    # Friends info
    connection.execute(
        """CREATE TABLE IF NOT EXISTS Friends
        (user_id INTEGER,
        friend_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES UserData(id),
        FOREIGN KEY(friend_id) REFERENCES UserData(id),
        PRIMARY KEY(user_id, friend_id));"""
    )

    # Profile info
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            profile_title TEXT,
            major TEXT,
            university_name TEXT,
            about TEXT,
            job_experience TEXT,
            education_experience TEXT,
            FOREIGN KEY (user_id) REFERENCES Users(id)
        );
    ''')


def exist(table, column, value, connection=global_conn):
    query = "SELECT 1 FROM {} WHERE {} = ? LIMIT 1;".format(table, column)
    result = connection.execute(query, (value,)).fetchone()
    return result is not None

def newAccount(username, password, firstName, lastName, university, major, connection=global_conn):
    # Saves Login Info
    connection.execute(
        "INSERT INTO UserLogin (username, password) VALUES (?, ?);",
        (username, password))
    connection.commit()
  
    # Saves User info
    connection.execute(
        "INSERT INTO UserData (firstName, lastName, university, major) VALUES (?, ?, ?, ?);",
        (firstName, lastName, university, major))
    connection.commit()
  
def accountCount(table="UserLogin", connection=global_conn):
    return connection.execute("SELECT COUNT(*) FROM " + table + ";").fetchone()[0]

def jobListingCount(connection=global_conn):
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM JobListing;")
    count = cursor.fetchone()[0]
    return count

def newJobListing(position, description, employer, location, salary, firstName, lastName, connection=global_conn):
    # Saves Job Listing info
    connection.execute(
        "INSERT INTO JobListing (position, description, employer, location, salary, posterFirstName, posterLastName) VALUES (?, ?, ?, ?, ?, ?, ?);",
        (position, description, employer, location, salary, firstName, lastName))
    connection.commit()

def storeLoggedInUser(loggedIn, connection=global_conn):
    # Saves current logged in user first and last name
    connection.execute("DELETE FROM LoggedIn")
    connection.execute(
        "INSERT INTO LoggedIn (fName, lName) VALUES (?, ?);",
        (*loggedIn,))
    connection.commit()

def loggedOut(connection=global_conn):
    # Clears LoggedIn table
    connection.execute("DELETE FROM LoggedIn;")
    connection.commit()

def get_loggedIn_id(connection = global_conn):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM LoggedIn LIMIT 1")
    first, last  = cursor.fetchone()
    cursor.execute("SELECT id FROM UserData WHERE firstName = ? AND lastName = ?", (first, last))
    id = cursor.fetchone()[0]
    return id

def get_id(first, last, connection = global_conn):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM UserData WHERE firstName = ? AND lastName = ?", (first, last))
    result = cursor.fetchone()
    if result == None:
        return None
    else:
        id = result[0]
        return id

def get_first_and_last(id,connection = global_conn):
    cursor = connection.cursor()
    cursor.execute("SELECT firstName, lastName FROM UserData WHERE id = ?", (id,))
    first_name, last_name = cursor.fetchone()
    return first_name, last_name

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=