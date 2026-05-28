# ============================================
# SECURE ONLINE VOTING SYSTEM USING PYTHON
# ============================================

import random

# Candidate Database
candidates = {"Alice": 0,"Bob": 0,"Charlie": 0,"Bobby": 0,"Max": 0}

# Registered Users
users = {"voter1": {"password": "pass1","voted": False},"voter2": {"password": "pass2","voted": False},
         "voter3": {"password": "pass3","voted": False},"voter4": {"password": "pass4","voted": False},
         "voter5": {"password": "pass5","voted": False}}

# Function to Display System Features
def show_features():

    print("\n======================================")
    print(" ONLINE VOTING SYSTEM FEATURES")
    print("======================================")


# Function for Login Authentication
def login():

    username = input("\nEnter Username: ")
    password = input("Enter Password: ")

    # Check username and password
    if username in users and users[username]["password"] == password:

        print("\nPassword Verified Successfully!")

        # Generate OTP
        otp = random.randint(1000, 9999)

        print("Generated OTP:", otp)

        user_otp = int(input("Enter OTP: "))

        if user_otp == otp:
            print("Authentication Successful!")
            return username

        else:
            print("Invalid OTP!")
            return None

    else:
        print("Invalid Username or Password!")
        return None


# Function to Display Candidates
def show_candidates():

    print("\n===== Candidate List =====")

    for candidate in candidates:
        print("-", candidate)


# Function for Voting
def vote(username):

    # Check if already voted
    if users[username]["voted"] == True:
        print("\nYou Have Already Voted!")
        return

    show_candidates()

    choice = input("\nEnter Candidate Name: ")

    # Vote Counting
    if choice in candidates:

        candidates[choice] += 1

        users[username]["voted"] = True

        print("\nVote Cast Successfully!")
        print("Thank You for Participating in Online Voting.")

    else:
        print("Invalid Candidate Name!")


# Function to Display Results
def results():

    print("\n======================================")
    print("          ELECTION RESULTS")
    print("======================================")

    for candidate, votes in candidates.items():
        print(candidate, ":", votes, "Votes")


# Main Program
show_features()

while True:

    print("\n======================================")
    print("      ONLINE VOTING SYSTEM")
    print("======================================")

    print("1. Login and Vote")
    print("2. View Results")
    print("3. Exit")

    option = input("\nEnter Your Choice: ")

    # Login and Vote
    if option == "1":

        user = login()

        if user:
            vote(user)

    # View Results
    elif option == "2":
        results()

    # Exit Program
    elif option == "3":

        print("\nExiting Online Voting System...")
        print("Voting can be done anytime and from anywhere.")
        break

    # Invalid Option
    else:
        print("Invalid Choice! Please Try Again.")