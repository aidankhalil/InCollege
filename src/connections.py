# connections.py
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from database import global_conn

def search_students_by_last_name(last_name):
    connection = global_conn

    # Search for students by last name and return a list of matching profiles
    results = connection.execute(
        "SELECT id, firstName, lastName FROM UserData WHERE lastName = ?;", (last_name,)
    ).fetchall()

    return results

def search_students_by_university(university):
    connection = global_conn

    # Search for students by university and return a list of matching profiles
    results = connection.execute(
        "SELECT id, firstName, lastName FROM UserData WHERE university = ?;", (university,)
    ).fetchall()

    return results

def search_students_by_major(major):
    connection = global_conn

    # Search for students by major and return a list of matching profiles
    results = connection.execute(
        "SELECT id, firstName, lastName FROM UserData WHERE major = ?;", (major,)
    ).fetchall()

    return results

def get_user_network(user_id):
    connection = global_conn

    # Retrieve the user's network (connected friends) and return a list of profiles
    network = connection.execute(
        "SELECT id, firstName, lastName FROM UserData WHERE id IN (SELECT friend_id FROM Friends WHERE user_id = ?);", (user_id,)
    ).fetchall()

    return network

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=