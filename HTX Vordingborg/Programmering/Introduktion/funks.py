def getInput():
    user = input("What is your name, user? ")
    if user == "" or user == None:
        user = getInput()
    else:
        return user

alias = None
enemy = None
greeting = None

def setUserVars(anAlias, anEnemy, aGreeting):
    global alias, enemy, greeting
    alias = anAlias
    enemy = anEnemy
    greeting = aGreeting
