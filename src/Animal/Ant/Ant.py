import Animal

class Ant(Animal):
    def __init__(self, health, dmg):
        super.__init__(health, dmg)
        self.tier = 1