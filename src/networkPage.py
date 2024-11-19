# networkPage.py
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from  initDatabase import global_conn
from connections import *
from friends import *
from database import get_loggedIn_id, get_id, get_first_and_last, accountCount

# network page with options to list all connections, list all requests and search people
def networkPage():
    print("\n-=-=-=-=My Network Page=-=-=-=-\n")
    loop = True
    while loop:
        choice = input("Options: My Connections | Request List | Search People | Create Profile | Edit Profile | Display Profile | Exit\nEnter choice here: ")

        if choice.lower() == "my connections":
            print_user_network()

        elif choice.lower() == "request list":
            print_requests()

        elif choice.lower() == "search people":
            search_people()

        elif choice.lower() == "create profile":
            if not has_created_profile(get_loggedIn_id()):
                create_profile() 
            else:
                print("\nA user profile already exists, go to 'edit profile' to finish or edit current user profile.")

        elif choice.lower() == "edit profile":
            edit_profile() 

        elif choice.lower() == "display profile":
            if not has_created_profile(get_loggedIn_id()):
                print("\nUser profile does not exist. Please go to 'create profile'.")
            else:
                print_profile(get_loggedIn_id())

        elif choice.lower() == "exit":
            loop = False
        else:
            print("\nInvalid input, please enter choice again\n")


def print_formated_list(list):
        print(f"\n{'ID':^5}|{'First Name':^15}|{'Last Name':^15}")
        for entry in list:
            print(f"{entry[0]:^5}|{str(entry[1]).title():^15}|{str(entry[2]).title():^15}")
        print()

def print_user_network():
    # get the id of the currently logged in user
    loggedin_id = get_loggedIn_id()
    friends = get_user_network(loggedin_id)

    if len(friends) == 0:
        print("\nYour connection list is empty\n")
        return
    else:
        print_formated_list(friends)

        loop = True
    while loop:
        choice = input("Options: View Profile | Remove Friend | Exit\nEnter Choice Here: ")

        if choice.lower() == "view profile":
            view_profile()
        elif choice.lower() == "remove friend":
            delete_friend()
        elif choice.lower() == "exit":
            loop = False
        else:
            print("\nInvalid input, please enter choice again\n")
    return 0

def delete_friend():
    loggedin_id = get_loggedIn_id()
    # Remove Friend
    loop = True if accountCount(table = "Friends") >= 1 else False
    while loop:
        choice = input("\nWould you like to delete a friend?(Yes/No) ")
        if choice.lower() == "yes":
            first_name = input("Enter first Name: ").lower()
            last_name = input("Enter last Name: ").lower()

            unfriend_id = get_id(first_name, last_name)
            unfriend(loggedin_id, unfriend_id)

            loop = True if accountCount(table = "Friends") >= 1 else False

        elif choice.lower() == "no":
            loop = False
        else:
            print("\nInvalid input, please enter choice again\n")

def view_profile():
    loggedin_id = get_loggedIn_id()
    # Display friends' profiles
    loop = True if accountCount(table="Friends") >= 1 else False
    while loop:
        choice = input("\nWould you like to view a friend's profile? (Yes/No): ")
        if choice.lower() == "yes":
            friend_id = input("Enter the ID of the friend whose profile you want to view: ")
            friend_id = int(friend_id)
            if is_friend(loggedin_id, friend_id):
                if has_created_profile(friend_id):
                    print_profile(friend_id)
                else:
                    print("\nThis friend has not created their profile.")
            else:
                print("\nYou are not connected to this friend.")
        elif choice.lower() == "no":
            loop = False
        else:
            print("\nInvalid input, please enter choice again\n")

# print_user_network helper, checks if a profile exists for each of a users friends
def has_created_profile(user_id):
    connection = global_conn
    profile = connection.execute(
        '''
        SELECT user_id
        FROM Profiles
        WHERE user_id = ?
        ''',
        (user_id,)
    ).fetchone()

    return profile is not None

