from Terning import Terning

class Raflebaeger():
    def __init__(self):
        self.terninger = []

    def add(self, terning):
        self.terninger.append(terning)

    def remove(self, terning):
        self.terninger.remove(terning)

    def roll(self):
        resultater = []
        for terning in self.terninger:
            resultater.append(terning.rul())
        return resultater

if __name__ == '__main__':
    koppen = Raflebaeger()
    koppen.add(Terning())
    koppen.add(Terning())
    koppen.add(Terning())
    koppen.add(Terning())
    koppen.add(Terning())

    print(koppen.rul())
