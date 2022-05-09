import time

tal = 1; #Variablen er til senere, for at starte ved tallet 1 i stedet for 0
spiller = 1 #Variablen er til, for at holde styr på spillerens tur

def checkForBum(tal, bumtal): #Begyndelsen på definationen
    if tal%bumtal == 0: #Modulo checker størrelsen på resten når man dividerer, så hvis den rest er 0 går bumtalet op i talet
        return True #hvis resten var 0 giver checkForBum resultatet true som bruges senere
    elif str(bumtal) in str(tal): #checker om bumtalet er i tallet
        return True
    else:
        return False #Hvis ingen af tingene går op, er checkForBum false

def bygBumListe(): #Dette skal bruges for at have flere bumtal
    bummer=[] #Her oprettes listen
    nyBum=None #Her laves en variabel til senere brug
    while nyBum!='':
        nyBum=input('Skriv bumtal')
        if nyBum.isdigit():
            bummer.append(int(nyBum))
#Sørger for at det du skriver er et tal og er noget
    return bummer

bumListe=bygBumListe()

while tal < 51: #
    valg=input('tal eller BUM? ')
    for bumtal in bumListe:
        if checkForBum(tal, bumtal):
            korrekt="BUM"
        else:
            korrekt=str(tal)
        if korrekt =='BUM':
            break
    if valg==korrekt:
        print("YAY!")
    else:
        print("BUH!")
    tal=tal+1
    if spiller ==1:
        spiller = 2
    else:
        spiller=1
    time.sleep(0.5)