# checks if a user is a friend
def is_friend(user_id, friend_id):
    connection = global_conn
    result = connection.execute(
        '''
        SELECT *
        FROM Friends
        WHERE (user_id = ? AND friend_id = ?) OR (user_id = ? AND friend_id = ?)
        ''',
        (user_id, friend_id, friend_id, user_id)
    ).fetchone()

    return result is not None


# search from the signed in users and option to make connection requests
def search_people():
    loop = True
    while loop:
        choice = input("Options: Last Name | University | Major | Make Request | Exit\nEnter choice here: ")

        if choice.lower() == "last name":
            name = input("Enter a last name: ").lower()
            people_list = search_students_by_last_name(name)
            if len(people_list) == 0:
                print("\nNo entries found.\n")
            else:
                print_formated_list(people_list)

        elif choice.lower() == "university":
            university = input("Enter a university name: ").lower()
            people_list = search_students_by_university(university)
            if len(people_list) == 0:
                print("\nNo entries found.\n")
            else:
                print_formated_list(people_list)

        elif choice.lower() == "major":
            major = input("Enter a major: ").lower()
            people_list = search_students_by_major(major)
            if len(people_list) == 0:
                print("\nNo entries found.\n")
            else:
                print_formated_list(people_list)

        elif choice.lower() == "make request":
            print("\nEnter first and last name to request a connection:\n")
            first_name = input("Enter first Name: ").lower()
            last_name = input("Enter last Name: ").lower()
            sender = get_loggedIn_id() 
            receiver = get_id(first_name, last_name) 
            send_friend_request(sender, receiver)

        elif choice.lower() == "exit":
            loop = False
        else:
            print("\nInvalid input, please enter choice again\n")

# Request list
def print_requests():
    current_user_id = get_loggedIn_id()
    requests = get_friend_requests(current_user_id)
    if len(requests) == 0:
        print("\nYou have no friend requests.\n")
        return

    for entry in requests:

        first, last = get_first_and_last(entry[0])
        sender_user_id = get_id(first, last)
        print(f"\n{str(first).title()} {str(last).title()} wants to connect (accept/reject/skip)")


        inner_loop = True
        while inner_loop:
            choice = input("Enter your choice: ")

            if choice.lower() == "accept":
                accept_friend_request(sender_user_id, current_user_id)
                inner_loop = False

            elif choice.lower() == "reject":
                cancel_friend_request(sender_user_id, current_user_id)
                inner_loop = False

            elif choice.lower() == "skip":
                inner_loop = False
            else:
                print("\nInvalid input, please enter choice again\n") 

# Create Profile
def create_profile():
    print("\n-=-=-=-=- Create Profile -=-=-=-=-")
    save_and_quit = " "
    profile_complete = 0
    profile_title = major = university_name = about = job_experience = education_experience = " "
    while save_and_quit.lower() != "yes":
        profile_title = input("Profile Title: ")
        major = input("Major: ").lower().title()
        university_name = input("University Name: ").lower().title()

        while True:
            save_and_quit = input("\nWould you like to Save/Quit (Yes) or Continue (No)? (Yes/No): ")
            if save_and_quit.lower() == "yes" or save_and_quit.lower() == "no":
                break
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")

        if save_and_quit.lower() == "yes":
            profile_complete = 0
            break

        about = input("About: ")

        while True:
            save_and_quit = input("\nWould you like to Save/Quit (Yes) or Continue (No)? (Yes/No): ")
            if save_and_quit.lower() == "yes" or save_and_quit.lower() == "no":
                break
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")

        if save_and_quit.lower() == "yes":
            profile_complete = 0
            break

        job_experience = " "
        has_job_experience = input("\nDo you have job experience? (Yes/No): ")
        if has_job_experience.lower() == "yes":
            job_experience += create_job_experience()

        while True:
            save_and_quit = input("\nWould you like to Save/Quit (Yes) or Continue (No)? (Yes/No): ")
            if save_and_quit.lower() == "yes" or save_and_quit.lower() == "no":
                break
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")

        if save_and_quit.lower() == "yes":
            profile_complete = 0
            break

        education_experience = create_education_experience()
        profile_complete = 1
        save_profile(get_loggedIn_id(), profile_title, major, university_name, about, job_experience, education_experience)
        print("\nCongratulations, you've created your profile!")
        break  # break out of create profile loop. Once a user finishes education experience, save and quit should not prompt.

    if save_and_quit.lower() == "yes":
        user_id = get_loggedIn_id()
        save_profile(user_id, profile_title, major, university_name, about, job_experience, education_experience)
        if profile_complete == 1:
            print("\nCongratulations, you've created your profile!")
        else:
            print("\nCongratulations, you've created part of your profile! To finish creation go to Edit Profile")
    else:
        print("\n")


