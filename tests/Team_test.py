import unittest

from src.Team import Team
from src.Animal.Animals import *


class TeamTests(unittest.TestCase):
    def test_create(self):
        t = Team()
        t.forceAddAnimal(0, Ant())
        t.forceAddAnimal(1, Cricket())
        t.forceAddAnimal(2, Beaver())
        t.forceAddAnimal(3, Horse())

    def test_friend_summoned(self):
        t = Team()
        t.forceAddAnimal(0, Ant())
        t.forceAddAnimal(1, Cricket())
        t.forceAddAnimal(2, Beaver())
        t.forceAddAnimal(3, Horse())
        t.friends[1].onFaint(t.friends)

        t2 = Team()
        t2.forceAddAnimal(0, Ant())
        t2.forceAddAnimal(1, Cricket())
        t2.forceAddAnimal(2, Beaver())
        t2.forceAddAnimal(3, Horse())
        t2.friends[1].setDmg(2)
        t2.friends[1].setHp(1)

        self.assertEqual(t2.__str__(), t.__str__())

    def test_buy(self):
        pass

    def test_sell(self):
        pass
