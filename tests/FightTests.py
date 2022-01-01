import unittest

from src.Fight import Fight
from src.Team import Team


def createDummy() -> Team:
    t = Team()
    t.buyFriend(0, 0)
    t.buyFriend(1, 1)
    t.buyFriend(2, 2)
    return t


def dummyTurn(team: Team):
    team.nextTurn()
    team.sellFriend(0)
    team.sellFriend(1)
    team.sellFriend(2)
    team.buyFriend(0, 0)
    team.buyFriend(1, 1)
    team.buyFriend(2, 2)


class FightTests(unittest.TestCase):
    def test_simulate(self):
        for i in range(1):
            t1 = createDummy()
            t2 = createDummy()
            f = Fight(t1, t2)
            while t1.getLife() > 0 and t2.getLife() > 0:
                f.simulate()
                dummyTurn(t1)
                dummyTurn(t2)
                print(t1.getRound())
            print(t1)
            print(t2)
