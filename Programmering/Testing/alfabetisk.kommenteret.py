"""
Denne funktion modtager to bogstaver og
returnerer det bogstav,
som kommer først i alfabetet.
Hvis bogstaverne er ens, returnerer
funktionen bogstav1.
Hvis parametrene er andet eller mere end et bogstav,
returnerer funktionen ingenting.
"""

def compareAlphabetically(bogstav1, bogstav2):
    # Fang ugyldige indtastninger
    if bogstav1.isalpha() and bogstav2.isalpha():
        if len(bogstav1) != 1 or len(bogstav2) != 1:
            return

        # Ensret for lettere sammenligning
        bogstav1 = str(bogstav1).lower()
        bogstav2 = str(bogstav2).lower()

        # Find det bogstav, som er først i alfabetet
        if ord(bogstav1) > ord(bogstav2):
            return bogstav2
        elif ord(bogstav1) < ord(bogstav2):
            return bogstav1
        else:
            return bogstav2

print(compareAlphabetically('', ''))
