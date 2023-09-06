import pyautogui as pag
import time

time.sleep(3)

while True:
    pag.moveTo(780, 1040)
    print('move')
    time.sleep(1)
    pag.click()
    print('click')
    time.sleep(9)
