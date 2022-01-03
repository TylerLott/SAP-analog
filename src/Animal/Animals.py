from random import choice, choices
from typing import List
from math import floor

from src.Animal import Animal
from src.Food.Foods import Melon, Milk


class NoneAnimal(Animal):
    """None class for animals"""

    def __init__(self):
        super().__init__(0, 0)

    def __bool__(self):
        return False


class Ant(Animal):
    """
    Ant Class

    level 1: faint -> give random friend +2/+1

    level 2: faint -> give random friend +4/+2

    level 3: faint -> give random friend +6/+3
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 1
        default_dmg = 2
        ability = "Faint: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 1

    def onFaint(self, friends: List[Animal], enemies: List[Animal]) -> None:
        pos, possible = getPosAndOthers(self, friends)

        if len(possible) == 0:
            return
        friend = choice(possible)
        friends[friend].setBaseHp(friends[friend].getBaseHp() + 1 * self.getLevel())
        friends[friend].setBaseDmg(friends[friend].getBaseDmg() + 2 * self.getLevel())
        super().onFaint(friends, enemies)


class Badger(Animal):
    """
    Badger Class

    Level 1: Faint -> Deal 1x attack damage to adjacent animals

    Level 2: Faint -> Deal 2x attack damage to adjacent animals

    Level 3: Faint -> Deal 3x attack damage to adjacent animals
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 4
        default_dmg = 5
        ability = "Faint: Attack"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onFaint(self, friends: List[Animal], enemies: List[Animal]):
        pos = self.getPosition(friends)
        amt = self.dmg * self.getLevel()
        if pos > 0:
            if pos - 1 > -1:
                friends[pos - 1].subHp(amt, friends, enemies)
            if pos + 1 < len(friends):
                friends[pos + 1].subHp(amt, friends, enemies)
        else:
            if pos + 1 < len(friends):
                friends[pos + 1].subHp(amt, friends, enemies)
            if len(enemies) > 0:
                enemies[0].subHp(amt, enemies, friends)
        super().onFaint(friends, enemies)


class Bat(Animal):
    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2


class Beaver(Animal):
    """
    Beaver Class

    Level 1: sell -> give 2 random friends +1 health

    Level 2: sell -> give 2 random friends +2 health

    Level 3: sell -> give 2 random friends +3 health
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 2
        ability = "Sell: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 1

    def onSell(self, friends: List[Animal], team) -> None:
        pos = self.getPosition(friends)
        possible = list(range(len(friends) - 1))
        possible.remove(pos)

        animals = getSubset(possible, k=2)

        for i in animals:
            friends[i].setBaseHp(friends[i].getBaseHp() + self.getLevel())
            friends[i].setBaseDmg(friends[i].getBaseDmg() + self.getLevel())


class Bison(Animal):
    """
    Bison Class

    Level 1: End Turn -> Gain +2/+2 if there is a level 3 friend

    Level 2: End Turn -> Gain +4/+4 if there is a level 3 friend

    Level 3: End Turn -> Gain +6/+6 if there is a level 3 friend
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 6
        default_dmg = 6
        ability = "End Turn: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 4

    def onEndOfTurn(self, friends: List[Animal]):
        isLevel3 = False
        for i in friends:
            if i.getLevel() == 3:
                isLevel3 = True
        if isLevel3:
            self.setBaseHp(self.getBaseHp() + 2 * self.getLevel())
            self.setBaseDmg(self.getBaseDmg() + 2 * self.getLevel())


class Blowfish(Animal):
    """
    Blowfish Class

    Level 1: Hurt -> Deal 2 damage to random enemy

    Level 2: Hurt -> Deal 4 damage to random enemy

    Level 3: Hurt -> Deal 6 damage to random enemy
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 5
        default_dmg = 3
        ability = "Hurt: Attack"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onHurt(self, friends: List[Animal], enemies: List[Animal]):
        if len(enemies) <= 0:
            return
        if len(enemies) == 1:
            animal = enemies[0]
        else:
            animal = choice(enemies)
        # enemies and friends are flipped because it it hurting an enemy
        animal.subHp(2 * self.getLevel(), enemies, friends)


class Boar(Animal):
    """
    Boar Class

    Level 1: Before Attack -> Gain +2/+2

    Level 2: Before Attack -> Gain +4/+4

    Level 3: Before Attack -> Gain +6/+6
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 6
        default_dmg = 8
        ability = "Before Attack: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 6

    def onBeforeAttack(self, friends: list, enemies: list):
        self.setBaseHp(self.getBaseHp() + 2 * self.getLevel())
        self.setBaseDmg(self.getBaseDmg() + 2 * self.getLevel())


