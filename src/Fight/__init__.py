from typing import List

from src.Animal import Animal
from src.Team import Team


class Fight:
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

        # Remove all of the NoneAnimals()
        for i in self.team1Friends:
            if i.__class__.__name__ == "NoneAnimal":
                self.team1Friends.remove(i)
        for i in self.team2Friends:
            if i.__class__.__name__ == "NoneAnimal":
                self.team2Friends.remove(i)

        # get start of fight move order for each team
        sob1 = self.team1.getMoveOrder()
        sob2 = self.team2.getMoveOrder()

        for i in range(5):
            self.team1Friends[sob1[i]].onStartOfBattle(
                self.team1Friends, self.team2Friends
            )
            self.team2Friends[sob2[i]].onStartOfBattle(
                self.team2Friends, self.team1Friends
            )
            self.__purgeDead()

        while len(self.team1Friends) > 0 or len(self.team2Friends) > 0:
            pass
            # trigger animal onBeforeAttack()
            # front animals attack
            # if not faint           -> trigger animals onHurt()
            # if faint               -> trigger animal onFaint()
            #   if summon on faint   -> trigger all animals onFriendSummoned()
            #   if summon on faint, only fill up to 5 animal length
            # if front animal faints -> trigger behind animal onFriendAheadFaint()
            # if not                 -> trigger behind animal onFriendAheadAttack()

    ### Private ###

    def __purgeDead(self):
        """private method to purge dead animals"""
        for i in self.team1Friends:
            if not i.getAlive():
                self.team1Friends.remove(i)
        for i in self.team2Friends:
            if not i.getAlive():
                self.team2Friends.remove(i)
