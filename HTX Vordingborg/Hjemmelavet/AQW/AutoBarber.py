import pyautogui as pag
import time
import threading

time.sleep(5)
pag.click()
time.sleep(1)
pag.press("1")

def a():
    while True:
        pag.press('2')
        time.sleep(0.6)
        pag.press('2')
        time.sleep(3)

def b():
    while True:
        pag.press('3')
        time.sleep(0.6)
        pag.press('3')
        time.sleep(5)



threading.Thread(target=a).start()
threading.Thread(target=b).start()
