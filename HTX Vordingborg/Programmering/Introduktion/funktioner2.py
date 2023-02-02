alias = None
enemy = None
greeting = None

def getInput():
    user = input("What is your name, user? ")
    if user == "" or user == None:
        user = getInput()
    return user

def setUserVars(anAlias, anEnemy, aGreeting):
    global alias, enemy, greeting
    alias = anAlias
    enemy = anEnemy
    greeting = aGreeting


def greetUser(greetWord):
    return "{} {}. {}. Good luck defeating {}!".format(greetWord, alias, greeting, enemy)

if __name__ == '__main__':
    user = getInput()

    if user == "Bruce Wayne":
        setUserVars("Batman", "The Joker", "You are the hero Gotham deserves, but not the one it needs right now")
    elif user == "Katniss Everdeen":
        setUserVars("Mockingjay", "President Snow", "May the odds be ever in your favour")
    elif user == "Peter Parker":
        setUserVars("Spiderman","Green Goblin","You are an Avenger now!")
    elif user == "Bruce Banner":
        setUserVars("Hulk","it","Please don't be angry, and")
    elif user == "Tony Stark":
        setUserVars("Iron Man","Thanos","Welcome the smartest Avenger")
    elif user == "Kyle Rayner":
        setUserVars("Green and blue lantern","the red lanterns","May you have the will to keep up hope")
    elif user == "Josh the Tempest":
        setUserVars("The Traveller of Worlds","whoever means your friends harm","Welcome Tempest")
    else:
        setUserVars("Programmer", "The Compiler", "You are the 5%")

    print(greetUser('Welcome'))
