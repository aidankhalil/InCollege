from database import newAccount
from test_base import get_display_output, set_keyboard_input, clear_database
from homePage import homePage
import sqlite3
from initDatabase import *

def test_name_in_database():

    username = "minari"
    password = "Hello1!!"
    firstName = "kelp"
    lastName = "just"
    university = "USF"
    major = "art"

    newAccount(username, password, firstName, lastName, university, major)

    set_keyboard_input(["signup", "testUSERNAME", "Test1234!", "kelp", "just", "exit"])
    
    homePage()

    output = get_display_output()

    assert output.count("User already exists in the InCollege System") == 1 

    clear_database()
