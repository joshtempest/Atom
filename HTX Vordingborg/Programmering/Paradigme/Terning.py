import random

class Terning():
    def __init__(self, antalSider=6):
        self.sider = antalSider
        self.rul()

    def rul(self):
        self.slaget = random.randint(1, self.sider)
        return self.slaget

if __name == '__main__'
    minTerning = Terning()
    minAndenTerning = Terning(20)
    for i in range(20):
        print(minTerning.rul(), minAndenTerning.rul())
        print(minTerning.slaget)
