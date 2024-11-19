from jobs import createJobs
from register import newAccount
from login import isLoggedIn
from test_base import set_keyboard_input, get_display_output
import sqlite3
from initDatabase import *


def test_jobs_creation():
    connection = global_conn
    cursor = connection.cursor()
    cursor.execute("DELETE FROM UserLogin")
    cursor.execute("DELETE FROM UserData")
    cursor.execute("DELETE FROM JobListing")
    connection.commit()

    username = "minari"
    password = "Hello1!!"
    firstName = "first"
    lastName = "last"
    university = "USF"
    major = "art"

    newAccount(username, password, firstName, lastName, university, major)
    isLoggedIn(username)

    set_keyboard_input(["Chef","Cooking stuff","Gordan Ramsey","Somewhere in Florida", "$100000"])
    
    createJobs()
    
    output = get_display_output()

    assert output == ["\nTo create a job/internship listing please enter a title, job description, employer, location, and salary\n",
                      "Enter Title: ",
                      "Enter Description: ",
                      "Enter Employer: ",
                      "Enter Location: ",
                      "Enter Salary: "]
    
    cursor = connection.cursor()
    cursor.execute("DELETE FROM UserLogin")
    cursor.execute("DELETE FROM UserData")
    cursor.execute("DELETE FROM JobListing")
    connection.commit()
    
   
def test_jobs_limit():
    connection = global_conn
    cursor = connection.cursor()
    cursor.execute("DELETE FROM UserLogin")
    cursor.execute("DELETE FROM UserData")
    cursor.execute("DELETE FROM JobListing")
    connection.commit()

    username = "minari"
    password = "Hello1!!"
    firstName = "first"
    lastName = "last"
    university = "USF"
    major = "art"

    newAccount(username, password, firstName, lastName, university, major)
    isLoggedIn(username)

    set_keyboard_input(["Chef","Cooking stuff","Gordan Ramsey","Somewhere in Florida", "$100000"])
    createJobs()
    set_keyboard_input(["Chef","Cooking stuff","Gordan Ramsey","Somewhere in Florida", "$100000"])
    createJobs()
    set_keyboard_input(["Chef","Cooking stuff","Gordan Ramsey","Somewhere in Florida", "$100000"])
    createJobs()
    set_keyboard_input(["Chef","Cooking stuff","Gordan Ramsey","Somewhere in Florida", "$100000"])
    createJobs()
    set_keyboard_input(["Chef","Cooking stuff","Gordan Ramsey","Somewhere in Florida", "$100000"])
    createJobs()


    createJobs()
    
    output = get_display_output()

    assert output == ['\nTo create a job/internship listing please enter a title, job description, employer, location, and salary\n', 
                      'Enter Title: ', 
                      'Enter Description: ', 
                      'Enter Employer: ', 
                      'Enter Location: ', 
                      'Enter Salary: ', 
                      'All permitted job listing have been created, please come back later']
    
    cursor = connection.cursor()
    cursor.execute("DELETE FROM UserLogin")
    cursor.execute("DELETE FROM UserData")
    cursor.execute("DELETE FROM JobListing")
    cursor.execute("DELETE FROM LoggedIn")
    connection.commit()