# Create Profile helper function (job experience)
def create_job_experience():
    job_experience = ""
    job_count = 1
    has_more_jobs = True

    while has_more_jobs and job_count <= 3:
        print(f"\nJob #{job_count} Information:")
        job_title = input("Title: ")
        job_employer = input("Employer: ")
        date_started = input("Date Started: ")
        date_ended = input("Date Ended: ")
        location = input("Location: ")
        description = input("Description: ")

        job_experience += f"\nJob #{job_count}:\nTitle: {job_title}\nEmployer: {job_employer}\nDate Started: {date_started}\nDate Ended: {date_ended}\nLocation: {location}\nDescription: {description}"

        if job_count >= 3:
            print("\nMaximum number of job experiences created (3)!")
            break

        job_count += 1

        while True:
            more_jobs = input("\nDo you have other job experiences? (Yes/No): ")
            if more_jobs.lower() == "yes" or more_jobs.lower() == "no":
                break
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")

        if more_jobs.lower() != "yes":
            has_more_jobs = False

    return job_experience



#Create Profile helper function (education experience)
def create_education_experience():
    education_experience = ""
    education_count = 1
    has_more_education = True

    while has_more_education:
        print(f"\nEducation #{education_count} Information:")
        school_name = input("School Name: ")
        degree_received = input("Degree Received: ")
        years_attended = input("Years Attended: ")

        education_experience += f"\nEducation #{education_count}:\nSchool Name: {school_name}\nDegree Received: {degree_received}\nYears Attended: {years_attended}"

        education_count += 1

        while True:
            more_education = input("\nDo you have other education? (Yes/No): ")
            if more_education.lower() == "yes" or more_education.lower() == "no":
                break
            else:
                print("Invalid choice. Please enter 'Yes' or 'No'.")

        if more_education.lower() == "no":
            has_more_education = False

    return education_experience


# Create Profile helper function (saves user profile to database)
def save_profile(user_id, profile_title, major, university_name, about, job_experience, education_experience):
    # Save the profile to the Profiles table in the database
    connection = global_conn
    connection.execute(
        '''
        INSERT INTO Profiles (user_id, profile_title, major, university_name, about, job_experience, education_experience)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''',
        (user_id, profile_title, major, university_name, about, job_experience, education_experience)
    )
    connection.commit()

