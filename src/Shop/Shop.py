from src.Animal.Animals import *
from src.Animal.AnimalGenerator import getRandomAnimal


class Shop:
    def __init__(self):
        """
        round 1-2: teir 1
        round 3-4: teir 1, 2
        round 5-6: teir 1, 2, 3
        round 7-8: teir 1, 2, 3, 4
        round 9-10: teir 1, 2, 3, 4, 5
        round 11+: all teirs

        round 1-4: 3 animals
        round 5-8: 4 animals
        round 9+:  5 animals

        round 1-2: 1 food
        round 3+: 2 food
        """
        self.round = 1
        self.animals = [None] * 3
        self.items = [None] * 1

    def roll(self):
        for i in self.animals:
            i = getRandomAnimal(self.getMaxTeir())
        for i in self.items:
            i = self.drawItem()

    def getMaxTeir(self):
        if 1 <= self.round <= 2:
            return 1
        if 3 <= self.round <= 4:
            return 2
        if 5 <= self.round <= 6:
            return 3
        if 7 <= self.round <= 8:
            return 4
        if 9 <= self.round <= 10:
            return 5
        if 11 <= self.round:
            return 6

    def nextRound(self):
        self.round += 1
        if self.round == 3:
            self.items = [None] * 2
        if self.round == 5:
            self.animals = [None] * 4
        if self.round == 9:
            self.animals = [None] * 5
        self.roll()
