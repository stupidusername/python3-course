# Requirement:
# Write a program that allows the creation of the user DB of a system.
# Each user must have an id, username and first and last name.
# The ID and username must be unique for each user.
# The username must be at least 3 characters long and it must only contain
# low case letters.
# At the end the program must print a list of the users ordered by ascending
# username.

# Implemented on Python 3.6.

users = []

def create_user(id, username, first_name, last_name):
    # Add a new user to the list.
    users.append({
        'id': id,
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
    })


def is_unique(attr, value):
    # Return True if the user is unique.
    return all([user[attr] != value for user in users])


def ask_user_info():
    # Ask and validate ID.
    id = int(input("User ID (integer only): "))
    if not is_unique(attr='id', value=id):
        print("The entered ID is not unique.")
        return
    # Ask and validate username.
    username = input("Username: ")
    if len(username) < 3:
        print("Username must be at least 3 characters long.")
        return
    if any([c < 'a' or c > 'z' for c in username]):
        print("Username must only contain lower case letters.")
        return
    if not is_unique(attr='username', value=username):
        print("The entered username is not unique.")
        return
    # Ask first name.
    first_name = input("First name: ")
    # Ask last name.
    last_name = input("Last name: ")
    # Create the user.
    create_user(id, username, first_name, last_name)


# Main program.
while True:
    option = input("Create new user (Y/N)? ")
    if option.upper() == 'Y':
        ask_user_info()
        print()
    elif option.upper() == 'N':
        print()
        break
    else:
        print("Invalid option.")
        print()

# Print users ordered by username.
users.sort(key=lambda user: user['username'])
sep = '-' * 25
for user in users:
    print(sep)
    print(f"ID: {user['id']}")
    print(f"Username: {user['username']}")
    print(f"First name: {user['first_name']}")
    print(f"Last name: {user['last_name']}")
else:
    print(sep)
