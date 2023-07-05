import pyautogui as pag;
import keyboard as keyb;
import time

quantity = 5
timeToPlant = quantity * 3
timeToHarvest = quantity * 8.5
waitSleepTime = 0.8

def start():
    seedAmount = int(input('How many seeds? '))
    cleanSeeds = seedAmount - seedAmount%5
    repeatAmount = cleanSeeds/5
    farmLevel = selectionCheck() #To make sure user selects a programmed craft level
    running = True
    print('press t to start, make sure craft is closed')
    while running == True:
        if keyb.is_pressed('t'):
            print('key pressed starting')
            time.sleep(5)
            running = False
            farmTime(repeatAmount, farmLevel)

def farmTime(repetitions, farmLevel):
    cropSelect(farmLevel)
    while repetitions >= 1:
        planting()
        time.sleep(timeToPlant) #to ensure time for planting
        harvestTime()
        time.sleep(timeToHarvest) #to ensure time for harvesting
        repetitions = repetitions - 1

def selectionCheck():
    levelsMade = ['appr', 'jour', 'expe', 'arti', 'mast']
    farmLevel = input('Chose farming level: appr, jour, expe, arti, mast, \n')
    if farmLevel in levelsMade:
        return farmLevel
    else:
        print('Input is not an available option, try again')
        selectionCheck()


def cropSelect(farmLevel):
    print('selecting crops')
    #All coordinates/pixel values assume crafting window is right under character plate
    pag.moveTo(42,216) #Collapse all, to ensure the right places are clicked
    pag.doubleClick()
    time.sleep(waitSleepTime)
    if farmLevel == 'appr':
        pag.moveTo(27,235) #opens apprentice
        pag.click()
        time.sleep(waitSleepTime)
        pag.moveTo(36,254) #opens grains
        pag.click()
        time.sleep(waitSleepTime)
        pag.moveTo(68,288) #selects spring barley field
        pag.click()
        time.sleep(waitSleepTime)
    if farmLevel == 'jour':
        pag.moveTo(25,255) #opens journeyman
        pag.click()
        time.sleep(waitSleepTime)
        pag.moveTo(37,289) #opens vegetables
        pag.click()
        time.sleep(waitSleepTime)
        pag.moveTo(61,323) #selects cabbage field
        pag.click()
        time.sleep(waitSleepTime)
    if farmLevel == 'expe':
        pag.moveTo(27,275) #opens expert
        pag.click()
        time.sleep(waitSleepTime)
        pag.moveTo(34,310) #opens vegetables
        pag.click()
        time.sleep(waitSleepTime)
        pag.moveTo(68,344) #selects green onion field
        pag.click()
        time.sleep(waitSleepTime)
    if farmLevel == 'arti':
        pag.moveTo(28,295) #opens artisan
        pag.click()
        time.sleep(waitSleepTime)
        pag.moveTo(36,332) #opens vegetables
        pag.click()
        time.sleep(waitSleepTime)
        pag.moveTo(100,363) #Selects Shire Apple Tree
        pag.click()
        time.sleep(waitSleepTime)
    if farmLevel == 'mast':
        pag.moveTo(28,314) #opens master
        pag.click()
        time.sleep(waitSleepTime)
        pag.moveTo(35,334) #Opens vegetables
        pag.click()
        time.sleep(waitSleepTime)
        pag.moveTo(84,385) #Selecs golden shire tater field
        pag.click()
        time.sleep(waitSleepTime)
    #else:
    #    print('something went wrong please try again')
    #    selectionCheck()


def planting():
    print('planting crops')
    pag.moveTo(605,658) #Moves to left side of quantity box
    time.sleep(waitSleepTime)
    pag.dragTo(630,658,1) #drags to right side to select everything in quantity box to delete it
    time.sleep(waitSleepTime)
    keyb.send('backspace')
    time.sleep(waitSleepTime)
    keyb.write(str(quantity)) #input for quantity
    time.sleep(waitSleepTime)
    pag.moveTo(682,661)
    pag.click()

def harvestTime():
    print('harvesting crops')
    cropsToHarvest = quantity #To ensure the correct amount of crops are harvested
    while cropsToHarvest != 0:
        keyb.send('y')
        time.sleep(waitSleepTime)
        keyb.send('g')
        cropsToHarvest = cropsToHarvest - 1



start()
