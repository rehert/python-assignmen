# Demonstration of Variables, Constant, and Print function in a Login System

# A constant (the SYSTEM NAME has fixed value that should not change)
SYSTEM_NAME = "Secure Login System"

# Variables (store values entered by the user - these can change)
username = input('Enter username: ')
password = input('Enter password: ')

if username == "Tatenda" and password == "12345678":
    # Print() is used to display messages on the screen
    print("Welcome to", SYSTEM_NAME)
    print("Access granted!")
else:
    print("Access denied! Please try again.")
