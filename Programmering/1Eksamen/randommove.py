import random
enemies = ["Atom", "Birb","Python"]
enemy = random.choice(enemies)

if enemy == "Atom":
    moves = [2,3,4]
    move = random.choice(moves)
if enemy == "Birb":
    moves = [1,5]
    move = random.choice(moves)
if enemy == "Python":
    moves = [2,3,4]
    move = random.choice(moves)

print("A wild " + enemy + " appeared")

if move == 1:
    print(enemy + " used kick!")
    print('It dealt 20 dmg')
elif move == 2:
    print(enemy + " used bug!")
    print("Does critical dmg")
    print('Took 99999999999999 dmg')
elif move == 3:
    print(enemy + " crashed")
    print("You won the battle")
elif move == 4:
    print(enemy + " used error")
    print("does 45 dmg")
elif move == 5:
    print(enemy + " used schreech")
    print("You take 5 dmg")
    print("You do 10% less dmg next attack")
