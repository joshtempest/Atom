import mouse
import time
from threading import Thread as thd
import keyboard as keyb

time.sleep(5)

run = True

def clicker():



def interupt():
    keyb.wait('esc')
    print('interupted')

thread1 = thd(target = clicker)
thread2 = thd(target = interupt)
thread2.start()
thread1.start()
#993,556 979,571
