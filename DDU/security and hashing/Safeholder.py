import bcrypt
import hashlib

salt = b'$2b$12$8gppykpvjYHUlqNeJXvI7e'

def register ():
    print('Making a user')
    user = input('Navn: ').encode()
    hashed = bcrypt.hashpw(input('password: ').encode('utf-8'), salt)
    file = open('user_details.txt','ab')
    file.write(user + b',' + hashed + b',' + salt + b'\n')
    file.close()
    logreg()

def logincheck (logname, logpass):
    file = open('user_details.txt','rb')
    for i in file:
        user, hashed, salt = i.split(b',')
    checked = bcrypt.checkpw(logpass, hashed)
    file.close()
    print(checked)
    if checked == False:
        print("username or password is incorrect, try again")
        login()
    else:
        print('Login succesful! Welcome')

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
    logname = input('Navn: ')
    logpass = bcrypt.hashpw(input('password: ').encode('utf-8'), salt)
    logincheck(logname, logpass)


logreg()
