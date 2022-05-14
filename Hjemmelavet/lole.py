import keyboard as key
import time as T

run = 1
running = True

while running == True:
    if key.is_pressed('e'):
        run += -run
    if key.is_pressed('esc'):
        running = False
    while run == 1:
        key.press('2')
