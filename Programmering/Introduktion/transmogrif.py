"""
Ret i transmogrif.py, så programmet kører
I skal bruge følgende funktioner:
- int()
- str()
- float()
Find selv ud af, hvad de kan, og hvordan de fungerer.
"""

countTo = 3
theLordSpake = "First shalt thou take out the Holy Pin. Then, shalt thou count to " + str(countTo) + ". No more. No less. " + str(countTo) + " shalt be the number thou shalt count, and the number of the counting shall be " + str(countTo) + ". " + str(countTo+1) + " shalt thou not count, nor either count thou " + str(countTo-1) + ", excepting that thou then proceed to " + str(countTo) + ". " + str(countTo+2) + " is right out. Once the number " + str(countTo) + ", being the third number, be reached, then, lobbest thou thy Holy Hand Grenade of Antioch towards thy foe, who, being naughty in My sight, shall snuff it."

print(theLordSpake)

tal = int(input("Indtast et tal, som skal opløftes i anden potens: "))

print(tal ** 2)

myVar = "The meaning of life," + " the universe " + "and everything"

print(myVar)

myVar = myVar + " is: " + str((2 * 2 + 2) * (24/3 - 99 ** 0))

print(myVar)
