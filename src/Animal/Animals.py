from src.Animal import Animal


class NoneAnimal(Animal):
    """None class for animals"""

    def __init__(self):
        super().__init__(0, 0)

    def __bool__(self):
        return False


class Ant(Animal):
    """Ant Class"""

    def __init__(self, health: int, dmg: int):

        default_health = 1
        default_dmg = 2
        ability = "Faint: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 1

    def onFaint(self):
        pass


class Badger(Animal):
    def __init__(self, health, dmg):

        default_health = 4
        default_dmg = 5

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 3

    def onFaint(self):
        pass


class Bat(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2


class Beaver(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 1


class Bison(Animal):
    def __init__(self, health, dmg):

        default_health = 6
        default_dmg = 6

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 4


class Blowfish(Animal):
    def __init__(self, health, dmg):

        default_health = 5
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 3


class Boar(Animal):
    def __init__(self, health, dmg):

        default_health = 6
        default_dmg = 8

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 6


class Camel(Animal):
    def __init__(self, health, dmg):

        default_health = 5
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 3


class Cat(Animal):
    def __init__(self, health, dmg):

        default_health = 5
        default_dmg = 4

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 6


class Cow(Animal):
    def __init__(self, health, dmg):

        default_health = 6
        default_dmg = 4

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 5


class Crab(Animal):
    def __init__(self, health, dmg):

        default_health = 3
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2


class Cricket(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 1


class Crocodile(Animal):
    def __init__(self, health, dmg):

        default_health = 4
        default_dmg = 8

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 5


class Deer(Animal):
    def __init__(self, health, dmg):

        default_health = 1
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 4


class Dodo(Animal):
    def __init__(self, health, dmg):

        default_health = 3
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2


class Dog(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 3


class Dolphin(Animal):
    def __init__(self, health, dmg):

        default_health = 6
        default_dmg = 4

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 4


class Dragon(Animal):
    def __init__(self, health, dmg):

        default_health = 8
        default_dmg = 6

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 6


class Duck(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 1


class Elephant(Animal):
    def __init__(self, health, dmg):

        default_health = 5
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2


class Fish(Animal):
    def __init__(self, health, dmg):

        default_health = 3
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 1


class Flamingo(Animal):
    def __init__(self, health, dmg):

        default_health = 1
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2


class Fly(Animal):
    def __init__(self, health, dmg):

        default_health = 5
        default_dmg = 5

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 6


class Giraffe(Animal):
    def __init__(self, health, dmg):

        default_health = 5
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 3


class Gorilla(Animal):
    def __init__(self, health, dmg):

        default_health = 9
        default_dmg = 6

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 6


class Hedgehog(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2


class Hippo(Animal):
    def __init__(self, health, dmg):

        default_health = 7
        default_dmg = 4

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 4


class Horse(Animal):
    def __init__(self, health, dmg):

        default_health = 1
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 1


class Kangaroo(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 3


class Leopard(Animal):
    def __init__(self, health, dmg):

        default_health = 4
        default_dmg = 10

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 6


class Mammoth(Animal):
    def __init__(self, health, dmg):

        default_health = 10
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 6


class Mosquito(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 1


class Monkey(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 5


class Otter(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 1


class Ox(Animal):
    def __init__(self, health, dmg):

        default_health = 4
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 3


class Parrot(Animal):
    def __init__(self, health, dmg):

        default_health = 3
        default_dmg = 5

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 4


class Peacock(Animal):
    def __init__(self, health, dmg):

        default_health = 5
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2


class Penguin(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 4


class Pig(Animal):
    def __init__(self, health, dmg):

        default_health = 1
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 1


class Rabbit(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 3


class Rat(Animal):
    def __init__(self, health, dmg):

        default_health = 5
        default_dmg = 4

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2


class Rhino(Animal):
    def __init__(self, health, dmg):

        default_health = 8
        default_dmg = 5

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 5


class Rooster(Animal):
    def __init__(self, health, dmg):

        default_health = 3
        default_dmg = 5

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 4


class Scorpion(Animal):
    def __init__(self, health, dmg):

        default_health = 1
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 5


class Seal(Animal):
    def __init__(self, health, dmg):

        default_health = 8
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 5


class Shark(Animal):
    def __init__(self, health, dmg):

        default_health = 4
        default_dmg = 4

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 5


class Sheep(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 3


class Shrimp(Animal):
    def __init__(self, health, dmg):

        default_health = 3
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2


class Skunk(Animal):
    def __init__(self, health, dmg):

        default_health = 6
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 4


class Sloth(Animal):
    def __init__(self, health, dmg):

        default_health = 1
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 1


class Snail(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 3


class Snake(Animal):
    def __init__(self, health, dmg):

        default_health = 6
        default_dmg = 6

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 6


class Spider(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2


class Squirrel(Animal):
    def __init__(self, health, dmg):

        default_health = 5
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 4


class Swan(Animal):
    def __init__(self, health, dmg):

        default_health = 3
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2


class Tiger(Animal):
    def __init__(self, health, dmg):

        default_health = 3
        default_dmg = 4

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 6


class Turkey(Animal):
    def __init__(self, health, dmg):

        default_health = 4
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 5


class Turtle(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 3


class Whale(Animal):
    def __init__(self, health, dmg):

        default_health = 6
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 4


class Worm(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 4
