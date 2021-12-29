from src.Team.Team import Team


class Fight:
    def __init__(self, team1: Team, team2: Team):
        pass
        # turn order is based on damage

    def simulate(self):
        # Copy teams into new arrays

        """
        onStartOfBattle in order of dmg

        while loop
            onStartOfTurn
            onBeforeAttack for front animals
            attack - using getDmg and subHp
            onFaint
                if faint pop that animal out of arr
                if summons add animal in the dead one's place
                    call onSummoned for all others
            onHurt
            onFriendAheadFaint
            onFrinedAheadAttack if not faint
        """
        pass
