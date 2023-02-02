log=[["josh","why"],["tempest","k"]]
while True:
    if input("Username: ") in log:
        while True:
            if input("password: ") in log:
                print("velkommen")
                break
            else:
                print("forkert, prøv igen")
        break
    else:
        print("forkert, prøv igen")
