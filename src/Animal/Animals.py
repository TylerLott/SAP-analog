from random import choice
from typing import List

from src.Animal import Animal
from src.Effect.Effects import MelonEffect, SplashEffect


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

    def onFaint(self, friends: List[Animal]) -> None:
        pos = self.getPosition(friends)
        possible = list(range(len(friends) - 1))
        possible.remove(pos)
        friend = choice(possible)
        friends[friend].addBaseHp(1 * self.getLevel())
        friends[friend].addBaseDmg(2 * self.getLevel())


class Badger(Animal):
    """
    Badger Class

    Level 1: Faint -> Deal 1x attack damage to adjacent animals
    Level 2: Faint -> Deal 2x attack damage to adjacent animals
    Level 3: Faint -> Deal 3x attack damage to adjacent animals
    """

    def __init__(self, health, dmg):

        default_health = 4
        default_dmg = 5
        ability = "Faint: Attack"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onFaint(self, friends: List[Animal], enemies: List[Animal]):
        pos = self.getPosition(friends)
        amt = self.dmg * self.getLevel()
        if pos > 0:
            friends[pos - 1].subHp(amt, friends, enemies)
            friends[pos + 1].subHp(amt, friends, enemies)
        else:
            friends[pos + 1].subHp(amt, friends, enemies)
            enemies[0].subHp(amt, enemies, friends)


class Bat(Animal):
    def __init__(self, health, dmg):

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

    def onSell(self, friends: List[Animal]) -> None:
        pos = self.getPosition(friends)
        possible = list(range(len(friends) - 1))
        possible.remove(pos)
        if len(possible) < 1:
            return
        elif len(possible) < 2:
            friend = possible
            friends[friend[0]].addBaseHp(1 * self.getLevel())
        else:
            friend = choice(possible, k=2)
            friends[friend[0]].addBaseHp(1 * self.getLevel())
            friends[friend[1]].addBaseHp(1 * self.getLevel())


class Bison(Animal):
    """
    Bison Class

    Level 1: End Turn -> Gain +2/+2 if there is a level 3 friend
    Level 2: End Turn -> Gain +4/+4 if there is a level 3 friend
    Level 3: End Turn -> Gain +6/+6 if there is a level 3 friend
    """

    def __init__(self, health, dmg):

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

    def __init__(self, health, dmg):

        default_health = 5
        default_dmg = 3
        ability = "Hurt: Attack"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onHurt(self, friends: List[Animal], enemies: List[Animal]):
        animal = choice(enemies)
        # enemies and friends are flipped because it it hurting an enemy
        animal.subHp(2 * self.getLevel(), enemies, friends)


class Boar(Animal):
    def __init__(self, health, dmg):

        default_health = 6
        default_dmg = 8

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 6


class Camel(Animal):
    """
    Camel Class

    Level 1: Hurt -> give friend behind +1/+2
    Level 2: Hurt -> give friend behind +2/+4
    Level 3: Hurt -> give friend behind +3/+6
    """

    def __init__(self, health, dmg):

        default_health = 5
        default_dmg = 2
        ability = "Hurt: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onHurt(self, friends: List[Animal], enemies: List[Animal]):
        pos = self.getPosition(friends)
        friends[pos + 1].setBaseHp(friends[pos + 1].getBaseHp() + 2 * self.getLevel())
        friends[pos + 1].setBaseDmg(friends[pos + 1].getBaseDmg() + 1 * self.getLevel())


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
    """
    Crab Class

    Level 1: Buy -> Copy health from most healthy friend
    Level 2: Buy -> Copy health from most healthy friend
    Level 3: Buy -> Copy health from most healthy friend
    """

    def __init__(self, health, dmg):

        default_health = 3
        default_dmg = 3
        ability = "Buy: Copy Health"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 2

    def onBuy(self, friends: List[Animal]) -> None:
        high_health = 0
        for i in friends:
            high_health = i.getHp() if i.getHp() > high_health else high_health
        self.setHp(high_health)


