import requests, json
#http://loripsum.net/api/medium
lixget=requests.get('http://loripsum.net/api/medium')

#if checker her om vi faktisk har fået noget data
if lixget.status_code==200:
    print(lixget.text)
    #Finder O, som er antal ord i teksten
    findO=len(lixget.text.split(' '))
    print('antal ord: ',findO)

    #Finder P, som er antal punktummer i teksten
    findP=lixget.text.count('.')
    print('antal punktummer: ', findP)

    #Finder L, som er antal ord med over 6 bogstaver
    findL=0
    for ord in lixget.text.split(' '):
        for tegn in '.,!;:?<>()/':
            ord=ord.replace(tegn,'')
        if len(ord)>6:
            findL=findL+1
    print('Antal lange ord: ', findL)

    #Beregner lixtallet for teksten ud fra de overstående data indsamlinger
    lixtal=(findO/findP)+((findL*100)/findO)
    #Printer lixtallet
    print('Lix = ', round(lixtal))
    if lixtal >= 55:
        print('Teksten er meget svær')
    elif lixtal <55 and lixtal >44:
        print("Teksten er svær")
    elif lixtal <45 and lixtal > 34:
        print('teksten er middel')
    elif lixtal <35 and lixtal > 24:
        print('teksten er let for øvede læsere')
    else:
        print("teksten er let for alle læsere")

else:
    #Hvis vi ikke får data der virker, printer den det
    print('fejl 400')
