from random import choice
from typing import List

from src.Animal import Animal
from src.Effect.Effects import SplashEffect


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


class Bus(Animal):
    def __init__(self, health, dmg):

        default_health = 5
        default_dmg = 5

        super().__init__(
            default_health + health, default_dmg + dmg, effect=SplashEffect()
        )
        self.tier = 4


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
    def __init__(self, health, dmg):

        default_health = 1
        default_dmg = 1

        super().__init__(default_health + health, default_dmg + dmg)
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
    def __init__(self, health: int = 0, dmg: int = 0):

        default_health = 1
        default_dmg = 2
        ability = "Friend Summoned: Buff"

        super().__init__(default_health + health, default_dmg + dmg, ability=ability)
        self.tier = 1

    def onFriendSummoned(self, friends: List[Animal], friend: Animal) -> None:
        friend.addTempDmg(1 * self.getLevel())


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
        animal.subHp(1 * self.getLevel())


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
