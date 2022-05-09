import pyautogui as pag
import time
import threading

time.sleep(5)

while True:
    pag.press('4')
    time.sleep(0.3)
    pag.press('1')
    pag.click(842, 770)