class Camel(Animal):
    """
    Camel Class

    Level 1: Hurt -> give friend behind +1/+2

    Level 2: Hurt -> give friend behind +2/+4

    Level 3: Hurt -> give friend behind +3/+6
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 5
        default_dmg = 2
        ability = "Hurt: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onHurt(self, friends: List[Animal], enemies: List[Animal]):
        pos = self.getPosition(friends)
        if pos + 1 < len(friends):
            friends[pos + 1].setBaseHp(
                friends[pos + 1].getBaseHp() + 2 * self.getLevel()
            )
            friends[pos + 1].setBaseDmg(
                friends[pos + 1].getBaseDmg() + 1 * self.getLevel()
            )


class Cat(Animal):
    """
    Cat Class

    Level 1: Food buffs are 2x

    Level 2: Food buffs are 3x

    Level 3: Food buffs are 4x
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 5
        default_dmg = 4
        ability = "Enhance Food"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 6

    # TODO figure out how to implement this


class Cow(Animal):
    """
    Cow Class

    Level 1: Buy -> replace shop food with milk that gives +1/+2

    Level 2: Buy -> replace shop food with milk that gives +2/+4

    Level 3: Buy -> replace shop food with milk that gives +3/+6
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 6
        default_dmg = 4
        ability = "Buy: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 5

    def onBuy(self, friends: list, team):
        for i in range(len(team.shop.items)):
            team.shop.items[i] = Milk(self.getLevel())


class Crab(Animal):
    """
    Crab Class

    Level 1: Buy -> Copy health from most healthy friend

    Level 2: Buy -> Copy health from most healthy friend

    Level 3: Buy -> Copy health from most healthy friend
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 3
        default_dmg = 3
        ability = "Buy: Copy Health"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 2

    def onBuy(self, friends: List[Animal], team) -> None:
        high_health = 0
        for i in friends:
            high_health = i.getHp() if i.getHp() > high_health else high_health
        self.setHp(high_health)


class Cricket(Animal):
    """
    Cricket Class

    Level 1: faint -> summon a 1/1 cricket that is non spawning

    Level 2: faint -> summon a 2/2 cricket that is non spawning

    Level 3: faint -> summon a 3/3 cricket that is non spawning
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 1
        ability = "Faint: Summon"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 1

    def onFaint(self, friends: List[Animal], enemies: List[Animal]) -> None:
        pos = self.getPosition(friends)

        others = list(range(len(friends) - 1))
        if len(others) <= 1:
            others = []
        else:
            others.remove(pos)

        friends[pos] = CricketSpawn(self.getLevel(), self.getLevel())

        for i in others:
            friends[i].onFriendSummoned(friends, friends[pos])
        super().onFaint(friends, enemies)


class CricketSpawn(Animal):
    """
    Cricket Spawn Class

    Only created on Cricket death
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 0
        default_dmg = 0
        ability = "Faint: Summon"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 1


class Crocodile(Animal):
    """
    Crocodile Class

    Level 1: Start of Battle -> Deal 8 Dmg to last enemy

    Level 2: Start of Battle -> Deal 16 Dmg to last enemy

    Level 3: Start of Battle -> Deal 24 Dmg to last enemy
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 4
        default_dmg = 8
        ability = "Start of Battle: Attack"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 5

    def onStartOfBattle(self, friends: List[Animal], enemies: List[Animal]):
        enemies[-1].subHp(8 * self.getLevel(), enemies, friends)


class Deer(Animal):
    """
    Deer Class

    Level 1: Faint -> Summon a 5/5 Bus with Splash

    Level 2: Faint -> Summon a 10/10 Bus with Splash

    Level 3: Faint -> Summon a 15/15 Bus with Splash
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 1
        default_dmg = 1
        ability = "Faint: Summon"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 4

    def onFaint(self, friends: list, enemies: list):
        pos = self.getPosition(friends)
        friends[pos] = Bus(5 * self.getLevel(), 5 * self.getLevel())
        super().onFaint(friends, enemies)


class Bus(Animal):
    """
    Bus Class

    Only summoned by a deer
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 0
        default_dmg = 0
        ability = "None"

        super().__init__(
            default_health + health,
            default_dmg + dmg,
            effect="splash",
            ability=ability,
        )
        self.tier = 4


class Dodo(Animal):
    """
    Dodo Class

    Level 1: Start of Battle -> give 50% of dodo dmg to friend ahead

    Level 2: Start of Battle -> give 100% of dodo dmg to friend ahead

    Level 3: Start of Battle -> give 150% of dodo dmg to friend ahead
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 3
        default_dmg = 2
        ability = "Start of Battle: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 2

    def onStartOfBattle(self, friends: List[Animal], enemies: List[Animal]) -> None:
        pos = self.getPosition(friends)
        if pos == 0:
            return
        animal = friends[pos - 1]
        amt = round(self.dmg * 0.5 * self.getLevel())
        animal.setTempDmg(animal.getTempDmg() + amt)


