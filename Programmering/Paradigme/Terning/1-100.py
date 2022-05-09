from Raflebaeger import Raflebaeger
from Terning import Terning

class SpillerController():

    def __init__(self):
        self.baeger = Raflebaeger()
        self.baeger.add(Terning(6))
        self.points = 0
        self.turPoints = 0

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

    def __init__(self):
        self.spiller1 = SpillerController()
        self.spiller2 = SpillerController()
        self.aktivSpiller = self.spiller1
        self.vinder = None

    def skiftSpiller(self):
        print('SKIFT')
        if self.aktivSpiller == self.spiller1:
            self.aktivSpiller = self.spiller2
        else:
            self.aktivSpiller = self.spiller1

    def checkForsejr(self):
        if self.aktivSpiller.points >= 100:
            self.vinder = self.aktivSpiller

    def spil(self, valg):
        if valg == 'rul':
            self.aktivSpiller.rul()
            if self.aktivSpiller.turPoints == 0:
                self.skiftSpiller()
        elif valg == 'stop':
            self.aktivSpiller.stop()
            self.skiftSpiller()
        self.checkForsejr()

class SpilView():

    def __init__(self):
        self.spillet = SpilController()
        while self.spillet.vinder == None:
            self.printStilling()
            if self.spillet.aktivSpiller == self.spillet.spiller1:
                print('\nSpiller 1 har turen')
            else:
                print('\nSpiller 2 har turen')
            valg = input('Rul eller Stop?')
            self.spillet.spil(valg)
            if valg == 'rul':
                print('Du slog:\t{}'.format(self.spillet.aktivSpiller.baeger.terninger[0].slaget))
            self.printTurStilling()
        print('Spillet er slut')
        print('{} er vinderen'.format(self.vinder))

    def printStilling(self):
        print('Stilling:')
        print('Spiller 1:\t{}'.format(self.spillet.spiller1.points))
        print('Spiller 2:\t{}'.format(self.spillet.spiller2.points))

    def printTurStilling(self):
        print('\nTurpoint:\t{}'.format(self.spillet.aktivSpiller.turPoints))


if __name__ == '__main__':
    SpilView()
