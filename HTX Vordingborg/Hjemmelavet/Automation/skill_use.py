import time
import pyautogui as pag

x = 0
while x <  50:
    pag.keyDown('1')
    time.sleep(1)
    pag.keyUp('1')
    time.sleep(11)
    x = x + 1