class Dog(Animal):
    """
    Dog Class

    Level 1: Friend Summoned -> gain +1/+1

    Level 2: Friend Summoned -> gain +2/+2

    Level 3: Friend Summoned -> gain +3/+3
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 2
        ability = "Friend Summoned: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onFriendSummoned(self, friends: List[Animal], friend: Animal):
        self.setBaseHp(self.getBaseHp() + self.getLevel())
        self.setBaseDmg(self.getBaseDmg() + self.getLevel())


class Dolphin(Animal):
    """
    Dolphin Class

    Level 1: Start of Battle -> Deal 5 damage to lowest health enemy

    Level 2: Start of Battle -> Deal 10 damage to lowest health enemy

    Level 3: Start of Battle -> Deal 15 damage to lowest health enemy
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 6
        default_dmg = 4
        ability = "Start of Battle: Attack"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 4

    def onStartOfBattle(self, friends: list, enemies: list):
        lowest = enemies[0]
        for i in enemies:
            if enemies[i].getHp() < lowest.getHp():
                lowest = enemies[i]

        lowest.subHp(5 * self.getLevel(), friends, enemies)


class Dragon(Animal):
    """
    Dragon Class

    Level 1: Buy tier 1 friend -> Give all friends +1/+1

    Level 2: Buy tier 1 friend -> Give all friends +2/+2

    Level 3: Buy tier 1 friend -> Give all friends +3/+3
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 8
        default_dmg = 6
        ability = "Friend Buy: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 6

    def onFriendBought(self, friends: List[Animal], friend: Animal):
        if not friend.getTier() == 1:
            return
        pos = self.getPosition(friends)

        others = list(range(len(friends) - 1))
        others.remove(pos)

        for i in others:
            i.setBaseHp(i.getBaseHp() + self.getLevel())
            i.setBaseDmg(i.getBaseDmg() + self.getLevel())


class Duck(Animal):
    """
    Duck Class

    Level 1: Sell -> Give shop pets +1 Health

    Level 2: Sell -> Give shop pets +2 Health

    Level 3: Sell -> Give shop pets +3 Health
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 1
        ability = "Sell: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 1

    def onSell(self, friends: List[Animal], team):
        for i in team.shop.animals:
            i.setBaseHp(i.getBaseHp() + 1 * self.getLevel())


class Elephant(Animal):
    """
    Elephant Class

    Level 1: Before Attack -> Deal 1 Dmg to 1 friend behind

    Level 2: Before Attack -> Deal 1 Dmg to 2 friends behind

    Level 3: Before Attack -> Deal 1 Dmg to 3 friends behind
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 5
        default_dmg = 3
        ability = "Before Attack: Attack"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 2

    def onBeforeAttack(self, friends: List[Animal], enemies: List[Animal]) -> None:
        pos = self.getPosition(friends)
        for i in range(1, self.getLevel() + 1):
            if pos + i < len(friends):
                friends[pos + i].subHp(1, friends, enemies)


class Fish(Animal):
    """
    Fish Class

    Level 1: Level-up -> give all friends +1/+1

    Level 2: Level-up -> give all friends +2/+2

    Level 3: None
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 3
        default_dmg = 2
        ability = "Level-up: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 1

    def onLevelUp(self, friends: List[Animal]) -> None:
        pos = self.getPosition(friends)

        others = list(range(len(friends) - 1))
        others.remove(pos)

        amt = 1 if self.getLevel() == 1 else 2

        for i in others:
            friends[i].setBaseHp(friends[i].getBaseHp() + amt)
            friends[i].setBaseDmg(friends[i].getBaseDmg() + amt)


class Flamingo(Animal):
    """
    Flamingo Class

    Level 1: Faint -> Give the two friends behind +1/+1

    Level 2: Faint -> Give the two friends behind +2/+2

    Level 3: Faint -> Give the two friends behind +3/+3
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 1
        default_dmg = 3
        ability = "Faint: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 2

    def onFaint(self, friends: List[Animal], enemies: List[Animal]) -> None:
        pos = self.getPosition(friends)
        amt = 1 * self.getLevel()
        for i in range(1, 3):
            if pos + i < len(friends):
                friends[pos + i].setBaseHp(friends[pos + i].getBaseHp() + amt)
                friends[pos + i].setBaseDmg(friends[pos + i].getBaseDmg() + amt)
        super().onFaint(friends, enemies)


class Fly(Animal):
    """
    Fly Class

    Level 1: Friend Faints -> Summon a 5/5 fly in it's place

    Level 2: Friend Faints -> Summon a 10/10 fly in it's place

    Level 3: Friend Faints -> Summon a 15/15 fly in it's place
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 5
        default_dmg = 5
        ability = "Friend Faint: Summon"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 6

    def onFriendFaint(self, friends: List[Animal]):
        # TODO figure out how to find location to insert fly
        return super().onFriendFaint()


