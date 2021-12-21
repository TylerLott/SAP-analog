from src.Animal.Animals import Animal

class Badger(Animal):
    def __init__(self, health, dmg, position):

        default_health = 4
        default_dmg = 5

        super().__init__(default_health+health, default_dmg+dmg, position)
        self.tier = 3

    def onFaint(self) -> int:
        # damage all enemies level * dmg
        return self.getLevel() * self.dmg

    