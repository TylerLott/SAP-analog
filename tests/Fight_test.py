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
        # Issues with 1/3 of games erroring
        # error games are forced to end after 100 fights for now, both teams always have 10 health...
        team1Wins = 0
        team2Wins = 0
        err = 0
        for i in range(1000):
            t1 = createDummy()
            t2 = createDummy()

            turns = 0
            while t1.getLife() > 0 and t2.getLife() > 0 and turns < 100:

                dummyTurn(t1)
                dummyTurn(t2)
                f = Fight(t1, t2)
                f.simulate()

                turns += 1
            if not turns < 100:
                err += 1
                err_team1 = t1
                err_team2 = t2
                continue
            if t1.getLife() > t2.getLife():
                team1Wins += 1
            else:
                team2Wins += 1
        print("Team 1 Wins: ", team1Wins)
        print("Team 2 Wins: ", team2Wins)
        print(
            "Error Games: ", err
        )  # doesn't seem to be a single animal type causing this...

        print(err_team1.friends)
        print(err_team2.friends)