class Giraffe(Animal):
    """
    Giraffe Class

    Level 1: End Turn -> Give friend ahead +1/+1

    Level 2: End Turn -> Give friend ahead +2/+2

    Level 3: End Turn -> Give friend ahead +3/+3
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 5
        default_dmg = 2
        ability = "End Turn: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onEndOfTurn(self, friends: List[Animal]) -> None:
        pos = self.getPosition(friends)
        friends[pos - 1].setBaseHp(friends[pos - 1].getBaseHp() + self.getLevel())
        friends[pos - 1].setBaseDmg(friends[pos - 1].getBaseDmg() + self.getLevel())


class Gorilla(Animal):
    """
    Gorilla Class

    All Levels: Hurt -> Gain coconut shield
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 9
        default_dmg = 6
        ability = "Hurt: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 6

    def onHurt(self, friends: list, enemies: list):
        self.effect = "coconut"


class Hedgehog(Animal):
    """
    Hedgehog class

    Level 1: Faint -> Deal 2 Dmg to all

    Level 2: Faint -> Deal 4 Dmg to all

    Level 3: Faint -> Deal 6 Dmg to all
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 3
        ability = "Faint: Attack"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 2

    def onFaint(self, friends: List[Animal], enemies: List[Animal]):
        amt = 2 * self.getLevel()
        for i in friends:
            i.subHp(amt, friends, enemies)
        for i in enemies:
            i.subHp(amt, enemies, friends)
        super().onFaint(friends, enemies)


class Hippo(Animal):
    """
    Hippo Class

    Level 1: Knock Out -> Gain +2/+2

    Level 2: Knock Out -> Gain +4/+4

    Level 3: Knock Out -> Gain +6/+6
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 7
        default_dmg = 4
        ability = "Knock Out: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 4

    def onKnockOut(self, friends: List[Animal], enemies: List[Animal]):
        self.setBaseHp(self.getBaseHp() + 2 * self.getLevel())
        self.setBaseDmg(self.getBaseDmg() + 2 * self.getLevel())


class Horse(Animal):
    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 1
        default_dmg = 2
        ability = "Friend Summoned: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 1

    def onFriendSummoned(self, friends: List[Animal], friend: Animal) -> None:
        friend.setTempDmg(friend.getTempDmg() + 1 * self.getLevel())


class Kangaroo(Animal):
    """
    Kangaroo Class

    Level 1: Friend Ahead Attack -> Gain +2/+2

    Level 2: Friend Ahead Attack -> Gain +4/+4

    Level 3: Friend Ahead Attack -> Gain +6/+6
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 1
        ability = "Friend Ahead Attack: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onFriendAheadAttack(self, friends: list, enemies: list):
        self.setBaseHp(self.getBaseHp() + 2 * self.getLevel())
        self.setBaseDmg(self.getBaseDmg() + 2 * self.getLevel())


class Leopard(Animal):
    """
    Leopard Class

    Level 1: Start of battle -> Deal 50% attack damage to 1 random enemy

    Level 2: Start of battle -> Deal 50% attack damage to 2 random enemies

    Level 3: Start of battle -> Deal 50% attack damage to 3 random enemies
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 4
        default_dmg = 10
        ability = "Start of Battle: Attack"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 6

    def onStartOfBattle(self, friends: list, enemies: List[Animal]):
        animals = getSubset(enemies, k=self.getLevel())
        for i in animals:
            enemies[i].subHp(round(self.getDmg() * 0.5), enemies, friends)


class Mammoth(Animal):
    """
    Mammoth Class

    Level 1: Faint -> Give all friends +2/+2

    Level 2: Faint -> Give all friends +4/+4

    Level 3: Faint -> Give all friends +6/+6
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 10
        default_dmg = 3
        ability = "Faint: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 6

    def onFaint(self, friends: List[Animal], enemies: list):
        pos, others = getPosAndOthers(self, friends)

        for i in others:
            friends[i].setBaseHp(friends[i].getBaseHp() + 2 * self.getLevel())
            friends[i].setBaseDmg(friends[i].getBaseDmg() + 2 * self.getLevel())
        super().onFaint(friends, enemies)


class Mosquito(Animal):
    """
    Mosquito Class

    Level 1: Start of Battle -> Deal 1 Dmg to random enemy

    Level 2: Start of Battle -> Deal 2 Dmg to random enemy

    Level 3: Start of Battle -> Deal 3 Dmg to random enemy
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 2
        ability = "Start of Battle: Attack"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 1

    def onStartOfBattle(self, friends: List[Animal], enemies: List[Animal]) -> None:
        animal = choice(enemies)
        animal.subHp(1 * self.getLevel(), enemies, friends)


