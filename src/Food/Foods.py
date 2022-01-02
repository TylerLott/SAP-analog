from src.Effect.Effects import *
from src.Food import Food


class NoneFood(Food):
    def __init__(self):
        super().__init__()

    def __bool__(self):
        return False


class Apple(Food):
    def __init__(self):
        super().__init__()
        self.perm_hp = 1
        self.perm_dmg = 1


class Honey(Food):
    def __init__(self):
        super().__init__()
        self.effect = HoneyEffect()


class Cupcake(Food):
    def __init__(self):
        super().__init__()
        self.temp_hp = 3
        self.temp_dmg = 3


class MeatBone(Food):
    def __init__(self):
        super().__init__()
        self.effect = BoneEffect()


class Pill(Food):
    def __init__(self):
        super().__init__(cost=1)


class Garlic(Food):
    def __init__(self):
        super().__init__()
        self.effect = GarlicEffect()


class Salad(Food):
    def __init__(self):
        super().__init__()


class CannedFood(Food):
    def __init__(self):
        super().__init__()


class Pear(Food):
    def __init__(self):
        super().__init__()


class Chili(Food):
    def __init__(self):
        super().__init__()
        self.effect = SplashEffect()


class Chocolate(Food):
    def __init__(self):
        super().__init__()


class Sushi(Food):
    def __init__(self):
        super().__init__()


class Melon(Food):
    def __init__(self):
        super().__init__()
        self.effect = MelonEffect()


class Mushroom(Food):
    def __init__(self):
        super().__init__()
        self.effect = ExtraLifeEffect()


class Pizza(Food):
    def __init__(self):
        super().__init__()


class Steak(Food):
    def __init__(self):
        super().__init__()
        self.effect = SteakEffect()


class Milk(Food):
    def __init__(self, level: int):
        self.hp = 2 * level
        self.dmg = 1 * level
        super().__init__()