# Edit profile function
def edit_profile():
    user_id = get_loggedIn_id()
    connection = global_conn
    profile = connection.execute(
        '''
        SELECT profile_title, major, university_name, about, job_experience, education_experience
        FROM Profiles
        WHERE user_id = ?
        ''',
        (user_id,)
    ).fetchone()

    if profile is not None:
        profile_title, major, university_name, about, job_experience, education_experience = profile
        print("\n-=-=-=-=- Edit Profile -=-=-=-=-")
        print(f"\nCurrent Profile Title: {profile_title}")

        edit_title = input("\nWould you like to edit this section? (Yes/No): ")
        while edit_title.lower() not in ["yes", "no"]:
            print("Invalid input. Please enter 'Yes' or 'No'.")
            edit_title = input("\nWould you like to edit this section? (Yes/No): ")

        if edit_title.lower() == "yes":
            new_title = input("Enter new Profile Title: ")
            profile_title = new_title

        print(f"\nCurrent Major: {major}")
        edit_major = input("\nWould you like to edit this section? (Yes/No): ")
        while edit_major.lower() not in ["yes", "no"]:
            print("Invalid input. Please enter 'Yes' or 'No'.")
            edit_major = input("\nWould you like to edit this section? (Yes/No): ")

        if edit_major.lower() == "yes":
            new_major = input("Enter new Major: ").lower().title()
            major = new_major

        print(f"\nCurrent University Name: {university_name}")
        edit_university = input("\nWould you like to edit this section? (Yes/No): ")
        while edit_university.lower() not in ["yes", "no"]:
            print("Invalid input. Please enter 'Yes' or 'No'.")
            edit_university = input("\nWould you like to edit this section? (Yes/No): ")

        if edit_university.lower() == "yes":
            new_university = input("Enter new University Name: ").lower().title()
            university_name = new_university

        print(f"\nCurrent bio: {about}")
        edit_about = input("\nWould you like to edit this section? (Yes/No): ")
        while edit_about.lower() not in ["yes", "no"]:
            print("Invalid input. Please enter 'Yes' or 'No'.")
            edit_about = input("\nWould you like to edit this section? (Yes/No): ")

        if edit_about.lower() == "yes":
            new_about = input("Enter new bio: ").lower().title()
            about = new_about

        print(f"\nCurrent Job Experience: {job_experience}")
        edit_job_experience = input("\nWould you like to edit this section? (Yes/No): ")
        while edit_job_experience.lower() not in ["yes", "no"]:
            print("Invalid input. Please enter 'Yes' or 'No'.")
            edit_job_experience = input("\nWould you like to edit this section? (Yes/No): ")

        if edit_job_experience.lower() == "yes":
            job_experience = create_job_experience()

        print(f"\nCurrent Education Experience: {education_experience}")
        edit_education_experience = input("\nWould you like to edit this section? (Yes/No): ")
        while edit_education_experience.lower() not in ["yes", "no"]:
            print("Invalid input. Please enter 'Yes'or 'No'.")
            edit_education_experience = input("\nWould you like to edit this section? (Yes/No): ")

        if edit_education_experience.lower() == "yes":
            education_experience = create_education_experience()

        # Update the profile in the database
        connection.execute(
            '''
            UPDATE Profiles
            SET profile_title=?, major=?, university_name=?, about=?, job_experience=?, education_experience=?
            WHERE user_id=?
            ''',
            (profile_title, major, university_name, about, job_experience, education_experience, user_id)
        )
        connection.commit()

        print("\nProfile updated successfully!")
        print_profile(user_id)
    else:
        print("\nUser profile does not exist. Please go to 'create profile'.")


# Create Profile helper function (prints user profile, used after profile creation is finished or user finishes making profile edits). Also used for 'Display Profile' option
def print_profile(user_id):
    connection = global_conn
    profile = connection.execute(
        '''
        SELECT UserData.firstName, UserData.lastName, Profiles.profile_title, Profiles.major, Profiles.university_name, Profiles.about, Profiles.job_experience, Profiles.education_experience
        FROM UserData
        INNER JOIN Profiles ON UserData.id = Profiles.user_id
        WHERE UserData.id = ?
        ''',
        (user_id,)
    ).fetchone()

    if profile is not None:
        first_name, last_name, profile_title, major, university_name, about, job_experience, education_experience = profile

        formatted_first_name = first_name.lower().title()   # ensure the User's first 
        formatted_last_name = last_name.lower().title()     # and last name displays at the top of their profile.

        print(f"\n{formatted_first_name} {formatted_last_name}'s Profile")
        print("\n")
        print(f"-=-=-=Profile Title=-=-=-\n {profile_title}")
        print("\n")
        print(f"-=-=-=Major=-=-=-\n {major}")
        print("\n")
        print(f"-=-=-=University=-=-=-\n {university_name}")
        print("\n")
        print(f"-=-=-=Bio=-=-=-\n {about}")
        print("\n")
        print(f"-=-=-=Job Experience=-=-=- {job_experience}")
        print("\n")
        print(f"-=-=-=Education=-=-=- {education_experience}")
    else:
        print("\nProfile not found.")




#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=