# jobs.py
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from database import tables, jobListingCount, newJobListing
from login import isLoggedIn
from initDatabase import *
import sqlite3

def jobs():
    print("\n-=-=-=-=Welcome to the job board=-=-=-=-\n")

    loop = True
    while loop:
        choice = input("Options: Create | Find | Exit\nEnter choice here: ")

        if choice.lower() == "create":
            createJobs()
        elif choice.lower() == "find":
            findJobs()
        elif choice.lower() == "exit":
            loop = False
        else:
            print("\nInvalid input, please enter choice again\n")

def createJobs():

    connection = global_conn
    cursor = connection.cursor()
    cursor.execute("SELECT fName FROM LoggedIn")
    firstName = cursor.fetchone()[0]
    cursor.execute("SELECT lName FROM LoggedIn")
    lastName = cursor.fetchone()[0]
    #print(firstName)
    #print(lastName)

    table = "JobListing"

    if jobListingCount() >= 5:
        print("All permitted job listing have been created, please come back later")
        return None
    else:
        print("\nTo create a job/internship listing please enter a title, job description, employer, location, and salary\n")

        count = jobListingCount()
        #print("number of job listings:", count)

        title = input("Enter Title: ").lower()
        description = input("Enter Description: ").lower()
        employer = input("Enter Employer: ").lower()
        location = input("Enter Location: ").lower()
        salary = input("Enter Salary: ").lower()

    newJobListing(title, description, employer, location, salary, firstName, lastName)

    return 0

def findJobs():
    print("\nUnder Construction")
    return 0

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=