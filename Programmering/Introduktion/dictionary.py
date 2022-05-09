MinKarakterer = {"Biologi":7,"Samfundsfag":7,"Skriftlig Fysik":10, "Skriftlig Matematik":12, "Mundtlig Matematik":10,"Mundtlig Dansk":7,"Skriftlig Dansk":7};



def udskrivEnKarakter(fag, bog):
    if fag in bog.keys():
        karakter = bog[fag]
        tilPrint = "Karakteren for {}: {}".format(fag,karakter)
        print(tilPrint)
    else:
        print('Fejl. Der findes ingen karakter for det angivne fag, i den angivne karakterbog.('+ fag + ")")


#udskrivEnKarakter("Biologi",MinKarakterer)

def udskrivAlleKarakterer(k):
    for key in k.keys():
        udskrivEnKarakter(key,k)

#udskrivAlleKarakterer(MinKarakterer)

def beregnSnit(k):
    total = 0
    for karakter in k.values():
        total = total + karakter
    snit = total/len(k)
    print('Gennemsnit af karakterer i {} fag: {}' .format(len(k),snit))

beregnSnit(MinKarakterer)
