
from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, health, dmg, position):
        self.health = health
        self.dmg = dmg
        self.position = position
        self.alive = True
        self.level = 1 # above 5: level 3, above 3: level 2, less: level 1

    def onHit(self, dmgAmt):
        self.dmg -= dmgAmt
        if self.dmg <= 0:
            self.alive = False

    def onCombine(self):
        self.level += 1     

    def updatePosition(self, pos):
        self.position = pos      

    @abstractmethod
    def onfaint(self):
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
