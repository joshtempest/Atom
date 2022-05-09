import time

tal = 1;
bumtal = int(input("Hvad skal bumtallet være? "))

def checkForBum(tal, bumtal):
    if tal%bumtal == 0:
        return True
    elif str(bumtal) in str(tal):
        return True
    else:
        return False


while tal < 23456:
    if checkForBum(tal, bumtal) == True:
        print("BUM")
    else:
        print(tal)
    tal=tal+1
    #time.sleep(0.5)
