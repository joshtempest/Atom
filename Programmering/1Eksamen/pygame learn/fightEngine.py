# import the pygame module, so you can use it, keyboard to check for input, random to randomise enemy and its move and to add a delay when necessary
import pygame
import keyboard
import random
import time

# initialize the pygame module
pygame.init()

#Makes a variable hold RGB values to make objects transparent
transparent = (0, 0, 0, 0)
#Defines player health to start the game with
PlayerHP = 200
#height and width of screen defined
screen_width = 1000
screen_height = 1000
#Defines a text font, needed to write text on the screen
Text = pygame.font.SysFont(None, 32)
#Pixel position for text, to have close to centered text
textH = 500
textW = 400

#Define a main function
def main():
    #Pygame needs a defined screen to show what happens
    screen = pygame.display.set_mode((screen_width, screen_height))
    #Allows us to open png
    pygame.image.get_extended()
    #load and set the logo
    logo = pygame.image.load("vine-1948358__480.png")
    pygame.display.set_icon(logo)
    #Gives a title
    pygame.display.set_caption("Fighting Engine")
    #Starts the pygame
    running = True
    #Then we load and display the player and an enemy, right after filling the screen in colour
    image = pygame.image.load("player.png")
    enemiage = pygame.image.load("enemy.png")
    screen.fill((109, 136, 157))
    screen.blit(image, (250, 250))
    screen.blit(enemiage, (500, 500))
    pygame.display.flip()

    #Defines the parameters of movement for player
    xpos = 25
    ypos = 25
    step_x = 0.8
    step_y = 0.8

        # main loop
    while running:
        #This stops player movement so they don't run of screen
        if xpos > screen_width - 40:
            xpos = screen_width - 40
        if xpos < 0:
            xpos = 0
        if ypos > screen_height - 40:
            ypos = screen_height - 40
        if ypos < 0:
            ypos = 0

        #Starts combat if the player enters these coordinats, to test the combat system
        if 500 <= xpos <= 550 and 500 <= ypos <= 550:
            combat()


    # Update the position of the smiley
        if keyboard.is_pressed('d') or keyboard.is_pressed('right arrow'):
            xpos += step_x # move it to the right
        if keyboard.is_pressed('s') or keyboard.is_pressed('down arrow'):
            ypos += step_y # move it down
        if keyboard.is_pressed('a') or keyboard.is_pressed('left arrow'):
            xpos += -step_x # move it to the left
        if keyboard.is_pressed('w') or keyboard.is_pressed('up arrow'):
            ypos += -step_y # move it up
            #Checks if escape is pressed to end the game
        if keyboard.is_pressed('esc'):
            running = False
        #To update the screen so you know what happens, we fill the screen, then put in the player in its correct position and the enemy
        screen.fill((109, 136, 157))
        screen.blit(image, (xpos, ypos))
        screen.blit(enemiage, (500, 500))
        pygame.display.flip()
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

#Makes a new screen specifically for combat
cscreen = pygame.display.set_mode((screen_width, screen_height))


def combat():
    #A list of enemies to randomly be chosen when combat is called
    enemies = ["Atom", "Birb", "Python"]
    enemy = random.choice(enemies)
    enemy = "Birb"
    #Depending on which enemy it is, health is defined to fit
    if enemy == "Atom":
        enemyHP = 120
    elif enemy == "Birb":
        enemyHP = 80
    elif enemy == "Python":
        enemyHP = 160
    #Shows on screen which enemy you're going to face
    appear = Text.render(("A wild " + enemy + " appeared"), True, pygame.Color('white'))
    cscreen.blit(appear, (textW, textH))
    pygame.display.flip()
    #After 2 seconds we "reset" the screen to make room for the other info needed in combat
    time.sleep(2)
    cscreen.fill(transparent)
    pygame.display.flip()
    #Starts combat running loop
    crunning = True
    #Makes a variable for enemy health that can be changed
    currentEHP = enemyHP
    #gives 0.5 second delay, to fix a chrashing problem.
    time.sleep(0.5)
    #Starts combat loop
    while crunning == True:
        #"failsafe" to end the game if necessary
        if keyboard.is_pressed('esc'):
            crunning = False
        #Loads a specific fun image found on the internet
        fimage = pygame.image.load("combat-zone.png")
        #Loads a picture of enemy to show what you are fighting, meant to be different depending on what you fight. However the pictures filled everything
        #hence the map sprite for enemy is used
        enemypicture = pygame.image.load("enemy.png")#enemy + ".png")
        #Puts the two pictures on the screen and shows them
        cscreen.blit(fimage, (screen_width - 220, screen_height - 410))
        cscreen.blit(enemypicture, (screen_width - 1000, screen_height - 1000))
        pygame.display.flip()
        #Gets enemys current health and dmg modifier from playerattack function which needs current health
        currentEHP, DMGModifier = playerAttack(currentEHP)
        #Checks to see if enemy health is over zero and gives the enemy its turn.
        if currentEHP > 0:
            enemyAttack(enemy)
        #If enemy is dead victory screen is loaded after screen "reset" and combat is stopped
        else:
            cscreen.fill(transparent)
            Vic = Text.render(("You have won! Congratulations!"), True, pygame.Color('gold'))
            cscreen.blit(Vic, (textW, textH))
            pygame.display.flip()
            time.sleep(2)
            crunning = False

