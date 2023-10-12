from threading import Thread as thd
import keyboard as keyb

run = True

def counter():
    count=0
    while thread2.is_alive():
        print(count)
        count+=1

def interupt():
    keyb.wait('esc')
    print('interupted')

thread1 = thd(target = counter)
thread2 = thd(target = interupt)
thread2.start()
thread1.start()
