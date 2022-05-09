import random

class Terning():

    def __init__(self, antalSider=6):
        self.sider = antalSider
        self.rul()

    def rul(self):
        self.slaget = random.randint(1, self.sider)
        return self.slaget

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
            out += 'd{}: {}\n'.format(terning.sider, terning.slaget)
        return out

class SpillerController():

    def __init__(self, navn='Rudolf'):
        self.baeger = Raflebaeger()
        self.baeger.add(Terning(6))
        self.points = 0
        self.turPoints = 0
        self.navn = navn

    def rul(self):
        self.baeger.roll()
        for terning in self.baeger.terninger:
            if terning.slaget == 1:
                self.turPoints = 0
            else:
                self.turPoints += terning.slaget

    def stop(self):
        self.points += self.turPoints
        self.turPoints = 0

class SpilController():

    def __init__(self, target=100):
        self.spillere = [SpillerController('Terkel'), SpillerController()]
        self.aktivSpiller = self.spillere[0]
        self.vinder = None
        self.ture = 0
        self.target = target

    def skiftSpiller(self):
        print('SKIFT')
        self.ture += 1
        aktivIndex = self.spillere.index(self.aktivSpiller)
        if aktivIndex == len(self.spillere)-1:
            self.aktivSpiller = self.spillere[0]
        else:
            self.aktivSpiller = self.spillere[aktivIndex+1]

    def checkForSejr(self):
        maxPoints = 0
        potentielVinder = None
        for spiller in self.spillere:
            if spiller.points > maxPoints:
                potentielVinder = spiller
                maxPoints = spiller.points
        if potentielVinder.points >= self.target and self.ture % 2 == 0:
            self.vinder = potentielVinder


    def spil(self, valg):
        if valg == 'rul':
            self.aktivSpiller.rul()
            if self.aktivSpiller.turPoints == 0:
                self.skiftSpiller()
                return 'død'
            return 'fortsæt'
        elif valg == 'stop':
            self.aktivSpiller.stop()
            self.checkForSejr()
            self.skiftSpiller()
            return 'stop'

class SpilView():

    def __init__(self):
        self.spillet = SpilController(10)
        while self.spillet.vinder == None:
            self.printStilling()
            print('Tur nr.: {}'.format(self.spillet.ture))
            print('{} har turen'.format(self.spillet.aktivSpiller.navn))
            valg = input('Rul eller Stop? ')
            resultat = self.spillet.spil(valg)
            if valg == 'rul' and resultat == 'stop':
                print(self.spillet.aktivSpiller.baeger.showResults())
            self.printTurStilling()

        print('\nSpillet er slut')
        print('{} er vinderen'.format(self.spillet.vinder.navn))

    def printStilling(self):
        print('Stilling:')
        for spiller in self.spillet.spillere:
            print('{}: {}'.format(spiller.navn, spiller.points))

    def printTurStilling(self):
        print('Tur: {}'.format(self.spillet.aktivSpiller.turPoints))

if __name__ == '__main__':
    SpilView()
