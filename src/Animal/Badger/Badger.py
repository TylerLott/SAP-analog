from src.Animal.Animal import Animal

class Badger(Animal):
    def __init__(self, health, dmg, position):

        default_health = 4
        default_dmg = 5

        super().__init__(default_health+health, default_dmg+dmg, position)
        self.tier = 3

    def onFaint(self):
        # damage all enemies level * dmg
        pass

    