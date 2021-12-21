
from abc import ABC, abstractmethod
from random import randrange

class Animal(ABC):

    def __init__(self, health: int, dmg: int, position):
        self.health = health
        self.dmg = dmg
        self.position = position
        self.alive = True
        self.level = 1 # above 5: level 3, above 3: level 2, less: level 1
        self.effect = None
        self.dmgModifier = 1

    def getLevel(self) -> int:
        if self.level > 5: return 3
        if self.level > 2: return 2
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

    @abstractmethod
    def onFaint(self):
        pass

    @abstractmethod
    def onSell(self):
        pass

    @abstractmethod
    def onEat(self):
        pass

    @abstractmethod
    def onEndOfTurn(self):
        pass

    @abstractmethod
    def onLevelUp(self):
        pass

    @abstractmethod
    def onFoodBought(self):
        pass

    @abstractmethod
    def onStartOfBattle(self):
        pass

    @abstractmethod
    def onBuy(self):
        pass

    @abstractmethod
    def onStartOfTurn(self):
        pass

    @abstractmethod
    def onBeforeAttack(self):
        pass

    @abstractmethod
    def onHurt(self):
        pass

    @abstractmethod
    def onFriendSold(self):
        pass

    @abstractmethod
    def onFriendSummoned(self):
        pass

    @abstractmethod
    def onFriendAheadAttack(self):
        pass

    @abstractmethod
    def onFriendAheadFaint(self):
        pass


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


class Badger(Animal):
    def __init__(self, health, dmg, position):

        default_health = 4
        default_dmg = 5

        super().__init__(default_health+health, default_dmg+dmg, position)
        self.tier = 3

    def onFaint(self) -> int:
        # damage all enemies level * dmg
        return self.getLevel() * self.dmg

class Bat(Animal):
    def __init__(self, health, dmg, position):
        pass

class Beaver(Animal):
    def __init__(self, health, dmg, position):
        pass

class Beetle(Animal):
    def __init__(self, health, dmg, position):
        pass

class Bison(Animal):
    def __init__(self, health, dmg, position):
        pass

class Blowfish(Animal):
    def __init__(self, health, dmg, position):
        pass

class Bluebird(Animal):
    def __init__(self, health, dmg, position):
        pass

class Boar(Animal):
    def __init__(self, health, dmg, position):
        pass

class Camel(Animal):
    def __init__(self, health, dmg, position):
        pass

class Cat(Animal):
    def __init__(self, health, dmg, position):
        pass

class Cow(Animal):
    def __init__(self, health, dmg, position):
        pass

class Crab(Animal):
    def __init__(self, health, dmg, position):
        pass

class Cricket(Animal):
    def __init__(self, health, dmg, position):
        pass

class Crocodile(Animal):
    def __init__(self, health, dmg, position):
        pass

class Deer(Animal):
    def __init__(self, health, dmg, position):
        pass

class Dodo(Animal):
    def __init__(self, health, dmg, position):
        pass

class Dog(Animal):
    def __init__(self, health, dmg, position):
        pass

class Dolphin(Animal):
    def __init__(self, health, dmg, position):
        pass

class Dragon(Animal):
    def __init__(self, health, dmg, position):
        pass

class Duck(Animal):
    def __init__(self, health, dmg, position):
        pass

class Elephant(Animal):
    def __init__(self, health, dmg, position):
        pass

class Fish(Animal):
    def __init__(self, health, dmg, position):
        pass

class Flamingo(Animal):
    def __init__(self, health, dmg, position):
        pass

class Fly(Animal):
    def __init__(self, health, dmg, position):
        pass

class Giraffe(Animal):
    def __init__(self, health, dmg, position):
        pass

class Gorilla(Animal):
    def __init__(self, health, dmg, position):
        pass

class Hedgehog(Animal):
    def __init__(self, health, dmg, position):
        pass

class Hippo(Animal):
    def __init__(self, health, dmg, position):
        pass

class Horse(Animal):
    def __init__(self, health, dmg, position):
        pass

class Kangaroo(Animal):
    def __init__(self, health, dmg, position):
        pass

class Ladybug(Animal):
    def __init__(self, health, dmg, position):
        pass

class Leopard(Animal):
    def __init__(self, health, dmg, position):
        pass

class Mammoth(Animal):
    def __init__(self, health, dmg, position):
        pass

class Mosquito(Animal):
    def __init__(self, health, dmg, position):
        pass

class Monkey(Animal):
    def __init__(self, health, dmg, position):
        pass

class Otter(Animal):
    def __init__(self, health, dmg, position):
        pass

class Ox(Animal):
    def __init__(self, health, dmg, position):
        pass

class Parrot(Animal):
    def __init__(self, health, dmg, position):
        pass

class Peacock(Animal):
    def __init__(self, health, dmg, position):
        pass

class Penguin(Animal):
    def __init__(self, health, dmg, position):
        pass

class Pig(Animal):
    def __init__(self, health, dmg, position):
        pass

class Rabbit(Animal):
    def __init__(self, health, dmg, position):
        pass

class Rat(Animal):
    def __init__(self, health, dmg, position):
        pass

class Rhino(Animal):
    def __init__(self, health, dmg, position):
        pass

class Rooster(Animal):
    def __init__(self, health, dmg, position):
        pass

class Scorpion(Animal):
    def __init__(self, health, dmg, position):
        pass

class Seal(Animal):
    def __init__(self, health, dmg, position):
        pass

class Shark(Animal):
    def __init__(self, health, dmg, position):
        pass

class Sheep(Animal):
    def __init__(self, health, dmg, position):
        pass

class Shrimp(Animal):
    def __init__(self, health, dmg, position):
        pass

class Skunk(Animal):
    def __init__(self, health, dmg, position):
        pass

class Sloth(Animal):
    def __init__(self, health, dmg, position):
        pass

class Snail(Animal):
    def __init__(self, health, dmg, position):
        pass

class Snake(Animal):
    def __init__(self, health, dmg, position):
        pass

class Spider(Animal):
    def __init__(self, health, dmg, position):
        pass

class Squirrel(Animal):
    def __init__(self, health, dmg, position):
        pass

class Swan(Animal):
    def __init__(self, health, dmg, position):
        pass

class Tiger(Animal):
    def __init__(self, health, dmg, position):
        pass


class Turkey(Animal):
    def __init__(self, health, dmg, position):
        pass


class Turtle(Animal):
    def __init__(self, health, dmg, position):
        pass


class Whale(Animal):
    def __init__(self, health, dmg, position):
        pass


class Worm(Animal):
    def __init__(self, health, dmg, position):
        pass
