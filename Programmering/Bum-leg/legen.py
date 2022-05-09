import time

tal = 1;
bumtal = int(input("Hvad skal bumtallet være? "))
spiller = 1

def checkForBum(tal, bumtal):
    if tal%bumtal == 0:
        return True
    elif str(bumtal) in str(tal):
        return True
    else:
        return False

def bygBumListe():
    bummer=[]
    nyBum=None
    while nyBum!='':
        nyBum=input('Skriv bumtal')
        if nyBum.isdigit():
            bummer.append(int(nyBum))
    return bummer

bumListe=bygBumListe()

while tal < 51:
    valg=input('tal eller BUM? ')
    if checkForBum(tal, bumtal):
        korrekt="BUM"
    else:
        korrekt=str(tal)
    if valg==korrekt:
        print("YAY!")
    else:
        print("BUH!")
    if checkForBum(tal, bumtal) == True:
        print("BUM")
    else:
        print(tal)
    tal=tal+1
    if spiller ==1:
        spiller = 2
    else:
        spiller=1
    time.sleep(0.5)
