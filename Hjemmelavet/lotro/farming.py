import keyboard as key
import time
import pyautogui as pag

def farming(times):#, selection):
    while times >= 1:
        times = times - 1
        #crop(selection)
        quantity()
        harvest()
        time.sleep(2)
    print('done with farming')
    exit()

def crop(selection):
    pag.click(1160, 112)
    time.sleep(0.5)
    if selection == "apprentice" or selection == 'appr':
        pag.moveTo(1140, 130)
        pag.click()
        time.sleep(1)
        pag.moveTo(1150, 217)
        pag.click()
        time.sleep(1)
        pag.moveTo(1246, 260)
        pag.click()
        time.sleep(1)
    elif selection == 'journeyman' or selection == 'jour':
        pag.moveTo(1140, 150)
        pag.click()
        time.sleep(0.5)
        pag.moveTo(1150, 187)
        pag.click()
        time.sleep(0.5)
        pag.moveTo(1200, 223)
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
    cropsRemaining = 5
    harvesting = True
    time.sleep(0.5)
    while harvesting == True:
        if cropsRemaining != 0:
            cropsRemaining = cropsRemaining - 1
            key.press_and_release('y')
            time.sleep(0.5)
            key.press_and_release('g')
            time.sleep(0.5)
        else:
            harvesting = False
            time.sleep(30)
            return

def start():
    seeds = int(input('how many seeds? '))
    calcSeed = seeds - seeds%5
    repeats = calcSeed/5
    #selection = input('apprentice(appr), journeyman(jour)? ')
    running = True
    print('Do not have more than 99 in quantity and have your craft closed, to start press t')
    while running == True:
        if key.is_pressed('t'):
            print('go to the game')
            time.sleep(5)
            farming(repeats)#, selection)
            running = False
        if key.is_pressed('esc'):
            exit()
start()
