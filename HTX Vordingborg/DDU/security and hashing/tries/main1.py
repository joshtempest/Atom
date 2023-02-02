import bcrypt


#password = input("Please enter your password: ").encode("utf-8")

def login(name, checkword):
    success = False
    file = open('user_details.txt','r')
    for i in file:
        #print(i.split(','))
        a, b = i.split(',')
        if(a==name):
            b.encode('utf-8')
            #password.encode('utf-8')
            if bcrypt.checkpw(b, checkword):
                success = True
                break
    file.close()
    if(success):
        print('Login Successfull!')
    else:
        print('wrong username or password')

def register(name, Hpassword):
     file = open('user_details.txt','a')
     file.write(name + ',' + str(Hpassword))
     file.close()

def access(option):
    if (option == 'log'):
        name = input('Enter your username or email: ')
        chpassword = input('Enter your password: ').encode('utf-8')
        checkword = bcrypt.hashpw(chpassword, bcrypt.gensalt())
        login(name, checkword)
    else:
        print('Enter your information to register')
        name = input('Enter your username or email: ')
        password = input('Enter your password: ').encode("utf-8")
        Hpassword = bcrypt.hashpw(password, bcrypt.gensalt())
        register(name, Hpassword)

def begin():
    global option
    option = input('Login or Register (log, reg):')
    if (option != "log" and option != "reg"):
        begin()

begin()
access(option)
