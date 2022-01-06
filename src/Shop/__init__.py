import numpy as np

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
        self.freeze_animal = [False] * 5
        self.freeze_item = [False] * 2
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

        anim_state = [i.getState() for i in self.animals]
        anim_state = np.stack(anim_state, axis=0)
        while anim_state.shape[0] < 5:
            anim_state = np.append(anim_state, [NoneAnimal().getState()], axis=0)

        food_state = [i.getState() for i in self.items]
        food_state = np.stack(food_state, axis=0)
        while food_state.shape[0] < 2:
            food_state = np.append(food_state, [NoneFood().getState()], axis=0)

        freeze_state = np.array([int(i) for i in self.freeze_animal + self.freeze_item])

        return anim_state, food_state, freeze_state

    ### Setters ###

    def buyAnimal(self, position: int) -> Animal:
        """
        public buy animal method

        return Animal and remove from shop
        """
        animal = self.animals[position]
        self.freeze_animal[position] = False
        self.animals[position] = NoneAnimal()
        return animal

    def buyFood(self, position: int) -> Food:
        """
        public buy food

        return Animal and remove from shop
        """
        food = self.items[position]
        self.freeze_item[position] = False
        self.items[position] = NoneFood()
        return food

    def freezeAnimal(self, position: int):
        self.freeze_animal[position] = not self.freeze_animal[position]

    def freezeItem(self, position: int):
        self.freeze_item[position] = not self.freeze_item[position]

    ### Actions ###

    def roll(self):
        for i in range(len(self.animals)):
            self.animals[i] = getRandomAnimal(
                self.getMaxTier(),
                health_mod=self.health_modifier,
                dmg_mod=self.dmg_modifier,
            )
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
