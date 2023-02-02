import pyautogui as pag
import time

time.sleep(10)
pag.click()
time.sleep(0.5)
pag.mouseDown(button="right")
time.sleep(3)
pag.mouseUp(button="right")
time.sleep(1)
pag.click()
