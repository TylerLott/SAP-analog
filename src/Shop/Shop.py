from src.Animal.Animals import *
from src.Food.Food import *
from src.Animal.AnimalGenerator import getRandomAnimal
from src.Food.FoodGenerator import getRandomFood


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
        self.health_modifier = 0
        self.dmg_modifier = 0
        self.money = 10
        self.roll()

    def payRoll(self):
        if self.money > 0:
            self.roll()
            self.money -= 1

    def roll(self):
        self.money -= 1
        for i in range(len(self.animals)):
            self.animals[i] = getRandomAnimal(self.getMaxTier())
        for i in range(len(self.items)):
            self.items[i] = getRandomFood(self.getMaxTier())

    def buyAnimal(self, position: int) -> Animal:
        animal = self.animals[position]
        self.animals[position] = None
        return animal

    def buyFood(self, position: int) -> Food:
        food = self.items[position]
        self.items[position] = None
        return food

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

    def nextRound(self):
        self.round += 1
        if self.round == 3:
            self.items = [None] * 2
        if self.round == 5:
            self.animals = [None] * 4
        if self.round == 9:
            self.animals = [None] * 5
        self.roll()

    def __str__(self):

        animal_string = "|"
        stat_string = "|"
        for i in self.animals:
            if not i:
                space = " "
                animal_string += f"{space:^10}|"
                continue
            an = f"{i.__class__.__name__:^10}|"
            animal_string += an
            stat = f"{i.health:^5}{i.dmg:^5}|"
            stat_string += stat

        item_string = "|"
        for i in self.items:
            if not i:
                space = " "
                animal_string += f"{space:^10}|"
                continue
            it = f"{i.__class__.__name__:^10}|"
            item_string += it

        str_length = (len(animal_string) + len(item_string) - 6) // 2
        shop_text = ("#" * str_length) + " SHOP " + ("#" * str_length)

        anim_len = (len(animal_string) - 9) // 2
        animal_title = ("-" * anim_len) + " ANIMALS " + ("-" * anim_len) + "|"

        item_len = (len(item_string) - 7) // 2
        item_title = ("-" * item_len) + " ITEMS " + ("-" * item_len)

        return (
            shop_text
            + "\n"
            + animal_title
            + item_title
            + "\n"
            + animal_string
            + item_string
            + "\n"
            + stat_string
        )
