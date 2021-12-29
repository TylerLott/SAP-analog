from src.Team.Team import Team


class Fight:
    def __init__(self, team1: Team, team2: Team):
        self.team1 = team1
        self.team2 = team2
        self.team1Friends = team1.friends.copy()
        self.team2Friends = team2.friends.copy()
        # Copy teams into new arrays
        # turn order is based on damage

    def simulate(self) -> None:

        # subtract hp from losing team

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
        pass