class Cricket(Animal):
    """
    Cricket Class

    Level 1: faint -> summon a 1/1 cricket
    Level 2: faint -> summon a 2/2 cricket
    Level 3: faint -> summon a 3/3 cricket
    """

    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 2
        default_dmg = 1
        ability = "Faint: Summon"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 1

    def onFaint(self, friends: List[Animal]) -> None:
        pos = self.getPosition(friends)

        others = list(range(len(friends) - 1))
        others.remove(pos)

        friends[pos] = Cricket()
        friends[pos].setHp(1 * self.getLevel())
        friends[pos].setDmg(1 * self.getLevel())

        for i in others:
            friends[i].onFriendSummoned(friends, friends[pos])


class Crocodile(Animal):
    def __init__(self, health, dmg):

        default_health = 4
        default_dmg = 8

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 5


class Deer(Animal):
    """
    Deer Class

    Level 1: Faint -> Summon a 5/5 Bus with Splash
    Level 2: Faint -> Summon a 10/10 Bus with Splash
    Level 3: Faint -> Summon a 15/15 Bus with Splash
    """

    def __init__(self, health, dmg):

        default_health = 1
        default_dmg = 1
        ability = "Faint: Summon"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 4

    def onFaint(self, friends: list, enemies: list):
        pos = self.getPosition(friends)
        friends[pos] = Bus(5 * self.getLevel(), 5 * self.getLevel())


