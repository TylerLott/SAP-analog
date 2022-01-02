from math import perm
from src.Food import Food


class NoneFood(Food):
    def __init__(self):
        super().__init__()

    def __bool__(self):
        return False


class Apple(Food):
    def __init__(self):
        super().__init__(perm_hp=1, perm_dmg=1)


class Honey(Food):
    def __init__(self):
        super().__init__(effect="honey")


class Cupcake(Food):
    def __init__(self):
        super().__init__(temp_hp=3, temp_dmg=3)


class MeatBone(Food):
    def __init__(self):
        super().__init__(effect="meat")


class Pill(Food):
    def __init__(self):
        super().__init__(cost=1, effect="pill")


class Garlic(Food):
    def __init__(self):
        super().__init__(effect="garlic")


class Salad(Food):
    def __init__(self):
        super().__init__(effect="random", perm_hp=1, perm_dmg=1)
        self.num_animals = 2


class CannedFood(Food):
    def __init__(self):
        super().__init__(effect="buffShop", perm_hp=1, perm_dmg=2)


class Pear(Food):
    def __init__(self):
        super().__init__(perm_hp=2, perm_dmg=2)


class Chili(Food):
    def __init__(self):
        super().__init__(effect="splash")


class Chocolate(Food):
    def __init__(self):
        super().__init__(effect="exp")


class Sushi(Food):
    def __init__(self):
        super().__init__(effect="random", perm_hp=1, perm_dmg=1)
        self.num_animals = 3


class Melon(Food):
    def __init__(self):
        super().__init__(effect="melon")


class Mushroom(Food):
    def __init__(self):
        super().__init__(effect="extraLife")


class Pizza(Food):
    def __init__(self):
        super().__init__(effect="random", perm_hp=2, perm_dmg=2)
        self.num_animals = 2


class Steak(Food):
    def __init__(self):
        super().__init__(effect="steak")


class Milk(Food):
    def __init__(self, level: int):
        super().__init__(perm_hp=2 * level, perm_dmg=1 * level)
