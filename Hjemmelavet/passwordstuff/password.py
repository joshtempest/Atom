log=[["josh","why"],["tempest","k"]]
while(True):
    if input("Brugernavn:") in log:
        while True:
            if input("Kodeord: ") in log:
                print("velkommen")
                break
            else:
                print("forkert prøv igen")
        break
    else:
        print("forkert, prøv igen")
