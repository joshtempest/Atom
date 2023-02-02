import bcrypt


#password = input("Please enter your password: ").encode("utf-8")

def login(name, password):
    success = False
    file = open('user_details.txt','r')
    for i in file:
        a, b = i.split(',')
        if(a==name):
            b.encode('utf-8')
            if bcrypt.checkpw(b, password):
                success = True
                break
    file.close()
    if(success):
        print('Login Successfull!')
    else:
        print('wrong username or password')

def register(name, Hpassword, password):
     file = open('user_details.txt','a')
     file.write(name + ',' + str(Hpassword))
     file.close()

def access(option):
    if (option == 'login'):
        name = input('Enter your username or email: ')
        password = input('Enter your password: ').encode('utf-8')
        login(name, password)
    else:
        print('Enter your information to register')
        name = input('Enter your username or email: ')
        password = input('Enter your password: ').encode("utf-8")
        Hpassword = bcrypt.hashpw(password, bcrypt.gensalt())
        register(name, Hpassword, password)


def begin():
    global option
    option = input('Login or Register (login,reg):')
    if (option != "login" and option != "reg"):
        begin()
begin()
access(option)
