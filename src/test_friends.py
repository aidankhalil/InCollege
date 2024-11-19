from database import newAccount, tables
from test_base import get_display_output, set_keyboard_input, clear_database
from homePage import homePage
import sqlite3
from initDatabase import *
from main import *

def test_friend_notifications():


    tables()
    clear_database()
    
    usernameOne = "minari"
    passwordOne = "Hello1!!"
    firstNameOne = "kelp"
    lastNameOne = "just"
    universityOne = "usf"
    majorOne = "computer science"

    newAccount(usernameOne, passwordOne, firstNameOne, lastNameOne, universityOne, majorOne)

    usernameTwo = "test"
    passwordTwo = "Test1234!"
    firstNameTwo = "lemon"
    lastNameTwo = "flip"
    universityTwo = "ucf"
    majorTwo = "art"

    newAccount(usernameTwo, passwordTwo, firstNameTwo, lastNameTwo, universityTwo, majorTwo)

    set_keyboard_input(["login", "minari", "Hello1!!", "5", "search people", "make request", "lemon", "flip", "exit", "exit", "6",
                        "login", "test", "Test1234!", "6", "exit"])
    
    homePage()

    output = get_display_output()

    assert output.count("\U0001F514 Notification: You have a friend request. Go to 'Show My Network'-> 'Request List' to accept/reject\n") == 1 

    clear_database()

def test_friend_request_accept():

    set_keyboard_input(["signup", "test1", "Test1234!", "rhino", "helm", "usf", "comp sci", 
                        "signup", "test2", "Test1234!", "just", "kelp", "ucf", "art", 
                        "login", "test1", "Test1234!", "5", "search people", "make request", "just", "kelp", "exit", "exit", "6", 
                        "login", "test2", "Test1234!", "5", "request list", "accept", "exit", "6", "exit"])
    
    main()

    output = get_display_output()

    assert output.count("\nFriend request accepted. You are now friends.\n") == 1 

    clear_database()

def test_friend_request_reject():

    set_keyboard_input(["signup", "test1", "Test1234!", "rhino", "helm", "usf", "comp sci", 
                        "signup", "test2", "Test1234!", "just", "kelp", "ucf", "art", 
                        "login", "test1", "Test1234!", "5", "search people", "make request", "just", "kelp", "exit", "exit", "6", 
                        "login", "test2", "Test1234!", "5", "request list", "reject", "exit", "6", "exit"])
    
    main()

    output = get_display_output()

    assert output.count("\nFriend request rejected.\n") == 1 

    clear_database()

def test_friend_remove():

    set_keyboard_input(["signup", "test1", "Test1234!", "rhino", "helm", "usf", "comp sci", 
                        "signup", "test2", "Test1234!", "just", "kelp", "ucf", "art", 
                        "login", "test1", "Test1234!", "5", "search people", "make request", "just", "kelp", "exit", "exit", "6", 
                        "login", "test2", "Test1234!", "5", "request list", "accept", "my connections", "remove friend", "yes", "rhino", "helm", 
                        "exit", "exit", "6", "exit"])
    
    main()

    output = get_display_output()

    assert output.count("\nUnfriended successfully.\n") == 1 

    clear_database()