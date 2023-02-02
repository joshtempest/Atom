import bcrypt
import hashlib

#newsalt = b'$2b$12$pPxLWNBj5MI.IgJJ3IC7S.'
#password = input("Please enter your password: ").encode("utf-8")

def login(name, password):
    success = False
    file = open('user_details.txt','r')
    for i in file:
        user, hash, salt = i.split(',')
        if(user==name):
            #password = password.encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), hash):
                success = True
                break
    file.close()
    if(success):
        print('Login Successfull!')
    else:
        print('wrong username or password')

def register(name, Hpassword, salt):
     file = open('user_details.txt','a')
     print(name)
     print(Hpassword)
     print(salt)
     file.write(name + ',' + str(Hpassword))# + ','+ str(salt) + '\n')
     file.close()

def access(option):
    if (option == 'log'):
        name = input('Enter your username or email: ')
        password = input('Enter your password: ').encode('utf-8')
        #password = password.encode('utf-8')
        #enpassword = bcrypt.hashpw(password, salt=newsalt)
        login(name, password)
    else:
        print('Enter your information to register')
        name = input('Enter your username or email: ')
        password = input('Enter your password: ').encode("utf-8")
        newsalt = bcrypt.gensalt()
        Hpassword = bcrypt.hashpw(password, salt=newsalt)
        register(name, Hpassword, newsalt)

def begin():
    global option
    option = input('Login or Register (log,reg):')
    if (option != "log" and option != "reg"):
        begin()
begin()
access(option)
