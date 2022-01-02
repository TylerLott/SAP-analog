from abc import ABC

from src.Food import Food


class Animal(ABC):
    """
    Animal base class
    """

    ### Init ###

    def __init__(
        self,
        health: int,
        dmg: int,
        effect: str = None,
        ability: str = "None",
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
        self.dmgTakenModifier = 0  # negative if bad
        self.cost = 3
        self.tier = 1

        # Derived
        self.hp = self.temp_hp + self.base_hp
        self.dmg = self.temp_dmg + self.base_dmg

    #### Getters ####

    def getAlive(self) -> bool:
        """public get alive method"""
        return self.alive

    def getHp(self) -> int:
        """public get hp method"""
        return self.hp

    def getBaseHp(self) -> int:
        return self.base_hp

    def getTempHp(self) -> int:
        return self.temp_hp

    def getDmg(self) -> int:
        """public get dmg method"""
        return self.dmg

    def getBaseDmg(self) -> int:
        return self.base_dmg

    def getTempDmg(self) -> int:
        return self.temp_dmg

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

    def getEffect(self) -> str:
        """public get animal effect method"""
        return self.effect

    def getCost(self) -> int:
        """public get animal cost method"""
        return self.cost

    def getPosition(self, friends: list) -> int:
        """public method to get the animals position in a list"""
        for i in range(len(friends) - 1):
            if friends[i] == self:
                return i
        return 0

    def getTier(self) -> int:
        return self.tier

    def getState(self) -> list:
        """public get animal state method"""
        pass

    #### Setters ####

    def setBaseHp(self, amt: int) -> None:
        """public method to set base hp"""
        self.base_hp = amt
        self.__recalcHp()

    def setBaseDmg(self, amt: int) -> None:
        """public method to set base dmg"""
        self.base_dmg = amt
        self.__recalcDmg()

    def setTempHp(self, amt: int) -> None:
        """public method to set temp hp"""
        self.temp_hp = amt
        self.__recalcHp()

    def setTempDmg(self, amt: int) -> None:
        """public method to set temp dmg"""
        self.temp_dmg = amt
        self.__recalcDmg()

    def subHp(self, amt: int, friends: list, enemies: list) -> bool:
        """
        public subtract from hp method

        only for use in a fight

        removes hp from temp_hp then base_hp
        """
        if self.getHp() < 0:
            return

        if self.effect == "melon":
            amt = amt - 20 if amt - 20 > 0 else 0
            self.effect = None
        elif self.effect == "coconut":
            amt = 0
            self.effect = None
        elif self.effect == "garlic":
            amt = amt - 2 if amt - 2 > 1 else 1

        if self.temp_hp > 0:
            self.temp_hp -= amt
            if self.temp_hp < 0:
                amt = abs(self.temp_hp)
                self.temp_hp = 0
        if amt > 0:
            self.base_hp -= amt
        self.__recalcHp()
        if amt > 0:
            self.onHurt(friends, enemies)
        return True if self.getHp() <= 0 else False

    def setHp(self, amt: int) -> None:
        """public set hp method"""
        self.base_hp = amt
        self.__recalcHp()

    def setDmg(self, amt: int) -> None:
        """public set damage method"""
        self.base_dmg = amt
        self.__recalcDmg()

    def setAlive(self, isAlive) -> None:
        self.alive = isAlive

    #### Private ####

    def __setExp(self, amt: int) -> None:
        """private set exp method"""
        self.exp = amt

    def __recalcHp(self) -> bool:
        """
        private recalcuate total hp method

        returns whether the animal is still alive
        """
        self.hp = self.temp_hp + self.base_hp
        if self.hp < 0:
            self.alive = False
        return self.alive

    def __recalcDmg(self):
        """private recalcuate total damage method"""
        self.dmg = self.temp_dmg + self.base_dmg

    #### On Events ####

    # Normal On Events

    def attack(self, friends, enemies):
        dmg = self.getDmg()
        if self.effect == "steak":
            dmg += 20
            self.effect = None
        elif self.effect == "meat":
            dmg += 5

        knockout = enemies[0].subHp(dmg, friends, enemies)
        if knockout:
            self.onKnockOut(friends, enemies)

    ### Special On Events ###
    # These are passed friends or enemy lists of animals so they can be used in shop or fight
    # These should recurse down until there is nothing left

    def onFaint(self, friends: list, enemies: list):
        if self.effect == "honey" and len(friends) < 5:
            pos = self.getPosition(friends)

            others = list(range(len(friends) - 1))
            if len(others) <= 1:
                others = []
            else:
                others.remove(pos)

            friends[pos] = Bee()

            for i in others:
                friends[i].onFriendSummoned(friends, friends[pos])

    def onSell(self, friends: list, team, shop):
        pass

    def onEat(self, friends: list):
        pass

    def onEndOfTurn(self, friends: list):
        pass

    def onLevelUp(self, friends: list):
        pass

    def onFoodBought(self, friends: list):
        pass

    def onStartOfBattle(self, friends: list, enemies: list):
        pass

    def onBuy(self, friends: list, team):
        pass

    def onStartOfTurn(self, team):
        pass

    def onBeforeAttack(self, friends: list, enemies: list):
        pass

    def onHurt(self, friends: list, enemies: list):
        pass

    def onFriendSold(self, friends: list):
        pass

    def onFriendSummoned(self, friends: list, friend):
        pass

    def onFriendAheadAttack(self, friends: list, enemies: list):
        pass

    def onFriendAheadFaint(self, friends: list, enemies: list):
        pass

    def onFriendEat(self, friend):
        pass

    def onFriendFaint(self, friends: list):
        pass

    def onFriendBought(self, friends: list, friend):
        pass

    def onKnockOut(self, friends: list, enemies: list):
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
        out_str += "|" + f'{"Effect: "+ str(self.effect):^30}' + "|\n"
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
            self.setHp(high_hp + low_exp)
            self.setDmg(high_dmg + low_exp)

        # add food to animal
        if issubclass(other.__class__, Food):
            temp_buff = other.getTempBuff()
            perm_buff = other.getPermBuff()
            effect = other.getEffect()

            # TODO implement pill
            if effect == "pill":
                pass

            # TODO implement chocolate
            elif effect == "exp":
                self.__setExp(self.getExp() + 1)

            elif effect != None:
                self.effect = effect

            self.setTempHp(self.getTempHp() + temp_buff[0])
            self.setTempDmg(self.getTempDmg() + temp_buff[1])
            self.setBaseHp(self.getBaseHp() + perm_buff[0])
            self.setBaseDmg(self.getBaseDmg() + perm_buff[1])

            # TODO call self onEat

        return self

    def __add__(self, other):
        """
        override +

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
            self.setHp(high_hp + low_exp)
            self.setDmg(high_dmg + low_exp)

        # add food to animal
        if issubclass(other.__class__, Food):
            temp_buff = other.getTempBuff()
            perm_buff = other.getPermBuff()
            effect = other.getEffect()

            # TODO implement pill
            if effect == "pill":
                pass

            # TODO implement chocolate
            elif effect == "exp":
                self.__setExp(self.getExp() + 1)

            elif effect != None:
                self.effect = effect

            self.setTempHp(self.getTempHp() + temp_buff[0])
            self.setTempDmg(self.getTempDmg() + temp_buff[1])
            self.setBaseHp(self.getBaseHp() + perm_buff[0])
            self.setBaseDmg(self.getBaseDmg() + perm_buff[1])

            # TODO call self onEat

        return self

    def __bool__(self):
        """override boolean value of animal"""
        return True


class Bee(Animal):
    """
    Bee Class

    Spawn from Honey
    Had to put here so no circular imports happened
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 1
        default_dmg = 1
        ability = "None"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 1
