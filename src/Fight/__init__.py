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

    def simulate(self) -> list:
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

        # Remove all of the NoneAnimals()
        self.team1Friends = self.__purgeNoneAnimals(self.team1Friends)
        self.team2Friends = self.__purgeNoneAnimals(self.team2Friends)

        # get start of fight move order for each team
        sob1 = self.__getMoveOrder(self.team1Friends)
        sob2 = self.__getMoveOrder(self.team2Friends)

        for i in range(5):
            # TODO refactor this shithole code
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

        while len(self.team1Friends) > 0 and len(self.team2Friends) > 0:

            # trigger animal onBeforeAttack()
            self.team1Friends[0].onBeforeAttack(self.team1Friends, self.team2Friends)
            self.team2Friends[0].onBeforeAttack(self.team2Friends, self.team1Friends)

            # front animals attack
            self.team1Friends[0].attack(self.team1Friends, self.team2Friends)
            self.team2Friends[0].attack(self.team2Friends, self.team1Friends)

            # trigger behind animal onFriendAheadAttack()
            if len(self.team1Friends) > 1:
                self.team1Friends[1].onFriendAheadAttack(
                    self.team1Friends, self.team2Friends
                )
            if len(self.team2Friends) > 1:
                self.team2Friends[1].onFriendAheadAttack(
                    self.team2Friends, self.team1Friends
                )

            # purge dead
            self.__purgeDead()

            # Remove all of the NoneAnimals()
            self.team1Friends = self.__purgeNoneAnimals(self.team1Friends)
            self.team2Friends = self.__purgeNoneAnimals(self.team2Friends)

        if len(self.team1Friends) > len(self.team2Friends):
            self.team2.loseLife()
            self.team2.wonLast = False
            self.team1.wonLast = True
        elif len(self.team2Friends) > len(self.team1Friends):
            self.team1.loseLife()
            self.team1.wonLast = False
            self.team2.wonLast = True

        t = []
        for i in self.team1.friends:
            if i:
                t.append(i)
        t2 = []
        for i in self.team2.friends:
            if i:
                t2.append(i)

        if len(self.team1Friends) == len(self.team2Friends):

            if len(t) >= len(t2) and len(t2) < 2 and len(t) > 2:
                self.team2.life = 0
                self.team2.alive = False
            elif len(t2) > len(t) and len(t) < 2 and len(t2) > 2:
                self.team1.life = 0
                self.team1.alive = False

        if len(t) < 2 and len(t2) < 2:
            self.team1.life = 0
            self.team1.alive = False
            self.team2.life = 0
            self.team2.alive = False

        return 1 if len(self.team1Friends) > len(self.team2Friends) else 0

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
                if len(self.team1Friends) > 1 + ind and self.team1Friends[ind + 1]:
                    self.team1Friends[ind + 1].onFriendAheadFaint(
                        self.team1Friends, self.team2Friends
                    )
                for j in self.team1Friends:
                    j.onFriendFaint(i, self.team2Friends)
                if i in self.team1Friends:
                    self.team1Friends.remove(i)
        for i in self.team2Friends:
            if not i.getAlive():
                ind = self.team2Friends.index(i)
                i.onFaint(self.team2Friends, self.team1Friends)
                if len(self.team2Friends) > 1 + ind and self.team2Friends[ind + 1]:
                    self.team2Friends[ind + 1].onFriendAheadFaint(
                        self.team2Friends, self.team1Friends
                    )
                for j in self.team2Friends:
                    j.onFriendFaint(i, self.team2Friends)
                if i in self.team2Friends:
                    self.team2Friends.remove(i)

    def __purgeNoneAnimals(self, friends: List[Animal]) -> List[Animal]:
        newTeam = []
        for i in friends:
            if i:
                newTeam.append(i)
        return newTeam
