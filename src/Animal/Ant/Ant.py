from src.Animal.Animal import Animal

class Ant(Animal):
    def __init__(self, health, dmg, position):

        default_health = 1
        default_dmg = 2

        super().__init__(default_health+health, default_dmg+dmg, position)
        self.tier = 1

    def onFaint(self):
        # give random friend +2/1
        pass