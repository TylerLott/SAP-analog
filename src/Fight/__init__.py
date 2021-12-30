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

        # get start of fight move order for each team
        sob1, sob2 = self.__getStartOfBattle()

        pass

    ### Private ###

    def __getStartOfBattle(self) -> list:
        """
        private get start of battle method

        returns two arrays containing the array positions of start of battle moves

        this is shitty code and should be refactored
        """
        team1_sob = []

        for i in range(len(self.team1Friends)):
            if len(team1_sob) == 0:
                team1_sob.append(i)
            else:
                for j in team1_sob:
                    if (
                        self.team1Friends[team1_sob[j]].getDmg()
                        < self.team1Friends[i].getDmg()
                    ):
                        team1_sob.insert(j, i)
                        break
                team1_sob.append(i)

        team2_sob = []

        for i in range(len(self.team2Friends)):
            if len(team2_sob) == 0:
                team2_sob.append(i)
            else:
                for j in team2_sob:
                    if (
                        self.team2Friends[team2_sob[j]].getDmg()
                        < self.team2Friends[i].getDmg()
                    ):
                        team2_sob.insert(j, i)
                        break
                team2_sob.append(i)

        return team1_sob, team2_sob
