import bcrypt
import hashlib
import keyboard



def register ():
    salt = bcrypt.gensalt()
    print('Making a user')
    user = input('Navn: ').encode()
    hashed = bcrypt.hashpw(input('password: ').encode('utf-8'), salt)
    file = open('user_details.txt','ab')
    file.write(user + b',' + hashed + b',' + salt + b'\n')
    file.close()
    logreg()

def logincheck (logname):
    file = open('user_details.txt','rb')
    for i in file:
        linje = i.split(b'\n')
        print(linje)
        for linje in i:
            i.replace(b'\n',b'')
            user, hashed, salt = i.split(b',', -1)
            
    if logname in user:
        logpass = bcrypt.hashpw(input('password: ').encode('utf-8'), salt)
        while True:
            if logpass == hashed:
                print('Login succesful! Welcome')
                file.close()
                break
            else:
                print("password incorrect, try again")
                logpass = bcrypt.hashpw(input('password: ').encode('utf-8'), salt)
    else:
        login()


def logreg():
    loginregist = input('log/reg? ')
    if loginregist == 'log':
        print('Du er ved at logge ind')
        login()
    elif loginregist == 'reg':
        register()
    else:
        logreg()

def login():
    logname = input('Navn: ').encode()
    logincheck(logname)


logreg()
