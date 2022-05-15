import keyboard as key
import time
import pyautogui as pag

def farming(times):
    while times >= 1:
        times = times - 1
        print(times)
        crop()
        quantity()
        harvest()
        time.sleep(1)
    print('done with farming')
    exit()

def crop():
    pag.click(1246, 282)
    time.sleep(1)
    pag.click()
    time.sleep(0.5)

def quantity():
    pag.tripleClick(1735, 555)
    time.sleep(1)
    pag.click()
    time.sleep(0.5)
    key.press_and_release('backspace')
    key.press_and_release('backspace')
    time.sleep(0.5)
    pag.write('5')
    time.sleep(1)
    pag.doubleClick(1815, 555)
    time.sleep(0.5)
    pag.click()
    time.sleep(10)

def harvest():
    pag.click(1000, 200)
    pag.click()
    time.sleep(0.5)
    harvesting = 0
    while harvesting <= 5:
        key.press_and_release('y')
        time.sleep(0.5)
        key.press_and_release('g')
        harvesting = harvesting + 1
        print(harvesting)
        time.sleep(9)

def start():
    seeds = int(input('how many seeds? '))
    calcSeed = seeds - seeds%5
    print(calcSeed)
    repeats = calcSeed/5
    print(repeats)
    running = True
    print('Do not have more than 99 in quantity and have your craft closed, to start press t')
    while running == True:
        if key.is_pressed('t'):
            print('go to the game')
            time.sleep(5)
            farming(repeats)
            running = False
        if key.is_pressed('esc'):
            exit()
start()
