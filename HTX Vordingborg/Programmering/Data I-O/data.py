navnefil = open('lastnames.txt') #åbner filen
efternavne = navnefil.readlines() #læser og gemmer filen i efternavne
navnefil.close() #lukker filen

for navn in efternavne:
    navn = navn.strip()
    if len(navn) <= 5:
        print(navn)
