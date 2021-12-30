from src.Animal.Animals import Animal
from src.Food.Foods import Food
from src.Animal.AnimalGenerator import getRandomAnimal
from src.Food.FoodGenerator import getRandomFood


class Shop:
    """
    Shop class

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

    ### Init ###

    def __init__(self):

        self.round = 1
        self.animals = [None] * 3
        self.items = [None] * 1
        self.health_modifier = 0
        self.dmg_modifier = 0
        self.roll()

    ### Getters ###

    def getShop(self):
        return self.animals + self.items

    def getMoney(self):
        return self.money

    def getMaxTier(self):
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

    def checkAnimal(self, position: int) -> Animal:
        return self.animals[position]

    ### Setters ###

    def buyAnimal(self, position: int) -> Animal:
        animal = self.animals[position]
        self.animals[position] = None
        return animal

    def buyFood(self, position: int) -> Food:
        food = self.items[position]
        self.items[position] = None
        return food

    ### Actions ###

    def roll(self):
        for i in range(len(self.animals)):
            self.animals[i] = getRandomAnimal(self.getMaxTier())
        for i in range(len(self.items)):
            self.items[i] = getRandomFood(self.getMaxTier())

    def setRound(self, round: int):
        self.round = round
        if self.round == 3:
            self.items = [None] * 2
        if self.round == 5:
            self.animals = [None] * 4
        if self.round == 9:
            self.animals = [None] * 5
        self.roll()

    ### Private ###

    ### Overrides ###

    def __str__(self):
        """
        For printing cleanly to console
        """
        out_str = "|##############################|\n"
        out_str += "|############ SHOP ############|\n"
        out_str += "|##############################|\n"
        for i in self.animals:
            out_str += i.__str__()

        out_str += "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n"

        for i in self.items:
            out_str += i.__str__()

        out_str += "|##############################|\n"

        return out_str
