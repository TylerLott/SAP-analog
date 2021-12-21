class Action:
    def __init__(self, action_type, heal_amt, dmg_amt, team_position, enemy_position):
        """
        action type:      heal, attack, giveEffect
        heal_amount:      heal amount (affects the health stat [- bad, + good])
        dmg_amount:       amount of damage given (affects the damage stat [- bad, + good])
        team position:    what position of friendly team is affected (-1 = all, -2 = None)
        enemy position:   what position of enemy team is affected (-1 = all, -2 = None)
        """
        self.action_type = action_type
        self.heal_amt = heal_amt
        self.dmg_amt = dmg_amt
        self.team_pos = team_position
        self.enemy_pos = enemy_position
