import requests, json, random

insult = ''

def importList(file):
    #Åbner
    domeding = open(file)
    #Læser og gemmer indhold i en liste
    list = domeding.readlines()
    #lukker igen
    domeding.close()
    #Fjerner alle \n der evt. er i teksten
    for i in range(len(list)):
        list[i]=list[i].strip()
        #retunerer liste
    return list

#Vælger en random ting fra en liste der er lavet af overstående kode
def getRandom(liste):
    domething = random.choice(liste)
    return domething

#Tilføjer værdi til variable til senere brug
actsListe = importList('acts.txt')
acts=getRandom(actsListe)

#Det samme som overstående, dog fordi der skal bruges 2 ting fra jobs, har vi kodet ind at de to værdier ikke må være ens
jobList = importList('jobs.txt')
job=getRandom(jobList)
job2=getRandom(jobList)
while job==job2:
    job2=getRandom(jobList)

#Det samme som ved jobs, bare til en anden variabel
familyList = importList('family.txt')
family=getRandom(familyList)
family2=getRandom(familyList)
while family==family2:
    family2=getRandom(familyList)

thingsList=importList('things.txt')
things=getRandom(thingsList)

adjectivesList=importList('adjectives.txt')
adjectives=getRandom(adjectivesList)

#Her tilføjer vi værdi til den første variabel der blev lavet, blandt andet fra den kode lige ovenover er tilføjet.
#Dette giver den færdige insult som vi vil generere
insult += '\nI don’t want to talk to you no more you {} {}!... I {} in your general direction! Your {} was a {} and your {} smelt of {}!'.format(adjectives,job,acts,family,job2,family2,things)

#Her har vi en lille ekstra stykke kode for at spørge om man vil have en insult
answer=input('Would you like an insult? ')
#Hvis de svarer 'yes' så får de en insult
if answer == ('yes'):
    print(insult)
#Hvis de svarer 'no' giver det ingen mening, fordi folk normalt ikke vil gøres nar ad, men det bliver de alligevel.
elif answer == ('no'):
    print('Well you are going to anyway\n', insult)
#Hvis ikke der gives noget svar, ved vi ikke om der er nogen, hvis ikke der er nogen så kan vi jo ikke gøre nar ad folk
elif answer == (''):
    print('Hello?, anyone there?... No? okay bye!')
#Hvis de skrvier noget, men det ikke er 'yes' eller 'no' så er det forvirrende, et ja/nej spørgsmål skal svares med et ja eller et nej
else:
    print('Next time, please answer either yes or no')
