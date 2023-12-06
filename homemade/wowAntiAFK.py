import keyboard as keyb
import mouse as mse
import time
from threading import Thread as thd
import pyautogui as pag

def interupt():
    keyb.wait('esc')
    print('interupted')

def AntiAFK():
    while thread2.is_alive():
        pag.moveTo(340,980)
        mse.click()
        time.sleep(8)

def AntiAFK2():
    while thread2.is_alive():
        pag.moveTo(1880, 900)
        mse.click()
        time.sleep(100)

thread1 = thd(target = AntiAFK)
thread2 = thd(target = interupt)
thread3 = thd(target = AntiAFK2)

time.sleep(4)

thread2.start()
thread3.start()
thread1.start()
