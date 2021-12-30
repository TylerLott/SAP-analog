from abc import ABC, abstractmethod
from random import randrange
from typing import Union

from src.Food.Effect.Effect import *
from src.Food.Food import Food


class Animal(ABC):
    """
    Animal base class
    """

    ### Init ###

    def __init__(
        self, health: int, dmg: int, effect: Effect = NoneEffect, ability: str = "None"
    ) -> None:
        # Default
        self.temp_hp = 0
        self.temp_dmg = 0
        self.base_hp = health
        self.base_dmg = dmg
        self.alive = True
        self.exp = 1  # above 5: level 3, above 3: level 2, less: level 1
        self.ability = ability
        self.effect = effect
        self.dmgModifier = 1
        self.cost = 3

        # Derived
        self.hp = self.temp_hp + self.base_hp
        self.dmg = self.temp_dmg + self.base_dmg

    #### Getters ####

    def getHp(self) -> int:
        return self.hp

    def getDmg(self) -> int:
        return self.dmg

    def getLevel(self) -> int:
        if self.exp > 5:
            return 3
        if self.exp > 2:
            return 2
        return 1

    def getExp(self) -> int:
        return self.exp

    def getAbility(self) -> str:
        """Ability should be string describing animal abilities, if any"""
        return self.ability

    def getEffect(self) -> Effect:
        return self.effect

    def getCost(self) -> int:
        return self.cost

    def getState(self) -> list:
        pass

    #### Setters ####

    def addBaseHp(self, amt: int) -> None:
        self.base_hp += amt
        self.__recalcHp()

    def addTempHp(self, amt: int) -> None:
        self.temp_hp += amt
        self.__recalcHp()

    def subBaseHp(self, amt: int) -> None:
        self.base_hp -= amt
        self.__recalcHp()

    def subTempHp(self, amt: int) -> None:
        if amt == -1:
            self.temp_hp = 0
        else:
            self.temp_hp -= amt
        self.__recalcHp()

    def addBaseDmg(self, amt: int) -> None:
        self.base_dmg += amt
        self.__recalcDmg()

    def addTempDmg(self, amt: int) -> None:
        self.temp_dmg += amt
        self.__recalcDmg()

    def subBaseDmg(self, amt: int) -> None:
        self.base_dmg -= amt
        self.__recalcDmg()

    def subTempDmg(self, amt: int) -> None:
        if amt == -1:
            self.temp_dmg = 0
        else:
            self.temp_dmg -= amt
        self.__recalcDmg()

    def subHp(self, amt: int) -> None:
        # Only for use in battle
        self.hp -= amt

    def setEffect(self, effect: Effect) -> None:
        self.effect = effect

    def setFood(self, food: Food) -> None:
        pass

    #### Private ####

    def __setHp(self, amt: int) -> None:
        self.base_hp = amt
        self.__recalcHp()

    def __setDmg(self, amt: int) -> None:
        self.base_dmg = amt
        self.__recalcDmg()

    def __recalcHp(self):
        self.hp = self.temp_hp + self.base_hp

    def __recalcDmg(self):
        self.dmg = self.temp_dmg + self.base_dmg

    #### On Events ####

    # Normal On Events
    def onHit(self, dmgAmt):
        self.hp -= round(dmgAmt * self.dmgModifier)
        if self.hp <= 0:
            self.alive = False

    def onCombine(self, animal):
        self.exp += animal.getExp()
        self.base_hp += animal.getExp()
        self.base_dmg += animal.getExp()

    # Special On Events
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

    ### Overrides ###

    def __str__(self):
        out_str = "|==============================|\n"
        out_str += "|" + f"{self.__class__.__name__:^30}" + "|\n"
        out_str += "|------------------------------|\n"
        out_str += "|" + f'{"Health: " + str(self.hp):^30}' + "|\n"
        out_str += "|" + f'{"Damage: "+ str(self.dmg):^30}' + "|\n"
        out_str += "|" + f'{"Exp Level: "+ str(self.getLevel()):^30}' + "|\n"
        out_str += "|" + f'{"Ability: " + self.getAbility():^30}' + "|\n"
        out_str += "|" + f'{"Effect: "+ self.getEffect().__name__:^30}' + "|\n"
        out_str += "|" + f'{"Cost: "+ str(self.cost):^30}' + "|\n"
        out_str += "|==============================|\n"

        return out_str

    def __iadd__(self, other):
        # add two animals
        if other.__class__ == self.__class__:
            high_hp = self.base_hp if self.base_hp > other.base_hp else other.base_hp
            high_dmg = (
                self.base_dmg if self.base_dmg > other.base_dmg else other.base_dmg
            )
            low_exp = (
                self.getLevel()
                if self.getLevel() < other.getLevel()
                else other.getLevel()
            )
            self.__setHp(high_hp + low_exp)
            self.__setDmg(high_dmg + low_exp)

        # add food to animal
        if type(other) == Food:
            temp_buff = other.getTempBuff()
            perm_buff = other.getPermBuff()
            effect = other.getEffect()

            if type(effect) != NoneEffect:
                self.effect = effect

            self.addTempHp(temp_buff[0])
            self.addTempDmg(temp_buff[1])
            self.addBaseHp(perm_buff[0])
            self.addBaseDmg(perm_buff[1])


class Ant(Animal):
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
