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
        self.effect = "honey"


class Cupcake(Food):
    def __init__(self):
        super().__init__()
        self.temp_hp = 3
        self.temp_dmg = 3


class MeatBone(Food):
    def __init__(self):
        super().__init__()
        self.effect = "meat"


class Pill(Food):
    def __init__(self):
        super().__init__(cost=1)
        self.effect = "kill"


class Garlic(Food):
    def __init__(self):
        super().__init__()
        self.effect = "garlic"


class Salad(Food):
    def __init__(self):
        super().__init__()


class CannedFood(Food):
    def __init__(self):
        super().__init__()
        self.effect = "buffShop"
        self.perm_hp = 1
        self.perm_dmg = 2


class Pear(Food):
    def __init__(self):
        super().__init__()
        self.perm_hp = 2
        self.perm_dmg = 2


class Chili(Food):
    def __init__(self):
        super().__init__()
        self.effect = "splash"


class Chocolate(Food):
    def __init__(self):
        super().__init__()
        self.effect = "exp"


class Sushi(Food):
    def __init__(self):
        super().__init__()
        self.effect = "random"
        self.num_animals = 3
        self.perm_hp = 1
        self.perm_dmg = 1


class Melon(Food):
    def __init__(self):
        super().__init__()
        self.effect = "melon"


class Mushroom(Food):
    def __init__(self):
        super().__init__()
        self.effect = "extraLife"


class Pizza(Food):
    def __init__(self):
        super().__init__()
        self.effect = "random"
        self.num_animals = 2
        self.perm_hp = 2
        self.perm_dmg = 2


class Steak(Food):
    def __init__(self):
        super().__init__()
        self.effect = "steak"


class Milk(Food):
    def __init__(self, level: int):
        self.hp = 2 * level
        self.dmg = 1 * level
        super().__init__()
