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
    """
    Denne klasse kontrollerer data og handlinger for spillerne i spillet 1-100.
    """
    def __init__(self, navn='Rudolf'):
        """
        Initialiserer instansvariable, herunder spillerens navn til 'Rudolf',
        hvis andet ikke er angivet som parameter.
        """
        self.baeger = Raflebaeger()
        self.baeger.add(Terning(6))
        self.points = 0
        self.turPoints = 0
        self.navn = navn

    def rul(self):
        """
        Metoden ruller raflebægeret og opdaterer spillerens points for denne tur
        med resultatet. Slår spilleren 1 med en terning, bliver turens points nulstillet.
        """
        self.baeger.roll()
        for terning in self.baeger.terninger:
            if terning.slaget == 1:
                self.turPoints = 0
            else:
                self.turPoints += terning.slaget

    def stop(self):
        """
        Metoder lægger points optjent i den aktive tur til det totale pointtal
        og nulstiller tælleren for points i den aktive tur.
        """
        self.points += self.turPoints
        self.turPoints = 0

class SpilController():
    """
    Denne klasse kontrollerer data og forløb for et spil 1-100.
    Parametren 'spillere' er en liste af strings, som repræsenterer spillernes navne.
    Hvis andet ikke er angivet bliver spillet oprettet med spillerne 'Spiller 1'
    og 'Spiller 2'.
    Parametren 'target' er pointmålet for spillerne. Hvis andet ikke er angivet,
    er dette 100.
    """

    def __init__(self, spillere=['Spiller 1', 'Spiller 2'], target=100):
        """
        Initialiserer instansvariable. Metoden sikrer, at der er mindst en spiller
        og sætter den aktive spiller til den første i listen.
        """
        self.spillere = []
        if len(spillere) < 1:
            self.spillere.append(SpillerController('Solospiller'))
        else:
            for navn in spillere:
                self.spillere.append(SpillerController(navn))
        self.aktivSpiller = self.spillere[0]
        self.vinder = None
        self.ture = 1
        self.target = target

    def skiftSpiller(self):
        """
        Skifter den aktive spiller til den næste i rækken eller til den første,
        hvis enden af rækken er nået.
        """
        self.ture += 1
        aktivIndex = self.spillere.index(self.aktivSpiller)
        if aktivIndex == len(self.spillere)-1:
            self.aktivSpiller = self.spillere[0]
        else:
            self.aktivSpiller = self.spillere[aktivIndex+1]

    def checkForSejr(self):
        """
        Kontrollerer om der kan kåres en vinder af spillet. Følgende betingelser
        skal være opfyldt:
        - Mindst en spiller skal have nået pointmålet
        - Alle spillere skal have haft lige mange ture
        - Maksimalt en spiller har det højeste antal points
        """
        maxPoints = 0
        uafgjort = False
        potentielVinder = None
        for spiller in self.spillere:
            if spiller.points > maxPoints:
                potentielVinder = spiller
                maxPoints = spiller.points
                uafgjort = False
            elif spiller.points == maxPoints:
                uafgjort = True
        if not uafgjort and potentielVinder.points >= self.target and self.ture % len(self.spillere) == 0 and self.ture > 0:
            self.vinder = potentielVinder


    def spil(self, valg):
        """
        Modtager spillerens handling ('rul' eller 'stop') og afvikler spillerens
        tur jævnfør spillets regler.
        Metoden har forskellige returværdier afhængig af resultatet af spillerens
        handling og terningernes udfald:
        - 'død':     Spilleren har slået 1, og turen skifter til næste spiller
        - 'fortsæt': Spilleren kan fortsætte
        - 'stop':    Spilleren stopper sin tur, lægger de optjente points til
                     totalen og turen skifter til næste spiller
        """
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
    """
    Denne klasse udstiller et tekstbaseret brugerinterface til spillet 1-100.
    """
    def __init__(self):
        """
        Indhenter navne på de deltagende spillere, opretter en instans af
        spillet ud fra listen og viser en tekstmenu baseret på spillets tilstand.
        Når en vinder er fundet bliver stillingen samt vinderens navn udskrevet,
        og programmet slutter.
        """
        spillernavne = self.genererSpillerListe()
        self.spillet = SpilController(spillernavne, 10)
        while self.spillet.vinder == None:
            self.printStilling()
            print('{} har turen'.format(self.spillet.aktivSpiller.navn))
            valg = input('Rul eller Stop? ')
            resultat = self.spillet.spil(valg)
            if valg == 'rul':
                if resultat == 'død':
                    print('Du slog 1. Turen skifter.')
                elif resultat == 'fortsæt':
                    print(self.spillet.aktivSpiller.baeger.showResults())
                    self.printTurStilling()

        print('\nSpillet er slut')
        self.printStilling()
        print('{} er vinderen!'.format(self.spillet.vinder.navn))

    def genererSpillerListe(self):
        """
        Genererer en liste af stings med spilleres navne (med stort forbogstav)
        ud fra spillerens indtastninger og returnerer den.
        """
        spillerliste = []
        nyspiller = None
        while nyspiller != '':
            nyspiller = input('Indtast navn på spiller eller ENTER for at færdiggøre\n')
            spillerliste.append(nyspiller.title())
        return spillerliste[:len(spillerliste)-1]

    def printStilling(self):
        """
        Udskriver spillets øjeblikkelige stilling.
        """
        print('Stilling:')
        for spiller in self.spillet.spillere:
            print('{}: {}'.format(spiller.navn, spiller.points))

    def printTurStilling(self):
        """
        Udskriver det optjente pointtal for den aktive spiller.
        """
        print('Tur: {}\n'.format(self.spillet.aktivSpiller.turPoints))

if __name__ == '__main__':
    SpilView()
