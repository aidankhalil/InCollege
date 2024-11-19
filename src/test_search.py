from database import newAccount
from test_base import get_display_output, set_keyboard_input, clear_database
from homePage import homePage
import sqlite3
from initDatabase import *

def test_search_university():

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

    set_keyboard_input(["login", "minari", "Hello1!!", "5", "search people", "university", "ucf", "exit", "exit", "6", "exit"])
    
    homePage()

    output = get_display_output()

    foundValue = False
    for line in output:
        if firstNameTwo.title() in line and lastNameTwo.title() in line:
            foundValue = True
            break

    assert foundValue is True

    clear_database()

def test_search_lastname():

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

    set_keyboard_input(["login", "minari", "Hello1!!", "5", "search people", "last name", "flip", "exit", "exit", "6", "exit"])
    
    homePage()

    output = get_display_output()

    foundValue = False
    for line in output:
        if firstNameTwo.title() in line and lastNameTwo.title() in line:
            foundValue = True
            break

    assert foundValue is True

    clear_database()

def test_search_major():

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

    set_keyboard_input(["login", "minari", "Hello1!!", "5", "search people", "major", "art", "exit", "exit", "6", "exit"])
    
    homePage()

    output = get_display_output()

    foundValue = False
    for line in output:
        if firstNameTwo.title() in line and lastNameTwo.title() in line:
            foundValue = True
            break

    assert foundValue is True

    clear_database()