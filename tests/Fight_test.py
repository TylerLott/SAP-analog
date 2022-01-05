import unittest

from numpy.lib.function_base import average

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
    while team.getMoney() > 0:
        team.rollShop()


class FightTests(unittest.TestCase):
    def test_simulate(self):
        # currently takes around 4 seconds to sim 1000 full games
        team1Wins = 0
        team2Wins = 0
        err = 0
        avgMoves = []
        for i in range(1000):
            t1 = createDummy()
            t2 = createDummy()

            turns = 0
            while t1.getLife() > 0 and t2.getLife() > 0 and turns < 100:

                dummyTurn(t1)
                dummyTurn(t2)
                f = Fight(t1, t2)
                f.simulate()

                avgMoves.append(t1.getMovesNum())
                avgMoves.append(t2.getMovesNum())

                turns += 1
            if t1.getLife() > t2.getLife():
                team1Wins += 1
            else:
                team2Wins += 1

        self.assertAlmostEqual((team1Wins / 1000), 0.5, 1)  # even within 10%
