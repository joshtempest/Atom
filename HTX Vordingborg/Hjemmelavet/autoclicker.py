import pyautogui as pag
import keyboard as kb
import threading
import time



def autoclicker():
    time.sleep(0.2)
    while True:
        pag.click()
        print('click')
        #time.sleep(2)

threading.Thread(target=autoclicker).start()
#threading.Thread(target=stop).start()
