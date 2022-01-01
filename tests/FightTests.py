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
        # currently takes around 3.3 seconds to sim 1000 full games
        # Issues with team 2 winning 2 of 3 games
        # Issues with simulation not ending -> forced to end after 100 fights for now
        team1Wins = 0
        team2Wins = 0
        for i in range(1000):
            t1 = createDummy()
            t2 = createDummy()
            f = Fight(t1, t2)
            turns = 0
            while t1.getLife() > 0 and t2.getLife() > 0 and turns < 100:
                f.simulate()
                dummyTurn(t1)
                dummyTurn(t2)
                turns += 1
            if t1.getLife() > t2.getLife():
                team1Wins += 1
            else:
                team2Wins += 1
        print("Team 1 Wins: ", team1Wins)
        print("Team 2 Wins: ", team2Wins)
