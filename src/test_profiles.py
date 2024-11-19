from database import newAccount
from test_base import get_display_output, set_keyboard_input, clear_database
from homePage import homePage
import sqlite3
from initDatabase import *
from main import *

def test_partial_profile_creation():

    clear_database()

    set_keyboard_input(["signup", "test1", "Test1234!", "rhino", "helm", "usf", "comp sci", 
                        "login", "test1", "Test1234!", "5", "create profile", 
                        "This is my test profile title", "This is my test major", "This is my test university", "yes", "exit", "6", "exit"])
    
    main()

    output = get_display_output()

    assert output.count("\nCongratulations, you've created part of your profile! To finish creation go to Edit Profile") == 1 

    clear_database()

def test_profile_edit_and_display():

    clear_database()

    set_keyboard_input(["signup", "test1", "Test1234!", "rhino", "helm", "usf", "comp sci", 
                        "login", "test1", "Test1234!", "5", "create profile", 
                        "This is my test profile title", "This is my test major", "This is my test university", "yes", 
                        "edit profile", "no", "yes", "computer science", "yes", "this is my new university", "no", "no", "no", "display profile", 
                        "exit", "6", "exit"])
    
    main()

    output = get_display_output()

    foundValue = False
    for line in output:
        if "This Is My New University" in line:
            foundValue = True
            break

    assert foundValue is True

    clear_database()

def test_no_profile_edit_and_display():

    clear_database()

    set_keyboard_input(["signup", "test1", "Test1234!", "rhino", "helm", "usf", "comp sci", 
                        "login", "test1", "Test1234!", "5", "display profile", "edit profile", "exit", "6", "exit"])
    
    main()

    output = get_display_output()

    assert output.count("\nUser profile does not exist. Please go to 'create profile'.") == 2

    clear_database()

def test_view_friend_profile():

    clear_database()

    set_keyboard_input(["signup", "test1", "Test1234!", "rhino", "helm", "usf", "comp sci", 
                        "signup", "test2", "Test1234!", "just", "kelp", "ucf", "art", 
                        "login", "test1", "Test1234!", "5", "search people", "make request", "just", "kelp", "exit", 
                        "create profile", "this is my profile title", "this is my major", "this is my university", 
                        "yes", "exit", "6", 
                        "login", "test2", "Test1234!", "5", "request list", "accept", "my connections", "view profile", "yes", "1", "no", "exit", "exit", "6", "exit"])
    
    main()

    output = get_display_output()

    foundValue = False
    for line in output:
        if "This Is My University" in line:
            foundValue = True
            break

    assert foundValue is True

    clear_database()


def test_full_profile_creation():

    clear_database()

    set_keyboard_input(["signup", "test1", "Test1234!", "rhino", "helm", "usf", "comp sci", 
                        "login", "test1", "Test1234!", "5", "create profile", 
                        "This is my test profile title", "This is my test major", "This is my test university", "no",
                        "this is my bio", "no", "no", "no", "usf", "BS", "4", "no",
                        "exit", "6", "exit"])
    
    main()

    output = get_display_output()

    assert output.count("\nCongratulations, you've created your profile!") == 1

    clear_database()

def test_view_friend_no_profile():

    clear_database()

    set_keyboard_input(["signup", "test1", "Test1234!", "rhino", "helm", "usf", "comp sci", 
                        "signup", "test2", "Test1234!", "just", "kelp", "ucf", "art", 
                        "login", "test1", "Test1234!", "5", "search people", "make request", "just", "kelp", "exit", 
                        "create profile", "this is my profile title", "this is my major", "this is my university",
                        "yes", "exit", "6",
                        "login", "test2", "Test1234!", "5", "request list", "accept", "exit", "6",
                        "login", "test1", "Test1234!", "5", "my connections", "view profile", "yes", "2", "no", "exit", "exit", "6", "exit"])
    
    main()

    output = get_display_output()

    assert output.count("\nThis friend has not created their profile.") == 1

    clear_database()

def test_full_profile_display():

    set_keyboard_input(["signup", "test1", "Test1234!", "rhino", "helm", "usf", "comp sci", 
                        "login", "test1", "Test1234!", "5", "create profile", 
                        "This is my test profile title", "This is my test major", "This is my test university", "no","this is my bio","no", "yes",
                        "My job title","My employer","07/10/2022","07/20/2023","Job location","My job description","no", "no","Test school name", "high school diploma" ,"2020-2024","no", "display profile", 
                        "exit", "6", "exit"])
    
    main()

    output = get_display_output()

    titleValue = False
    majorValue = False
    universityValue = False
    jobValue = False
    jobTitleValue = False
    educationValue = False
    for line in output:
        if "This is my test profile title" in line:
            titleValue = True
        if "This Is My Test Major" in line:
            majorValue = True
        if "This Is My Test University" in line: 
            universityValue = True
        if "Job #1" in line:
            jobValue = True
        if "Title: My job title" in line:
            jobTitleValue = True
        if "Education #1" in line:
            educationValue = True

    assert jobTitleValue == True and titleValue == True and majorValue == True and universityValue == True and jobValue == True and educationValue == True

    clear_database()

def test_view_full_friend_profile():

    set_keyboard_input(["signup", "test1", "Test1234!", "rhino", "helm", "usf", "comp sci", 
                        "signup", "test2", "Test1234!", "just", "kelp", "ucf", "art", 
                        "login", "test1", "Test1234!", "5", "search people", "make request", "just", "kelp", "exit", 
                        "create profile", "This is my test profile title", "This is my test major", "This is my test university", "no","this is my bio","no", "yes",
                        "My job title","My employer","07/10/2022","07/20/2023","Job location","My job description","no", "no","Test school name", "high school diploma" ,
                        "2020-2024","no", "exit", "6", "login", "test2", "Test1234!", "5", "request list", "accept", "my connections",
                        "view profile", "yes", "1", "no", "exit", "exit", "6", "exit"])
    
    main()

    output = get_display_output()

    titleValue = False
    majorValue = False
    universityValue = False
    jobValue = False
    jobTitleValue = False
    educationValue = False
    for line in output:
        if "This is my test profile title" in line:
            titleValue = True
        if "This Is My Test Major" in line:
            majorValue = True
        if "This Is My Test University" in line: 
            universityValue = True
        if "Job #1" in line:
            jobValue = True
        if "Title: My job title" in line:
            jobTitleValue = True
        if "Education #1" in line:
            educationValue = True

    assert jobTitleValue == True and titleValue == True and majorValue == True and universityValue == True and jobValue == True and educationValue == True

    clear_database()

    