def playerAttack(currentEHP):
    #sets variables to be used
    playerDMG = 0
    enemyDMG = 0
    dmgMultiplier = 1
    enemyHP = currentEHP
    #Starts move choice loop
    while True:
        #Failsafe again
        if keyboard.is_pressed('esc'):
            crunning = False
        #Tells you which buttons to press
        moveChoice = Text.render(("Choose your move (1, 2, 3, 4)"), True, pygame.Color('white'))
        #Shows how much health the enemy has left
        ehp = Text.render('Enemy HP: ' + (str(enemyHP)), True, pygame.Color('white'))
        #Displays the previous texts
        cscreen.blit(ehp, (textW, 100))
        cscreen.blit(moveChoice, (textW, textH))
        pygame.display.flip()
        cscreen.fill(transparent)
        #Loads and displays the enemy you are facing
        enemypicture = pygame.image.load("enemy.png")
        cscreen.blit(enemypicture,(screen_width - 1000, screen_height - 1000))
        #Detects if 1,2,3 or 4 is being pressed and makes that move accordingly
        if keyboard.is_pressed("1"):
            #loads player move
            playerMove = Text.render(("You punched"), True, pygame.Color('white'))
            playerDMG = 30
            #calculates how much health the enemy will have left after the attack
            enemyHP = enemyHP - playerDMG
            #loads the dmg amout of the attack
            dmgtext = Text.render(("It did " + str(playerDMG) + " dmg"), True, pygame.Color('white'))
            #displays the move and the dmg for a second
            cscreen.blit(playerMove, (textW, textH))
            cscreen.blit(dmgtext, (textW, textH + 50))
            pygame.display.flip()
            time.sleep(1)
            #Returns the amount of health the enemy has left and the dmg multiplier for the opcoming attack from the enemy
            return enemyHP, 1
        #Does the same thing as the above, except more dmg
        elif keyboard.is_pressed("2"):
            playerMove = Text.render(("You kicked"), True, pygame.Color('white'))
            playerDMG = 40
            enemyHP = enemyHP - playerDMG
            dmgtext = Text.render(("It did " + str(playerDMG) + " dmg"), True , pygame.Color('white'))
            cscreen.blit(playerMove, (textW, textH))
            cscreen.blit(dmgtext, (textW, textH + 50))
            pygame.display.flip()
            time.sleep(1)
            return enemyHP, 1
        #Again the same, except less dmg and a different dmg multiplier
        elif keyboard.is_pressed("3"):
            playerMove = Text.render(("You screamed"), True, pygame.Color('white'))
            dmgMultipliertext = Text.render(("Enemy will do 10% less dmg next attack"), True, pygame.Color('white'))
            playerDMG = 15
            enemyHP = enemyHP - playerDMG
            dmgtext = Text.render(("It did " + str(playerDMG) + " dmg"), True, pygame.Color('white'))
            dmgMultiplier = 0.9
            cscreen.blit(playerMove, (textW, textH))
            cscreen.blit(dmgtext, (textW, textH + 50))
            cscreen.blit(dmgMultipliertext, (textW, textH + 100))
            pygame.display.flip()
            time.sleep(1)
            return enemyHP, dmgMultiplier
        #This move doesn't deal dmg but heavily reduces dmg taken
        elif keyboard.is_pressed("4"):
            playerMove = Text.render(("You defended yourself"), True, pygame.Color('white'))
            dmgtext = Text.render(("You take 90% less dmg"), True, pygame.Color('white'))
            cscreen.blit(playerMove, (textW, textH))
            cscreen.blit(dmgtext, (textW, textH + 50))
            pygame.display.flip()
            dmgMultiplier = 0.1
            time.sleep(1)
            crunning = False
            return enemyHP, dmgMultiplier

def enemyAttack(enemy):
    #Dependent on the enemy a list of possible attack is made and a random one is selected
    if enemy == "Atom":
        moves = [2,3,4]
        move = random.choice(moves)
    elif enemy == "Birb":
        moves = [1,5]
        move = random.choice(moves)
    elif enemy == "Python":
        moves = [2,3,4]
        move = random.choice(moves)
    #
    if move == 1 or move == 5:
        emove = Text.render((enemy + " used kick!"), True, pygame.Color('white'))
        edmg = Text.render(('It dealt 20 dmg'), True, pygame.Color('red'))
        enemyDMG = 20
        cscreen.blit(emove, (textW, textH))
        cscreen.blit(edmg, (textW, textH + 50))
        pygame.display.flip()
        time.sleep(2)
        return enemyDMG
"""    elif move == 2:
        print(enemy + " used bug!")
        print("Does critical dmg")
        print('Took 40 dmg')
    elif move == 3:
        print(enemy + " crashed")
        print("You won the battle")
    elif move == 4:
        print(enemy + " used error")
        print("does 45 dmg")
    elif move == 5:
        print(enemy + " used schreech")
        print("You take 5 dmg")
        #print("You do 10% less dmg next attack")
"""

# run the main function only if this module is executed as the main scripts
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
    #combat()
