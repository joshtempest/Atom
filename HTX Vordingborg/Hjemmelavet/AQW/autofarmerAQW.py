import pyautogui as pag
import time
import threading


time.sleep(5)


def b():
    while True:
        pag.press('2')
        time.sleep(4)

def a():
    while True:
        pag.press('5')
        time.sleep(0.6)
        pag.press('5')
        time.sleep(10)
def c():
    while True:
        pag.press('1')
        time.sleep(0.1)
def d():
    while True:
    #Quest selcetion
        pag.click(400, 290)
        time.sleep(1.5)
    #Turn In and accept
        pag.click(334, 840)
        time.sleep(1.5)


threading.Thread(target=a).start()
threading.Thread(target=b).start()
#threading.Thread(target=c).start()
#threading.Thread(target=d).start()
