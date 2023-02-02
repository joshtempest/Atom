import bcrypt

password = "mik"



success = False
file = open('user_details.txt','r')
for i in file:
    user, hash, salt = i.split(',')
    print(f"user = {user},hash= {hash}, salt={salt}")
    

file.close()
