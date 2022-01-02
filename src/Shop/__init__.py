from src.Animal import Animal
from src.Animal.Animals import NoneAnimal
from src.Food import Food
from src.Food.Foods import NoneFood
from src.Animal.Animals import getRandomAnimal
from src.Food.FoodGenerator import getRandomFood


class Shop:
    """
    Shop Base Class

    round 1-2: tier 1
    round 3-4: tier 1, 2
    round 5-6: tier 1, 2, 3
    round 7-8: tier 1, 2, 3, 4
    round 9-10: tier 1, 2, 3, 4, 5
    round 11+: all tiers

    round 1-4: 3 animals
    round 5-8: 4 animals
    round 9+:  5 animals

    round 1-2: 1 food
    round 3+: 2 food
    """

    ### Init ###

    def __init__(self):

        self.round = 1
        self.animals = [NoneAnimal()] * 3
        self.items = [NoneAnimal()] * 1
        self.health_modifier = 0
        self.dmg_modifier = 0
        self.roll()

    ### Getters ###

    def getMaxTier(self):
        """
        public get max shop animal tier method

        returns highest tier
        """
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
        """
        public check animal method

        returns animal from shop position, without removing from shop
        """
        return self.animals[position]

    def checkFood(self, position: int) -> Food:
        """
        public check food method

        returns food from shop position, without removing from shop
        """
        return self.items[position]

    def getState(self):
        """
        public get shop state method

        returns shop state array
        """
        pass

    ### Setters ###

    def buyAnimal(self, position: int) -> Animal:
        """
        public buy animal method

        return Animal and remove from shop
        """
        animal = self.animals[position]
        self.animals[position] = NoneAnimal()
        return animal

    def buyFood(self, position: int) -> Food:
        """
        public buy food

        return Animal and remove from shop
        """
        food = self.items[position]
        self.items[position] = NoneFood()
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
            self.items = [NoneFood()] * 2
        if self.round == 5:
            self.animals = [NoneAnimal()] * 4
        if self.round == 9:
            self.animals = [NoneAnimal()] * 5
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
