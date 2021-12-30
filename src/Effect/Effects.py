from src.Effect import Effect


class NoneEffect(Effect):
    def __init__(self):
        super().__init__()

    def __bool__(self):
        return False


class BoneEffect(Effect):
    """
    Bone effect

    Do 5 additional damage
    """

    def __init__(self):
        super().__init__()


class SplashEffect(Effect):
    """
    Splash effect

    Damage enemies two deep
    """

    def __init__(self):
        super().__init__()


class SteakEffect(Effect):
    """
    Steak effect

    Do 20 more damage for one attack
    """

    def __init__(self):
        super().__init__()


class PoisonEffect(Effect):
    """
    Scorpion poison effect

    Kill any enemy, unless has melon/coconut armor
    """

    def __init__(self):
        super().__init__()


class WeakEffect(Effect):
    """
    Weak effect

    Take 3 additional damage
    """

    def __init__(self):
        super().__init__()


class GarlicEffect(Effect):
    """
    Garlic effect

    Take 2 less damage (can't reduce less than 1)
    """

    def __init__(self):
        super().__init__()


class MelonEffect(Effect):
    """
    Melon effect

    Take 20 less damage one time
    """

    def __init__(self):
        super().__init__()


class HoneyEffect(Effect):
    """
    Honey effect

    Spawn a 1/1 bee on faint
    """

    def __init__(self):
        super().__init__()


class ExtraLifeEffect(Effect):
    """
    Extra life effect

    Spawn a 1/1 version of same animal on faint
    """

    def __init__(self):
        super().__init__()


class CoconutEffect(Effect):
    """
    Coconut effect

    Block one attack, of any amount of damage
    """

    def __init__(self):
        super().__init__()
