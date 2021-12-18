from random import randrange
from src.Animal.Animal import Animal

class Ant(Animal):
    def __init__(self, health:int, dmg:int, position:int):

        default_health = 1
        default_dmg = 2

        super().__init__(default_health+health, default_dmg+dmg, position)
        self.tier = 1

    def onFaint(self, friends: list) -> int:
        # give random friend +2/1
        # return index of friend from friend list
        if len(friends) == 0:
            return -1
        return randrange(len(friends))