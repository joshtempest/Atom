'''
Implementer og test klassen Raflebaeger.py med følgende egenskaber:
1. Klassen skal kunne gemme referencer til et vilkårligt antal instanser af klassen Terning.
2. Klassen skal have en metode til at tilføje nye instanser af klassen Terning.
3. Klassen skal have en metode, som ruller alle de instanser af klassen Terning, som en instans af Raflebaeger har referencer til.
4. Klassen skal have en metode, som returnerer et raflebægers indhold som string, således at det er tydeligt hvilke(n) terning(er), der har slået hvilket resultat.'''

from Terning import Terning, LudoTerning

class Raflebaeger():

    def __init__(self):
        self.terninger = []

    def add(self, terningen):
        self.terninger.append(terningen)

    def remove(self, terningen):
        self.terninger.remove(terningen)

    def roll(self):
        for terning in self.terninger:
            terning.rul()

    def showResults(self):
        out = ''
        for terning in self.terninger:
            out += 'd{}:\t{}\n'.format(terning.sider, terning.slaget)
        return out

if __name__ == '__main__':
    r1 = Raflebaeger()

    minterning = LudoTerning()

    r1.add(minterning)
    r1.add(Terning(10))
    r1.add(Terning(20))


    for i in range(25):
        r1.roll()
        print(r1.showResults())