class Monkey(Animal):
    """
    Monkey Class

    Level 1: End Turn -> Give right-most friend +3/+3

    Level 2: End Turn -> Give right-most friend +6/+6

    Level 3: End Turn -> Give right-most friend +9/+9
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 1
        ability = "End Turn: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 5

    def onEndOfTurn(self, friends: List[Animal]):
        friends[0].setBaseHp(friends[0].getBaseHp() + 3 * self.getLevel())
        friends[0].setBaseDmg(friends[0].getBaseDmg() + 3 * self.getLevel())


class Otter(Animal):
    """
    Otter Class

    Level 1: Buy -> give random friend +1/+1

    Level 2: Buy -> give random friend +2/+2

    Level 3: Buy -> give random friend +3/+3
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 1

    def onBuy(self, friends: List[Animal], team):
        pos = self.getPosition(friends)

        possible = list(range(len(friends) - 1))
        possible.remove(pos)

        friend = getSubset(possible, k=1)
        amt = self.getLevel()

        for i in friend:
            friends[i].setBaseHp(friends[i].getBaseHp() + amt)
            friends[i].setBaseDmg(friends[i].getBaseDmg() + amt)


class Ox(Animal):
    """
    Ox Class

    Level 1: Friend Ahead Faints -> Gain Melon, Gain +2 Dmg

    Level 2: Friend Ahead Faints -> Gain Melon, Gain +4 Dmg

    Level 3: Friend Ahead Faints -> Gain Melon, Gain +6 Dmg
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 4
        default_dmg = 1
        ability = "Friend Ahead Faints: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onFriendAheadFaint(self, friends: List[Animal], enemies: List[Animal]):
        self.setBaseDmg(self.getBaseDmg() + 2 * self.getLevel())
        self += Melon()


class Parrot(Animal):
    # TODO: implement this maybe just replace this animal with the animal type in front and carry over the stats
    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 3
        default_dmg = 5

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 4


class Peacock(Animal):
    """
    Peacock Class

    Level 1: Hurt -> gain +2 attack

    Level 2: Hurt -> gain +4 attack

    Level 3: Hurt -> gain +6 attack
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 5
        default_dmg = 1
        ability = "Hurt: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 2

    def onHurt(self, friends: List[Animal], enemies: List[Animal]):
        self.setBaseDmg(self.getBaseDmg() + 2 * self.getLevel())


class Penguin(Animal):
    """
    Penguin Class

    Level 1: End Turn -> Give other level 2 and 3 friends +1/+1

    Level 2: End Turn -> Give other level 2 and 3 friends +2/+2

    Level 3: End Turn -> Give other level 2 and 3 friends +3/+3
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 1
        ability = "End Turn: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 4

    def onEndOfTurn(self, friends: List[Animal]):
        for i in friends:
            if i.getLevel() > 1:
                i.setBaseHp(i.getBaseHp() + self.getLevel())
                i.setBaseDmg(i.getBaseDmg() + self.getLevel())


class Pig(Animal):
    """
    Pig Class

    Level 1: Sell -> Give 1 extra gold

    Level 2: Sell -> Give 2 extra gold

    Level 3: Sell -> Give 3 extra gold
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 1
        default_dmg = 3
        ability = "Sell: Extra Gold"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 1

    def onSell(self, friends: List[Animal], team):
        team.add_money(1 * self.getLevel())


class Rabbit(Animal):
    """
    Rabbit Class

    Level 1: Friend Eats -> Give additional +1 Health

    Level 2: Friend Eats -> Give additional +2 Health

    Level 3: Friend Eats -> Give additional +3 Health
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 3
        ability = "Friend Eats: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onFriendEat(self, friend: Animal):
        friend.setBaseHp(friend.getBaseHp() + self.getLevel())


class Rat(Animal):
    """
    Rat Class

    Level 1: Faint -> Summons 1/1 Dirty Rat at the back of the enemy team

    Level 2: Faint -> Summons 1/1 Dirty Rat at the back of the enemy team

    Level 3: Faint -> Summons 1/1 Dirty Rat at the back of the enemy team
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 5
        default_dmg = 4

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2

    def onFaint(self, friends: List[Animal], enemies: List[Animal]):
        if len(enemies) < 5:
            enemies.append(DirtyRat(0, 0))
        super().onFaint(friends, enemies)


