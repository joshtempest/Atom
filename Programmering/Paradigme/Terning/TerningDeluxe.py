# Copyright 2018 Rotten Banana Interactive

import random

class Terning():

    def __init__(self, sider):
        self.holdt = False
        self.sider = sider
        self.historik = []
        self.rul()

    # Returnerer  det seneste slag
    def senesteSlag(self):
        return self.historik[len(self.historik)-1]

    # Slaar med terningen og tilfoejer til terningens historik.
    # Returnerer det nye slag
    def rul(self):
        if not self.holdt:
            self.historik.append(random.randint(1, self.sider))
        return self.senesteSlag()

    def hold(self):
        self.holdt = True

    def frigiv(self):
        self.holdt = False

    # Custom implementation af '=='
    def __eq__(self, other):
        return self.senesteSlag() == other.senesteSlag()

    # Custom implementation af '<'
    def __lt__(self, other):
        return self.senesteSlag() < other.senesteSlag()

    def __str__(self):
        return str(self.senesteSlag())

    def __repr__(self):
        return self.senesteSlag()
