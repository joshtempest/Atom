class Fag():

    def __init__(self, navnet, niveauet=None, karakteren=None, vaegten=1):
        self.navn = navnet
        self.karakter = karakteren
        self.niveau = niveauet
        self.vaegt = vaegten

class KarakterBog():

    separator = '-'

    def __init__(self, elev='Navnløs'):
        self.elevNavn = elev
        self.data = []

    def nytFag(self, fag):
        self.data.append(fag)

    def beregnSnit(self):
        total = 0
        vaegtTotal = 0
        for fag in self.data:
            total += fag.karakter * fag.vaegt
            vaegtTotal += fag.vaegt
        return 'Karaktergennemsnit af {} fag: {}\n'.format(len(self.data), round(total/vaegtTotal, 2))

    def udskrivAlleKarakterer(self):
        output = ''
        for fag in self.data:
            output += 'Karakteren i {} ({} niveau) er: {}\n'.format(fag.navn.capitalize(), fag.niveau, fag.karakter)
        return output

martins = KarakterBog('Martin')

martins.nytFag(Fag('dansk', 'A', 4, 2))
martins.nytFag(Fag('programmering', 'B', 12, 1.5))
martins.nytFag(Fag('innovation', 'C', -3))
martins.nytFag(Fag('teknologi', 'A', -3, 2))
martins.nytFag(Fag('opvask', 'AAAA', 12))
martins.nytFag(Fag('racerbil', 'F1', 12, 4))

batmans = KarakterBog('Batman')

batmans.nytFag(Fag('sperlunking', 'Øvet', 7, 2))
batmans.nytFag(Fag('romancing', 'Rich kid', 2))
batmans.nytFag(Fag('public speaking', 'Hermit', -3))
batmans.nytFag(Fag('ninja', "League of Assassin's", 10, 2))
batmans.nytFag(Fag('crime fighting', 'Gotham', 12, 5))

KarakterBog.separator = '='

def udskrivKarakterbog(bog):
    print(bog.separator * 35 + '\n')
    print('Karakterbog for:', bog.elevNavn, '\n')
    print(bog.beregnSnit())
    print(bog.udskrivAlleKarakterer())
    print(bog.separator * 35 + '\n')

udskrivKarakterbog(batmans)
udskrivKarakterbog(martins)
