import random

class Terning():
    def __init__(self, antalSider=6):
        self.sider = antalSider
        self.rul()

    def rul(self):
        self.slaget = random.randint(1, self.sider)
        return self.slaget


class LudoTerning(Terning):
    def __init__(self):
        super(LudoTerning, self).__init__()

    def roll(self):
        super(LudoTerning, self).rul()
        if self.slaget == 3:
            self.slaget = 'Stjerne'
        elif self.slaget == 5:
            self.slaget = 'Globus'
        return self.slaget


if __name__ == '__main__':
    minTerning = LudoTerning()
    for i in range(20):
        print(minTerning.rul(), minTerning.slaget)







"""if __name__ == '__main__':
    minTerning = Terning()
    minAndenTerning = Terning(20)
    for i in range(20):
        print(minTerning.rul(), minAndenTerning.rul())
        print(minTerning.slaget)

if __name__ == '__main__':
    minTerning = LudoTerning()
    for i in range(10):
        minTerning.rul()
        if minTerning.rul() == 3:
            print('Stjerne')
        elif minTerning.rul() == 5:
            print('Globus')
        else:
            print(minTerning.slaget)"""
