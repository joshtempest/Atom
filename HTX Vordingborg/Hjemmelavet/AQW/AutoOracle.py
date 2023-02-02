import time
import pyautogui as pag
import threading

time.sleep(5)

def a():
    while True:
        pag.press('3')
        time.sleep(0.6)
        pag.press('3')
        time.sleep(15)

def b():
    while True:
        pag.press('5')
        time.sleep(0.6)
        pag.press('5')
        time.sleep(12)

def c():
    while True:
        pag.press('2')
        time.sleep(0.6)
        pag.press('2')
        time.sleep(8)
#  UwU
def d():
    while True:
        pag.press('4')
        time.sleep(0.6)
        pag.press('4')
        time.sleep(14)

#threading.Thread(target=a).start()
threading.Thread(target=b).start()
threading.Thread(target=d).start()
time.sleep(1)
threading.Thread(target=c).start()
