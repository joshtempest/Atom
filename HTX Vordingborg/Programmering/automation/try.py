import pyautogui as pag

txtfile = open ('txtfile.txt','w')
pag.typewrite("hello",0.25)
txtfile.close()
