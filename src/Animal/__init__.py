from abc import ABC
from random import randrange

from src.Effect import Effect
from src.Effect.Effects import NoneEffect
from src.Food.Foods import Food


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
        """public get hp method"""
        return self.hp

    def getDmg(self) -> int:
        """public get dmg method"""
        return self.dmg

    def getLevel(self) -> int:
        """public get animal level method"""
        if self.exp > 5:
            return 3
        if self.exp > 2:
            return 2
        return 1

    def getExp(self) -> int:
        """public get animal exp method"""
        return self.exp

    def getAbility(self) -> str:
        """
        public get ability method
        Ability should be string describing animal abilities, if any
        """
        return self.ability

    def getEffect(self) -> Effect:
        """public get animal effect method"""
        return self.effect

    def getCost(self) -> int:
        """public get animal cost method"""
        return self.cost

    def getState(self) -> list:
        """public get animal state method"""
        pass

    #### Setters ####

    def addBaseHp(self, amt: int) -> None:
        """public add to base hp method"""
        self.base_hp += amt
        self.__recalcHp()

    def addTempHp(self, amt: int) -> None:
        """public add to temp hp method"""
        self.temp_hp += amt
        self.__recalcHp()

    def subBaseHp(self, amt: int) -> None:
        """public subtract from base hp method"""
        self.base_hp -= amt
        self.__recalcHp()

    def subTempHp(self, amt: int) -> None:
        """
        public subtract from temp hp method
        sets temp hp to 0 if -1 is passed
        """
        if amt == -1:
            self.temp_hp = 0
        else:
            self.temp_hp -= amt
        self.__recalcHp()

    def addBaseDmg(self, amt: int) -> None:
        """public add to base damage method"""
        self.base_dmg += amt
        self.__recalcDmg()

    def addTempDmg(self, amt: int) -> None:
        """public add to temp damage method"""
        self.temp_dmg += amt
        self.__recalcDmg()

    def subBaseDmg(self, amt: int) -> None:
        """public subtract from base damage method"""
        self.base_dmg -= amt
        self.__recalcDmg()

    def subTempDmg(self, amt: int) -> None:
        """
        public subtract from temp damage method
        sets temp damage to 0 if -1 is passed
        """
        if amt == -1:
            self.temp_dmg = 0
        else:
            self.temp_dmg -= amt
        self.__recalcDmg()

    def subHp(self, amt: int) -> None:
        """
        public subtract from hp method
        only for use in a fight
        """
        self.hp -= amt

    def setEffect(self, effect: Effect) -> None:
        """public set effect method"""
        self.effect = effect

    #### Private ####

    def __setHp(self, amt: int) -> None:
        """private set hp method"""
        self.base_hp = amt
        self.__recalcHp()

    def __setDmg(self, amt: int) -> None:
        """private set damage method"""
        self.base_dmg = amt
        self.__recalcDmg()

    def __setExp(self, amt: int) -> None:
        """private set exp method"""
        self.exp = amt

    def __recalcHp(self):
        """private recalcuate total hp method"""
        self.hp = self.temp_hp + self.base_hp

    def __recalcDmg(self):
        """private recalcuate total damage method"""
        self.dmg = self.temp_dmg + self.base_dmg

    #### On Events ####

    # Normal On Events
    def onHit(self, dmgAmt):
        self.hp -= round(dmgAmt * self.dmgModifier)
        if self.hp <= 0:
            self.alive = False

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
        """
        override +=

        can be used to add two of the same animals

        can be used to apply food to an animal

        """
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
            high_exp = (
                self.getLevel()
                if self.getLevel() > other.getLevel()
                else other.getLevel()
            )
            self.__setExp(low_exp + high_exp)
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
            self.onEat()

    def __bool__(self):
        """override boolean value of animal"""
        return True