class DirtyRat(Animal):
    """
    Dirty Rat Class

    Can only be summoned on death of rat, attacks enemy team from back
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 1
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2

    # TODO: make dirty rat attack enemies


class Rhino(Animal):
    """
    Rhino Class

    Level 1: Knock Out: Deal 4 damage to first enemy

    Level 2: Knock Out: Deal 8 damage to first enemy

    Level 3: Knock Out: Deal 12 damage to first enemy
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 8
        default_dmg = 5
        ability = "Knock Out: Attack"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 5

    def onKnockOut(self, friends: list, enemies: List[Animal]):
        if len(enemies) > 0:
            enemies[0].subHp(4 * self.getLevel(), enemies, friends)


class Rooster(Animal):
    """
    Rooster Class

    Level 1: Faint -> Summon 1 Chick with 1 health and half of the rooster's attack

    Level 2: Faint -> Summon 2 Chicks with 1 health and half of the rooster's attack

    Level 3: Faint -> Summon 3 Chicks with 1 health and half of the rooster's attack
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 3
        default_dmg = 5
        ability = "Faint: Summon"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 4

    def onFaint(self, friends: List[Animal], enemies: List[Animal]):
        pos = self.getPosition(friends)
        attack = round(0.5 * self.getDmg())
        if len(friends) == 5:
            friends[pos] = Chick(0, attack)
            for i in friends:
                i.onFriendSummoned(friends, friends[pos])
        elif len(friends) == 4:
            friends[pos] = Chick(0, attack)
            for i in friends:
                i.onFriendSummoned(friends, friends[pos])
            friends.insert(pos, Chick(0, attack))
            for i in friends:
                i.onFriendSummoned(friends, friends[pos])
        else:
            friends[pos] = Chick(0, attack)
            for i in friends:
                i.onFriendSummoned(friends, friends[pos])
            friends.insert(pos, Chick(0, attack))
            for i in friends:
                i.onFriendSummoned(friends, friends[pos])
            friends.insert(pos, Chick(0, attack))
            for i in friends:
                i.onFriendSummoned(friends, friends[pos])
        super().onFaint(friends, enemies)


class Chick(Animal):
    """
    Chick Class

    Can only be summoned by Rooster
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 1
        default_dmg = 0

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 4


class Scorpion(Animal):
    """
    Scorpion Class

    No Abilities
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 1
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg, effect="poison")
        self.tier = 5


class Seal(Animal):
    """
    Seal Class

    Level 1: Eat -> Give 2 random friends +1/+1

    Level 2: Eat -> Give 2 random friends +2/+2

    Level 3: Eat -> Give 2 random friends +3/+3
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 8
        default_dmg = 3
        ability = "Eat: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 5

    def onEat(self, friends: List[Animal]):
        pos = self.getPosition(friends)

        others = list(range(len(friends) - 1))
        others.remove(pos)

        animals = getSubset(others, k=2)
        for i in animals:
            friends[i].setBaseHp(friends[i].getBaseHp() + self.getLevel())
            friends[i].setBaseDmg(friends[i].getBaseDmg() + self.getLevel())


class Shark(Animal):
    """
    Shark Class

    Level 1: Friend Faint -> Gain +2/+1

    Level 2: Friend Faint -> Gain +4/+2

    Level 3: Friend Faint -> Gain +6/+3
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 4
        default_dmg = 4
        ability = "Friend Faint: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 5

    def onFriendFaint(self):
        self.setBaseHp(self.getBaseHp() + self.getLevel())
        self.setBaseDmg(self.getBaseDmg() + 2 * self.getLevel())


class Sheep(Animal):
    """
    Sheep Class

    Level 1: Faint -> Summon two 2/2 Rams

    Level 2: Faint -> Summon two 4/4 Rams

    Level 3: Faint -> Summon two 6/6 Rams
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 2
        ability = "Faint: Summon"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onFaint(self, friends: List[Animal], enemies: List[Animal]):
        pos = self.getPosition(friends)
        if len(friends) == 5:
            friends[pos] = Ram(2 * self.getLevel(), 2 * self.getLevel())
            for i in friends:
                i.onFriendSummoned(friends, friends[pos])
        else:
            friends[pos] = Ram(2 * self.getLevel(), 2 * self.getLevel())
            for i in friends:
                i.onFriendSummoned(friends, friends[pos])
            friends.insert(pos, Ram(2 * self.getLevel(), 2 * self.getLevel()))
            for i in friends:
                i.onFriendSummoned(friends, friends[pos])
        super().onFaint(friends, enemies)


