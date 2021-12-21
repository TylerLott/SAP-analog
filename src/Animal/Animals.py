from abc import ABC, abstractmethod
from random import randrange

from src.Animal.Actions.Actions import Action


class Animal(ABC):
    def __init__(self, health: int, dmg: int, position):
        self.health = health
        self.dmg = dmg
        self.position = position
        self.alive = True
        self.level = 1  # above 5: level 3, above 3: level 2, less: level 1
        self.effect = None
        self.dmgModifier = 1

    def getLevel(self) -> int:
        if self.level > 5:
            return 3
        if self.level > 2:
            return 2
        return 1

    def onHit(self, dmgAmt):
        self.dmg -= round(dmgAmt * self.dmgModifier)
        if self.dmg <= 0:
            self.alive = False

    def onCombine(self):
        self.level += 1

    def updatePosition(self, pos):
        self.position = pos

    def getEffect(self, effect):
        pass

    def getFood(self, food):
        pass

    def onFaint(self):
        pass

    def onSell(self):
        pass

    def onEat(self):
        pass

    def onEndOfTurn(self):
        pass

    def onLevelUp(self):
        pass

    def onFoodBought(self):
        pass

    def onStartOfBattle(self):
        pass

    def onBuy(self):
        pass

    def onStartOfTurn(self):
        pass

    def onBeforeAttack(self):
        pass

    def onHurt(self):
        pass

    def onFriendSold(self):
        pass

    def onFriendSummoned(self):
        pass

    def onFriendAheadAttack(self):
        pass

    def onFriendAheadFaint(self):
        pass


class Ant(Animal):
    def __init__(self, health: int, dmg: int, position: int):

        default_health = 1
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 1

    def onFaint(self, friends: list) -> Action:
        # give random friend +2/1
        # return index of friend from friend list
        # TODO: figure out how to randomly assign
        act = Action("heal", 2, 1, "random", -2)
        return act


class Badger(Animal):
    def __init__(self, health, dmg, position):

        default_health = 4
        default_dmg = 5

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 3

    def onFaint(self) -> int:
        # damage adjacent enemies level * dmg
        # TODO: figure out how to represent the teams in a way that works
        # act = Action("attack", -(self.getLevel() * self.dmg), 0, self.position-1, )
        # return act
        pass


class Bat(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 2


class Beaver(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 1


class Bison(Animal):
    def __init__(self, health, dmg, position):

        default_health = 6
        default_dmg = 6

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 4


class Blowfish(Animal):
    def __init__(self, health, dmg, position):

        default_health = 5
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 3


class Boar(Animal):
    def __init__(self, health, dmg, position):

        default_health = 6
        default_dmg = 8

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 6


class Camel(Animal):
    def __init__(self, health, dmg, position):

        default_health = 5
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 3


class Cat(Animal):
    def __init__(self, health, dmg, position):

        default_health = 5
        default_dmg = 4

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 6


class Cow(Animal):
    def __init__(self, health, dmg, position):

        default_health = 6
        default_dmg = 4

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 5


class Crab(Animal):
    def __init__(self, health, dmg, position):

        default_health = 3
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 2


class Cricket(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 1


class Crocodile(Animal):
    def __init__(self, health, dmg, position):

        default_health = 4
        default_dmg = 8

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 5


class Deer(Animal):
    def __init__(self, health, dmg, position):

        default_health = 1
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 4


class Dodo(Animal):
    def __init__(self, health, dmg, position):

        default_health = 3
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 2


class Dog(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 3


class Dolphin(Animal):
    def __init__(self, health, dmg, position):

        default_health = 6
        default_dmg = 4

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 4


class Dragon(Animal):
    def __init__(self, health, dmg, position):

        default_health = 8
        default_dmg = 6

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 6


class Duck(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 1


class Elephant(Animal):
    def __init__(self, health, dmg, position):

        default_health = 5
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 2


class Fish(Animal):
    def __init__(self, health, dmg, position):

        default_health = 3
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 1


class Flamingo(Animal):
    def __init__(self, health, dmg, position):

        default_health = 1
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 2


class Fly(Animal):
    def __init__(self, health, dmg, position):

        default_health = 5
        default_dmg = 5

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 6


class Giraffe(Animal):
    def __init__(self, health, dmg, position):

        default_health = 5
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 3


class Gorilla(Animal):
    def __init__(self, health, dmg, position):

        default_health = 9
        default_dmg = 6

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 6


class Hedgehog(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 2


class Hippo(Animal):
    def __init__(self, health, dmg, position):

        default_health = 7
        default_dmg = 4

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 4


class Horse(Animal):
    def __init__(self, health, dmg, position):

        default_health = 1
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 1


class Kangaroo(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 3


class Leopard(Animal):
    def __init__(self, health, dmg, position):

        default_health = 4
        default_dmg = 10

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 6


class Mammoth(Animal):
    def __init__(self, health, dmg, position):

        default_health = 10
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 6


class Mosquito(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 1


class Monkey(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 5


class Otter(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 1


class Ox(Animal):
    def __init__(self, health, dmg, position):

        default_health = 4
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 3


class Parrot(Animal):
    def __init__(self, health, dmg, position):

        default_health = 3
        default_dmg = 5

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 4


class Peacock(Animal):
    def __init__(self, health, dmg, position):

        default_health = 5
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 2


class Penguin(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 4


class Pig(Animal):
    def __init__(self, health, dmg, position):

        default_health = 1
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 1


class Rabbit(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 3


class Rat(Animal):
    def __init__(self, health, dmg, position):

        default_health = 5
        default_dmg = 4

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 2


class Rhino(Animal):
    def __init__(self, health, dmg, position):

        default_health = 8
        default_dmg = 5

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 5


class Rooster(Animal):
    def __init__(self, health, dmg, position):

        default_health = 3
        default_dmg = 5

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 4


class Scorpion(Animal):
    def __init__(self, health, dmg, position):

        default_health = 1
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 5


class Seal(Animal):
    def __init__(self, health, dmg, position):

        default_health = 8
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 5


class Shark(Animal):
    def __init__(self, health, dmg, position):

        default_health = 4
        default_dmg = 4

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 5


class Sheep(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 3


class Shrimp(Animal):
    def __init__(self, health, dmg, position):

        default_health = 3
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 2


class Skunk(Animal):
    def __init__(self, health, dmg, position):

        default_health = 6
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 4


class Sloth(Animal):
    def __init__(self, health, dmg, position):

        default_health = 1
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 1


class Snail(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 3


class Snake(Animal):
    def __init__(self, health, dmg, position):

        default_health = 6
        default_dmg = 6

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 6


class Spider(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 2


class Squirrel(Animal):
    def __init__(self, health, dmg, position):

        default_health = 5
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 4


class Swan(Animal):
    def __init__(self, health, dmg, position):

        default_health = 3
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 2


class Tiger(Animal):
    def __init__(self, health, dmg, position):

        default_health = 3
        default_dmg = 4

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 6


class Turkey(Animal):
    def __init__(self, health, dmg, position):

        default_health = 4
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 5


class Turtle(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 3


class Whale(Animal):
    def __init__(self, health, dmg, position):

        default_health = 6
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 4


class Worm(Animal):
    def __init__(self, health, dmg, position):

        default_health = 2
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg, position)
        self.tier = 4
