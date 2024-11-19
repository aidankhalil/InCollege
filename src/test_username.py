from register import usernameCheck
from database import newAccount
from test_base import set_keyboard_input, get_display_output, clear_database
from homePage import homePage
import sqlite3
from initDatabase import *

#-----------------------------------------------#
#TEST usernameCheck
# if username is found in the database returns 0
# otherwise returns 1

def test_enter_username():

    username = "test1"
    check = usernameCheck(username)
    assert check == "test1"

    clear_database()


def test_duplicate_username():

    username = "minari"
    password = "Hello1!!"
    firstName = "1"
    lastName = "2"
    university = "USF"
    major = "art"

    newAccount(username, password, firstName, lastName, university, major)


    newUsername = "minari"
    set_keyboard_input([newUsername])

    usernameCheck(newUsername)

    output = get_display_output()

    assert output == ["Username already exists"]

    clear_database()

def test_account_limit():

    username = ["minari", "calamari", "villager", "arizona", "montana", "test1", "test2", "test3", "test4", "test5" ]
    password = "Hello1!"
    firstName = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    lastName = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
    university = "USF"
    major = "art"

    for i in range(len(username)):
        newAccount(username[i], password, firstName[i], lastName[i], university, major)

    set_keyboard_input(["signup", "exit"])

    homePage()

    output = get_display_output()

    assert output.count("All permitted accounts have been created, please come back later") == 1
    
    clear_database()