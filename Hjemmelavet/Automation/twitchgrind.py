import keyboard as kb
import pyautogui as pag
import time

run = False
program = True

while program == True:
    if kb.is_pressed('esc'):
        program = False
        exit()
    if kb.is_pressed('p'):
        run = True
    while run == True:
        if kb.is_pressed('esc'):
            run = False
        print('click')
        pag.click()
        time.sleep(5)
