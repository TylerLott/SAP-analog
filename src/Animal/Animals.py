
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