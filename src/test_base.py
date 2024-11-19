'''
Source: 
https://www.youtube.com/watch?v=tBAj2FqgIwg
'''
from initDatabase import *
import builtins

input_values = []
print_values = []


def mock_input(s):
    print_values.append(s)
    return input_values.pop(0)


def mock_input_output_start():
    global input_values, print_values

    input_values = []
    print_values = []

    builtins.input = mock_input
    builtins.print = lambda *args, **kwargs: print_values.append(' '.join(map(str, args)))


def get_display_output():
    global print_values
    return print_values


def set_keyboard_input(mocked_inputs):
    global input_values

    mock_input_output_start()
    input_values = mocked_inputs

def clear_database():
    connection = global_conn
    cursor = connection.cursor()
    cursor.execute("DELETE FROM UserLogin")
    cursor.execute("DELETE FROM UserData")
    cursor.execute("DELETE FROM LoggedIn")
    cursor.execute("DELETE FROM Friends")
    cursor.execute("DELETE FROM Profiles")
    connection.commit()