log=[["josh","why"],["tempest","k"]]
usernameslist=log
def login():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    for i in range(len(usernameslist)):
        if username == i and password == i:
            print("Access granted!")
        else:
            print("Incorrect Login credentials, please try again.")
login()
