from abc import ABC


class Effect(ABC):
    def __init__(self):
        self.test = 0


class NoneEffect(Effect):
    def __init__(self):
        super().__init__()


class BoneEffect(Effect):
    def __init__(self):
        super().__init__()


class SplashEffect(Effect):
    def __init__(self):
        super().__init__()


class SteakEffect(Effect):
    def __init__(self):
        super().__init__()


class PoisonEffect(Effect):
    def __init__(self):
        super().__init__()


class WeakEffect(Effect):
    def __init__(self):
        super().__init__()


class GarlicEffect(Effect):
    def __init__(self):
        super().__init__()


class MelonEffect(Effect):
    def __init__(self):
        super().__init__()


class HoneyEffect(Effect):
    def __init__(self):
        super().__init__()


class ExtraLifeEffect(Effect):
    def __init__(self):
        super().__init__()


class CoconutEffect(Effect):
    def __init__(self):
        super().__init__()
