from src.Animal.Animal import Animal

class Ant(Animal):
    def __init__(self, health, dmg, position):
        super().__init__(health, dmg, position)
        self.tier = 1