class Bus(Animal):
    """
    Bus Class

    Only summoned by a deer
    """

    def __init__(self, health, dmg):

        default_health = 0
        default_dmg = 0
        ability = "None"

        super().__init__(
            default_health + health,
            default_dmg + dmg,
            effect=SplashEffect(),
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

    def __init__(self, health, dmg):

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

    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 2
        ability = "Friend Summoned: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onFriendSummoned(self, friends: List[Animal], friend: Animal):
        self.setBaseHp(self.getBaseHp + self.getLevel())
        self.setBaseDmg(self.getBaseDmg + self.getLevel())


class Dolphin(Animal):
    """
    Dolphin Class

    Level 1: Start of Battle -> Deal 5 damage to lowest health enemy
    Level 2: Start of Battle -> Deal 10 damage to lowest health enemy
    Level 3: Start of Battle -> Deal 15 damage to lowest health enemy
    """

    def __init__(self, health, dmg):

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
    def __init__(self, health, dmg):

        default_health = 8
        default_dmg = 6

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 6


class Duck(Animal):
    """
    Duck Class

    Level 1: Sell -> Give shop pets +1 Health
    Level 2: Sell -> Give shop pets +2 Health
    Level 3: Sell -> Give shop pets +3 Health
    """

    def __init__(self, health, dmg):

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

    def __init__(self, health, dmg):

        default_health = 5
        default_dmg = 3
        ability = "Before Attack: Attack"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 2

    def onBeforeAttack(self, friends: List[Animal], enemies: List[Animal]) -> None:
        pos = self.getPosition(friends)
        for i in range(1, self.getLevel() + 1):
            friends[pos + i].subHp(1, friends, enemies)


class Fish(Animal):
    """
    Fish Class

    Level 1: Level-up -> give all friends +1/+1
    Level 2: Level-up -> give all friends +2/+2
    Level 3: None
    """

    def __init__(self, health, dmg):

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

    def __init__(self, health, dmg):

        default_health = 1
        default_dmg = 3
        ability = "Faint: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 2

    def onFaint(self, friends: List[Animal], enemies: List[Animal]) -> None:
        pos = self.getPosition(friends)
        amt = 1 * self.getLevel()
        for i in range(1, 3):
            friends[pos + i].setBaseHp(friends[pos + i].getBaseHp() + amt)
            friends[pos + i].setBaseDmg(friends[pos + i].getBaseDmg() + amt)


class Fly(Animal):
    def __init__(self, health, dmg):

        default_health = 5
        default_dmg = 5

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 6


class Giraffe(Animal):
    """
    Giraffe Class

    Level 1: End Turn -> Give friend ahead +1/+1
    Level 2: End Turn -> Give friend ahead +2/+2
    Level 3: End Turn -> Give friend ahead +3/+3
    """

    def __init__(self, health, dmg):

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
    def __init__(self, health, dmg):

        default_health = 9
        default_dmg = 6

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 6


class Hedgehog(Animal):
    """
    Hedgehog class

    Level 1: Faint -> Deal 2 Dmg to all
    Level 2: Faint -> Deal 4 Dmg to all
    Level 3: Faint -> Deal 6 Dmg to all
    """

    def __init__(self, health, dmg):

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


class Hippo(Animal):
    """
    Hippo Class

    Level 1: Knock Out -> Gain +2/+2
    Level 2: Knock Out -> Gain +4/+4
    Level 3: Knock Out -> Gain +6/+6
    """

    def __init__(self, health, dmg):

        default_health = 7
        default_dmg = 4
        ability = "Knock Out: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 4

    # TODO: Hippo knock out implement


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

    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 1
        ability = "Friend Ahead Attack: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onFriendAheadAttack(self, friends: list, enemies: list):
        self.setBaseHp(self.getBaseHp() + 2 * self.getLevel())
        self.setBaseDmg(self.getBaseDmg() + 2 * self.getLevel())


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
    """
    Mosquito Class

    Level 1: Start of Battle -> Deal 1 Dmg to random enemy
    Level 2: Start of Battle -> Deal 2 Dmg to random enemy
    Level 3: Start of Battle -> Deal 3 Dmg to random enemy
    """

    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 2
        ability = "Start of Battle: Attack"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 1

    def onStartOfBattle(self, friends: List[Animal], enemies: List[Animal]) -> None:
        animal = choice(enemies)
        animal.subHp(1 * self.getLevel(), enemies, friends)


class Monkey(Animal):
    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 5


class Otter(Animal):
    """
    Otter Class

    Level 1: Buy -> give random friend +1/+1
    Level 2: Buy -> give random friend +2/+2
    Level 3: Buy -> give random friend +3/+3
    """

    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 1

    def onBuy(self, friends: List[Animal]):
        pos = self.getPosition(friends)

        others = list(range(len(friends) - 1))
        others.remove(pos)

        friend = choice(others)
        amt = 1 * self.getLevel()

        friends[friend].setBaseHp(friends[friend].getBaseHp() + amt)
        friends[friend].setBaseDmg(friends[friend].getBaseDmg() + amt)


class Ox(Animal):
    """
    Ox Class

    Level 1: Friend Ahead Faints -> Gain Melon, Gain +2 Dmg
    Level 2: Friend Ahead Faints -> Gain Melon, Gain +4 Dmg
    Level 3: Friend Ahead Faints -> Gain Melon, Gain +6 Dmg
    """

    def __init__(self, health, dmg):

        default_health = 4
        default_dmg = 1
        ability = "Friend Ahead Faints: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onFriendAheadFaint(self, friends: List[Animal], enemies: List[Animal]):
        self.setBaseDmg(self.getBaseDmg() + 2 * self.getLevel())
        # TODO: Apply melon armor


class Parrot(Animal):
    # TODO: implement this
    def __init__(self, health, dmg):

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

    def __init__(self, health, dmg):

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

    def __init__(self, health, dmg):

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

    def __init__(self, health, dmg):

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

    def __init__(self, health, dmg):

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

    def __init__(self, health, dmg):

        default_health = 5
        default_dmg = 4

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2

    def onFaint(self, friends: List[Animal], enemies: List[Animal]):
        if len(enemies) < 5:
            enemies.append(DirtyRat())


class DirtyRat(Animal):
    """
    Dirty Rat Class

    Can only be summoned on death of rat, attacks enemy team from back
    """

    def __init__(self, health, dmg):

        default_health = 1
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2

    # TODO: make dirty rat attack enemies


class Rhino(Animal):
    def __init__(self, health, dmg):

        default_health = 8
        default_dmg = 5

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 5


class Rooster(Animal):
    """
    Rooster Class

    Level 1: Faint -> Summon 1 Chick with 1 health and half of the rooster's attack
    Level 2: Faint -> Summon 2 Chicks with 1 health and half of the rooster's attack
    Level 3: Faint -> Summon 3 Chicks with 1 health and half of the rooster's attack
    """

    def __init__(self, health, dmg):

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


class Chick(Animal):
    """
    Chick Class

    Can only be summoned by Rooster
    """

    def __init__(self, health, dmg):

        default_health = 1
        default_dmg = 0

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
    """
    Sheep Class

    Level 1: Faint -> Summon two 2/2 Rams
    Level 2: Faint -> Summon two 4/4 Rams
    Level 3: Faint -> Summon two 6/6 Rams
    """

    def __init__(self, health, dmg):

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


class Ram(Animal):
    """
    Ram Class

    Can only be summoned by Sheep
    """

    def __init__(self, health, dmg):

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

    def __init__(self, health, dmg):

        default_health = 3
        default_dmg = 2
        ability = "Friend Sold: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 2

    def onFriendSold(self, friends: List[Animal]):
        pos = self.getPosition(friends)

        others = list(range(len(friends) - 1))
        others.remove(pos)
        friend = choice(others)

        friends[friend].setBaseHp(friends[friend].getBaseHp() + 1 * self.getLevel())


class Skunk(Animal):
    def __init__(self, health, dmg):

        default_health = 6
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 4


class Sloth(Animal):
    """
    Sloth Class

    No abilities
    """

    def __init__(self, health, dmg):

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

    def __init__(self, health, dmg):

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
    def __init__(self, health, dmg):

        default_health = 6
        default_dmg = 6

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 6


class Spider(Animal):
    """
    Spider Class

    Level 1: Faint -> Summon a level 1 tier 3 pet as a 2/2
    Level 2: Faint -> Summon a level 2 tier 3 pet as a 2/2
    Level 3: Faint -> Summon a level 3 tier 3 pet as a 2/2
    """

    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 2
        ability = "Faint: Summon"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 2

    def onFaint(self, friends: List[Animal], enemies: List[Animal]):
        pos = self.getPosition(friends)
        friends[pos] = getRandomTierAnimal(3, 1 * self.getLevel(), 2, 2)

        others = list(range(len(friends) - 1))
        others.remove(pos)

        for i in others:
            friends[i].onFriendSummoned(friends, friends[pos])


class Squirrel(Animal):
    def __init__(self, health, dmg):

        default_health = 5
        default_dmg = 2

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 4


class Swan(Animal):
    """
    Swan Class

    Level 1: Start of Turn -> +1 gold
    Level 2: Start of Turn -> +2 gold
    Level 3: Start of Turn -> +3 gold
    """

    def __init__(self, health, dmg):

        default_health = 3
        default_dmg = 3

        super().__init__(default_health + health, default_dmg + dmg)
        self.tier = 2

    def onStartOfTurn(self, team) -> None:
        team.add_money(1 * self.getLevel())


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
    """
    Turtle Class

    Level 1: Faint -> give 1 friend behind melon armor
    Level 2: Faint -> give 2 friend behind melon armor
    Level 3: Faint -> give 3 friend behind melon armor
    """

    def __init__(self, health, dmg):

        default_health = 2
        default_dmg = 1
        ability = "Faint: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 3

    def onFaint(self, friends: List[Animal], enemies: List[Animal]):
        for i in range(1, self.getLevel() + 1):
            friends[i] += MelonEffect()


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


### Functions ###

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


def getRandomAnimal(maxTier: int, health_mod: int = 0, dmg_mod: int = 0) -> Animal:
    possible = []
    for i in range(1, maxTier + 1):
        possible += animals[i]
    animal = choice(possible)
    return animal(health_mod, dmg_mod)


def getRandomTierAnimal(tier, level: int, health: int, dmg: int) -> Animal:
    animal = choice(animals[tier])()
    animal.setBaseHp(health)
    animal.setBaseDmg(dmg)
    return animal


if __name__ == "__main__":
    for i in range(10):
        print(getRandomAnimal(3, 0, 0))
