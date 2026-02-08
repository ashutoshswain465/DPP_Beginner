username = input(f"Enter username: ")

if 5 <= len(username) <= 15:
    if username.isalnum():
        if username[0].isalpha():
            print("Valid username.")
        else:
            print("Invalid username: First character of username should be an alphabet")
    else:
        print("Invalid username: Only letters and numbers are allowed.")
else:
    print("Invalid username: Username length should be in between 5 and 15 characters")
