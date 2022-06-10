import keyboard
import time
shots = 0
repeats = 1
running = True

while running == True:
    if shots == 0 and repeats == 1:
        print('out of ammo, press r to reload')
        repeats = 0
    if keyboard.is_pressed('esc'):
        exit()
    if keyboard.is_pressed("r"):x
        print('reloaded')
        shots = 6
        repeats = 1
    while shots != 0:
        if keyboard.is_pressed("space"):
            print("bang!")
            shots = shots - 1
            time.sleep(0.3)