class Ram(Animal):
    """
    Ram Class

    Can only be summoned by Sheep
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 0
        default_dmg = 0
        ability = "None"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3


class Shrimp(Animal):
    """
    Shrimp Class

    Level 1: Friend Sold -> Give random friend +1 Health

    Level 2: Friend Sold -> Give random friend +2 Health

    Level 3: Friend Sold -> Give random friend +3 Health
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 3
        default_dmg = 2
        ability = "Friend Sold: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 2

    def onFriendSold(self, friends: List[Animal]):
        pos = self.getPosition(friends)

        others = list(range(len(friends) - 1))
        others.remove(pos)
        friend = getSubset(others, k=1)

        for i in friend:
            friends[i].setBaseHp(friends[i].getBaseHp() + self.getLevel())


class Skunk(Animal):
    """
    Skunk Class

    Level 1: Start of Battle -> Reduce the highest health enemy by 33%

    Level 2: Start of Battle -> Reduce the highest health enemy by 66%

    Level 3: Start of Battle -> Reduce the highest health enemy by 99%
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 6
        default_dmg = 3
        ability = "Start of Battle: Debuff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 4

    def onStartOfBattle(self, friends: List[Animal], enemies: List[Animal]):
        highest = enemies[0]
        for i in enemies:
            if i.getHp() > highest.getHp():
                highest = i
        highest.subHp(floor(0.33 * highest.getHp()), enemies, friends)


class Sloth(Animal):
    """
    Sloth Class

    No abilities
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 1
        default_dmg = 1
        ability = "Moral Support"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 1


class Snail(Animal):
    """
    Snail Class

    Level 1: Buy -> if lost last battle, give all +2/+1

    Level 2: Buy -> if lost last battle, give all +4/+2

    Level 3: Buy -> if lost last battle, give all +6/+3
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 2
        ability = "Buy: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onBuy(self, friends: List[Animal], team):
        if not team.wonLast:
            for i in friends:
                if i != self:
                    i.setBaseHp(i.getBaseHp() + self.getLevel())
                    i.setBaseDmg(i.getBaseDmg() + 2 * self.getLevel())


class Snake(Animal):
    """
    Snake Class

    Level 1: Friend Ahead Attacks -> Deal 5 damage to random enemy

    Level 2: Friend Ahead Attacks -> Deal 10 damage to random enemy

    Level 3: Friend Ahead Attacks -> Deal 15 damage to random enemy
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 6
        default_dmg = 6
        ability = "Friend Ahead Attack: Attack"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 6

    def onFriendAheadAttack(self, friends: list, enemies: List[Animal]):
        animal = choice(enemies)

        animal.subHp(5 * self.getLevel(), enemies, friends)


class Spider(Animal):
    """
    Spider Class

    Level 1: Faint -> Summon a level 1 tier 3 pet as a 2/2

    Level 2: Faint -> Summon a level 2 tier 3 pet as a 2/2

    Level 3: Faint -> Summon a level 3 tier 3 pet as a 2/2
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 2
        ability = "Faint: Summon"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 2

    def onFaint(self, friends: List[Animal], enemies: List[Animal]):
        pos, others = getPosAndOthers(self, friends)
        friends[pos] = getRandomTierAnimal(3, 1 * self.getLevel(), 2, 2)

        for i in others:
            friends[i].onFriendSummoned(friends, friends[pos])
        super().onFaint(friends, enemies)


class Squirrel(Animal):
    """
    Squirrel Class

    Level 1: Start of Turn -> Discount shop food by 1 gold

    Level 2: Start of Turn -> Discount shop food by 2 gold

    Level 3: Start of Turn -> Discount shop food by 3 gold
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 5
        default_dmg = 2
        ability = "Start of Turn: Discount"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 4

    def onStartOfTurn(self, team):
        for i in team.shop.items:
            if not i.__class__.__name__ == "Pill":
                i.setCost(i.getCost() - self.getLevel())


class Swan(Animal):
    """
    Swan Class

    Level 1: Start of Turn -> +1 gold

    Level 2: Start of Turn -> +2 gold

    Level 3: Start of Turn -> +3 gold
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 3
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2

    def onStartOfTurn(self, team) -> None:
        team.add_money(1 * self.getLevel())


class Tiger(Animal):
    """
    Tiger Class

    Level 1: Friend ahead repeated their ability as if they were a level 1

    Level 2: Friend ahead repeated their ability as if they were a level 2

    Level 3: Friend ahead repeated their ability as if they were a level 3
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 3
        default_dmg = 4
        ability = "Buff Friend"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 6

    # TODO figure out how to implement this


