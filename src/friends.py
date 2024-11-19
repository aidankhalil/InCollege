# friends.py
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from database import global_conn

def send_friend_request(sender_id, receiver_id):
    connection = global_conn
    # Check the possibility to make a request
    if receiver_id == None:
        print("\nNo such account. Failed to make a request.\n")
        return
    
    if sender_id == receiver_id:
        print("\nUnable to send a request for yourself.\n")
        return

    # Check if the friend request already exists
    existing_request = connection.execute(
        "SELECT * FROM FriendRequests WHERE sender_id = ? AND receiver_id = ?;",
        (sender_id, receiver_id),
    ).fetchone()
    
    if existing_request:
        print("\nFriend request already sent.\n")
        return


    # Send the friend request
    connection.execute(
        "INSERT INTO FriendRequests (sender_id, receiver_id) VALUES (?, ?);",
        (sender_id, receiver_id),
    )
    connection.commit()

    print("\nFriend request sent.\n")

def accept_friend_request(sender_id, receiver_id):
    connection = global_conn

    # Check if the friend request exists
    friend_request = connection.execute(
        "SELECT * FROM FriendRequests WHERE sender_id = ? AND receiver_id = ?;",
        (sender_id, receiver_id),
    ).fetchone()

    if not friend_request:
        print("Friend request not found.")
        return

    # Remove the friend request
    connection.execute(
        "DELETE FROM FriendRequests WHERE sender_id = ? AND receiver_id = ?;",
        (sender_id, receiver_id),
    )
    connection.commit()

    # Add the sender and receiver as friends
    connection.execute(
        "INSERT INTO Friends (user_id, friend_id) VALUES (?, ?);",
        (sender_id, receiver_id),
    )
    connection.execute(
        "INSERT INTO Friends (user_id, friend_id) VALUES (?, ?);",
        (receiver_id, sender_id),
    )
    connection.commit()

    print("\nFriend request accepted. You are now friends.\n")

def cancel_friend_request(sender_id, receiver_id):
    connection = global_conn

    # Check if the friend request exists
    friend_request = connection.execute(
        "SELECT * FROM FriendRequests WHERE sender_id = ? AND receiver_id = ?;",
        (sender_id, receiver_id),
    ).fetchone()

    if not friend_request:
        print("Friend request not found.")
        return

    # Remove the friend request
    connection.execute(
        "DELETE FROM FriendRequests WHERE sender_id = ? AND receiver_id = ?;",
        (sender_id, receiver_id),
    )
    connection.commit()

    print("\nFriend request rejected.\n")

def unfriend(user_id, friend_id):
    connection = global_conn

    # Check if the friendship exists
    friendship = connection.execute(
        "SELECT * FROM Friends WHERE user_id = ? AND friend_id = ?;",
        (user_id, friend_id),
    ).fetchone()

    if not friendship:
        print("Friendship not found.")
        return

    # Remove the friendship
    connection.execute(
        "DELETE FROM Friends WHERE user_id = ? AND friend_id = ?;",
        (user_id, friend_id),
    )
    connection.execute(
        "DELETE FROM Friends WHERE user_id = ? AND friend_id = ?;",
        (friend_id, user_id),
    )
    connection.commit()

    print("\nUnfriended successfully.\n")

def get_friend_requests(user_id):
    connection = global_conn

    # Get the friend requests received by the user
    friend_requests = connection.execute(
        "SELECT sender_id FROM FriendRequests WHERE receiver_id = ?;", (user_id,)
    ).fetchall()

    return friend_requests

def get_friends(user_id):
    connection = global_conn

    # Get the friends of the user
    friends = connection.execute(
        "SELECT * FROM UserData WHERE id IN (SELECT friend_id FROM Friends WHERE user_id = ?);",
        (user_id,),
    ).fetchall()

    return friends

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=