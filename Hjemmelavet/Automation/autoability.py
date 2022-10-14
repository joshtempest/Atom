import threading
import pyautogui as pag
import time

x = 0
y = 0

time.sleep(5)

def a():
    x = 0
    while x <= 4:
        pag.keyDown('leftshift')
        pag.press('8')
        time.sleep(0.5)
        pag.keyUp('leftshift')
        x = x + 1
        time.sleep(1800)

def b():
    y = 0
    while y <= 11:
        time.sleep(2)
        print('being used')
        pag.hotkey('shift','6')
        y = y + 1
        time.sleep(120)

#threading.Thread(target = a).start()
threading.Thread(target = b).start()
