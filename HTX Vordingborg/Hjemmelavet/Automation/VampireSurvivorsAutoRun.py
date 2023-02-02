import pyautogui as pag
import time
import keyboard as keyb

time.sleep(3)
while True:
    pag.keyDown('s')
    pag.press('space')
    if keyb.is_pressed('esc'):
        break
