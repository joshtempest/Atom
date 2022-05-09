import random, copy





"""
def selectionSort():
    items = items.copy()
    for n in range(len(items)):
        key = n
        while key > 0:
            if
"""

def insertionSort(items):
    # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale
    items = items.copy()
    for n in range(len(items)): #Gentager det hele indtil listen er sorteret
        key = n #Sætter key til at være det nummer vi er ved i listen
        while key > 0:
            if items[key-1]>items[key]: #Sammenligner om elementet til venstre fra vores position i listen er større...
                items[key-1],items[key]=items[key],items[key-1]
            key = key-1 #... og bytter om på dem

    return items


if __name__ == '__main__':
    l = list(range(0, 5))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)
        ## Kald den funktion, du vil teste
        ls = insertionSort(l)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('Succes! Algoritmen sorterer korrekt.')
    print('blandet: ', lb)
    print('sorteret:', ls)