class Turkey(Animal):
    """
    Turkey Class

    Level 1: Friend Summoned -> give it +3/+3

    Level 2: Friend Summoned -> give it +6/+6

    Level 3: Friend Summoned -> give it +9/+9
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 4
        default_dmg = 3
        ability = "Friend Summoned: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 5

    def onFriendSummoned(self, friends: list, friend: Animal):
        friend.setBaseHp(self.getBaseHp() + 3 * self.getLevel())
        friend.setBaseDmg(self.getBaseDmg() + 3 * self.getLevel())


class Turtle(Animal):
    """
    Turtle Class

    Level 1: Faint -> give 1 friend behind melon armor

    Level 2: Faint -> give 2 friend behind melon armor

    Level 3: Faint -> give 3 friend behind melon armor
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 1
        ability = "Faint: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onFaint(self, friends: List[Animal], enemies: List[Animal]):
        for i in range(1, self.getLevel() + 1):
            if i < len(friends):
                friends[i] += Melon()
        super().onFaint(friends, enemies)


class Whale(Animal):
    """
    Whale Class

    Level 1: Start of Battle -> Swallow friend ahead and release as level 1 after fainting

    Level 2: Start of Battle -> Swallow friend ahead and release as level 2 after fainting

    Level 3: Start of Battle -> Swallow friend ahead and release as level 3 after fainting
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 6
        default_dmg = 2
        ability = "Faint: Summon"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 4
        self.jonah = NoneAnimal()

    def onStartOfBattle(self, friends: List[Animal], enemies: List[Animal]):
        pos, others = getPosAndOthers(self, friends)
        if pos == 0:
            return
        self.jonah = friends[pos - 1].__class__()
        friends[pos - 1].onFaint(friends, enemies)
        friends[pos - 1].setAlive(False)

    def onFaint(self, friends: List[Animal], enemies: List[Animal]):
        pos = self.getPosition(friends)
        friends[pos] = self.jonah
        while friends[pos].getLevel() < self.getLevel():
            friends[pos] += friends[pos].__class__()
        super().onFaint(friends, enemies)


class Worm(Animal):
    """
    Worm Class

    Level 1: Eat -> Gain +1/+1

    Level 2: Eat -> Gain +2/+2

    Level 3: Eat -> Gain +3/+3
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 2
        ability = "Eat: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 4

    def onEat(self, friends: list):
        self.setBaseHp(self.getBaseHp() + self.getLevel())
        self.setBaseDmg(self.getBaseDmg() + self.getLevel())


### Constants ###

animals = {
    1: [Ant, Beaver, Cricket, Duck, Fish, Horse, Mosquito, Otter, Pig],
    2: [Crab, Dodo, Elephant, Flamingo, Hedgehog, Peacock, Rat, Shrimp, Spider, Swan],
    3: [
        Badger,
        Blowfish,
        Camel,
        Dog,
        Giraffe,
        Kangaroo,
        Ox,
        Rabbit,
        Sheep,
        Snail,
        Turtle,
    ],
    4: [
        Bison,
        Deer,
        Dolphin,
        Hippo,
        Parrot,
        Penguin,
        Rooster,
        Skunk,
        Squirrel,
        Whale,
        Worm,
    ],
    5: [Cow, Crocodile, Monkey, Rhino, Scorpion, Seal, Shark, Turkey],
    6: [Boar, Cat, Dragon, Fly, Gorilla, Leopard, Mammoth, Snake, Tiger],
}

### Functions ###


def getRandomAnimal(maxTier: int, health_mod: int = 0, dmg_mod: int = 0) -> Animal:
    possible = []
    for i in range(1, maxTier + 1):
        possible += animals[i]
    animal = choice(possible)
    return animal(health_mod, dmg_mod)


def getRandomTierAnimal(tier, level: int, health: int, dmg: int) -> Animal:
    animal = choice(animals[tier])(0, 0)
    animal.setBaseHp(health)
    animal.setBaseDmg(dmg)
    # TODO apply level to new animal
    return animal


def getSubset(possible: List[int], k: int) -> List[int]:
    if len(possible) <= k:
        return possible
    return choices(possible, k=k)


def getPosAndOthers(friend: Animal, friends: List[Animal]) -> list:
    # return [pos, [others]]
    pos = friend.getPosition(friends)
    possible = list(range(len(friends) - 1))

    if len(possible) <= 1:
        possible = []
    else:
        possible.remove(pos)

    return [pos, possible]


if __name__ == "__main__":
    for i in range(10):
        print(getRandomAnimal(3, 0, 0))
