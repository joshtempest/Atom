alias = None
enemy = None
greeting = None

user = input("What is your name, user? ")

if user == "Bruce Wayne":
    alias = "Batman"
    enemy = "The Joker"
    greeting = "You are the hero Gotham deserves, but not the one it needs right now."
elif user == "Katniss Everdeen":
    alias = "Mockingjay"
    enemy = "President Snow"
    greeting = "May the odds be ever in your favour!"
elif user == "Peter Parker":
    alias = "Spiderman"
    enemy = "Green Goblin"
    greeting = "You are an Avenger now!"
elif user == "Bruce Banner":
    alias = "Hulk"
    enemy = "it"
    greeting = "Please don't be angry, and"
elif user == "Tony Stark":
    alias = "Iron Man"
    enemy = "Thanos"
    greeting = "Welcome the smartest Avenger."
elif user == "Kyle Rayner":
    alias = "Green and blue Lantern"
    enemy = "the red lanterns"
    greeting = "May you have the will to keep up hope and"
elif user == "Josh the Tempest":
    alias = "The traveller of worlds"
    enemy = "whoever means your friends harm"
    greeting = "Welcome Tempest and"
else:
    alias = "programmer"
    enemy = "the compiler"
    greeting = "You are the 1%."

print("Greetings {}. {} Good luck defeating {}.".format(alias, greeting, enemy))
