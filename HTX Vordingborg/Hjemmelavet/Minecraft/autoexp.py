"""
Before you use this script make sure to have your weapon in hand and food in offhand
"""

import pyautogui as pag #Imports the needed components
import time

time.sleep(4) #Gives you some time to enter the game
x=0 #Sets a variable to use for counting

while True: #Runs forever, or at least until you stop it
    time.sleep(0.4) #Set here to make it more smooth and to make sure you get all attacks in
    pag.click() #Makes you attack
    time.sleep(2) #To make sure we get the AOE attacks
    x=x+1 #Gives a one up to the variable from earlier, to count how many swing we have taken
    if x==60: #When the count reaches 60....
        pag.mouseDown(button="right") #.... we hold right click down...
        time.sleep(3) #.... for a couple of seconds, so we can eat
        pag.mouseUp(button="right") #Makes it stop holding right click so you can attack again
        x=0 #resets the variable, so we can count over
        time.sleep(0.4) #Gives a little delay, again for smooth transition and to get all attacks in
