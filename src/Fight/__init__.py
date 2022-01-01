from typing import List

from src.Animal import Animal
from src.Team import Team


class Fight:
    """
    Fight Class

    Takes in two teams and simulates the battle
    """

    def __init__(self, team1: Team, team2: Team):
        self.team1 = team1
        self.team2 = team2
        self.team1Friends = team1.getFriendCopy()
        self.team2Friends = team2.getFriendCopy()
        # Copy teams into new arrays
        # turn order is based on damage

    ### Actions ###

    def simulate(self) -> None:
        """
        onStartOfBattle in order of dmg
            onFaint if dies
            onAheadFaint if ahead dies
            onFriendSummoned if summoned
            onHurt if hurt

        while loop til no animals on one team
            onStartOfTurn
            onBeforeAttack for front animals
            attack - using getDmg and subHp
            onFaint
                if faint pop that animal out of arr
                if summons add animal in the dead one's place
                    call onSummoned for all others
            onHurt
            onFriendAheadFaint
            onFriendAheadAttack if not faint
        """

        # I might need to make like a move buffer and just load into
        # that rather than recursively calling everything

        [print(i) for i in self.team1Friends]

        # Remove all of the NoneAnimals()
        newTeam1 = []
        for i in self.team1Friends:
            if i:
                newTeam1.append(i)
        self.team1Friends = newTeam1

        newTeam2 = []
        for i in self.team2Friends:
            if i:
                newTeam2.append(i)
        self.team2Friends = newTeam2

        # get start of fight move order for each team
        sob1 = self.__getMoveOrder(self.team1Friends)
        sob2 = self.__getMoveOrder(self.team2Friends)

        [print(i) for i in self.team1Friends]
        print(sob1)

        for i in range(5):
            try:
                self.team1Friends[sob1[i]].onStartOfBattle(
                    self.team1Friends, self.team2Friends
                )
            except:
                pass
            try:
                self.team2Friends[sob2[i]].onStartOfBattle(
                    self.team2Friends, self.team1Friends
                )
            except:
                pass
            self.__purgeDead()

        while len(self.team1Friends) > 0 or len(self.team2Friends) > 0:
            # trigger animal onBeforeAttack()
            self.team1Friends[0].onBeforeAttack(self.team1Friends)
            self.team2Friends[0].onBeforeAttack(self.team2Friends)

            # front animals attack
            self.team1Friends[0].attack(self.team1Friends, self.team2Friends)
            self.team2Friends[0].attack(self.team2Friends, self.team1Friends)

            # trigger behind animal onFriendAheadAttack()
            self.team1Friends[1].onFriendAheadAttack(
                self.team1Friends, self.team2Friends
            )
            self.team2Friends[1].onFriendAheadAttack(
                self.team2Friends, self.team1Friends
            )

            # purge dead
            self.__purgeDead()

    ### Private ###

    def __getMoveOrder(self, friends: List[Animal]) -> list:
        team_sob = []

        for i in range(len(friends)):
            if len(team_sob) == 0:
                team_sob.append(i)
            else:
                for j in range(len(team_sob)):
                    if friends[team_sob[j]].getDmg() < friends[i].getDmg():
                        team_sob.insert(j, i)
                        break
                    elif j == len(team_sob) - 1:
                        team_sob.append(i)
        return team_sob

    def __purgeDead(self):
        """private method to purge dead animals"""
        for i in self.team1Friends:
            if not i.getAlive():
                ind = self.team1Friends.index(i)
                i.onFaint(self.team1Friends, self.team2Friends)
                self.team1Friends[ind + 1].onFriendAheadFaint(
                    self.team1Friends, self.team2Friends
                )
                self.team1Friends.remove(i)
        for i in self.team2Friends:
            if not i.getAlive():
                ind = self.team2Friends.index(i)
                i.onFaint(self.team2Friends, self.team1Friends)
                self.team2Friends[ind + 1].onFriendAheadFaint(
                    self.team2Friends, self.team1Friends
                )
                self.team2Friends.remove(i)
