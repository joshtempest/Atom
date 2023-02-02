import bcrypt

regList = {"josh":"buss"}

def registrer():
    brugernavn = input('Brugernavn: ')
    if brugernavn in regList:
        print('brugernavn allerede i brug')
        registrer()
    else:
        kode = input('Kode: ')
        regList.append(brugernavn:kode)
        print(regList)
        print('Du er nu registreret, velkommen')
        start()

def tri():
    svar = input('Prøv igen? (y/n) ')
    if svar == 'y':
        login()
    elif svar == 'n':
        start()
    else:
        tri()

def login():
    logNavn = input('Navn: ')
    if logNavn in regList:
        logKode = input('Kode: ')
        if logKode in regList:
            print('Velkommen ' + logNavn)
    else:
        print('Forkert brugernavn')
        tri()

def start():
    valg = input('Login eller registrer? (log/reg) ')
    if valg == "log" or valg == "reg":
        if valg == "log":
            login()
        elif valg == 'reg':
            registrer()
    else:
        start()

start()
