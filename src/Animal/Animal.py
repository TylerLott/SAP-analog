
from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, health, dmg):
        self.health = health
        self.dmg = dmg
        self.alive = True

    def onHit(self, dmgAmt):
        self.dmg -= dmgAmt
        if self.dmg <= 0:
            self.alive = False

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
