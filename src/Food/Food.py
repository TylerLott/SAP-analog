from abc import ABC
from src.Food.Effect.Effect import *


class Food(ABC):
    """
    Food Base Class
    """

    ### Init ###

    def __init__(
        self,
        temp_hp: int = 0,
        temp_dmg: int = 0,
        perm_hp: int = 0,
        perm_dmg: int = 0,
        effect: Effect = NoneEffect,
        cost: int = 3,
    ):
        self.temp_buff = [temp_hp, temp_dmg]
        self.perm_buff = [perm_hp, perm_dmg]
        self.effect = effect
        self.cost = cost
        pass

    ### Getters ###

    def getCost(self) -> int:
        return self.cost

    def getEffect(self) -> Effect:
        return self.effect

    def getTempBuff(self) -> list:
        # [temp_hp, temp_dmg]
        return self.temp_buff

    def getPermBuff(self) -> list:
        # [perm_hp, perm_dmg]
        return self.perm_buff

    ### Setters ###

    ### Overrides ###

    def __str__(self):
        out_str = "|=============================|\n"
        out_str += "|" + f"{self.__class__.__name__:^30}" + "|\n"
        out_str += "|-----------------------------|\n"
        out_str += "|" + f'{"Tmp Health: " + self.temp_buff[0]:^30}' + "|\n"
        out_str += "|" + f'{"Tmp Damage: "+ self.temp_buff[1]:^30}' + "|\n"
        out_str += "|" + f'{"Perm Health: " + self.perm_buff[0]:^30}' + "|\n"
        out_str += "|" + f'{"Perm Damage: "+ self.perm_buff[1]:^30}' + "|\n"
        out_str += "|" + f'{"Effect: "+ self.effect.__class__.__name__:^30}' + "|\n"
        out_str += "|" + f'{"Cost: "+ self.cost:^30}' + "|\n"
        out_str += "|=============================|\n"

        return out_str


class Apple(Food):
    def __init__(self):
        pass


class Honey(Food):
    def __init__(self):
        pass


class Cupcake(Food):
    def __init__(self):
        pass


class MeatBone(Food):
    def __init__(self):
        pass


class Pill(Food):
    def __init__(self):
        super().__init__(cost=1)


class Garlic(Food):
    def __init__(self):
        pass


class Salad(Food):
    def __init__(self):
        pass


class CannedFood(Food):
    def __init__(self):
        pass


class Pear(Food):
    def __init__(self):
        pass


class Chili(Food):
    def __init__(self):
        pass


class Chocolate(Food):
    def __init__(self):
        pass


class Sushi(Food):
    def __init__(self):
        pass


class Melon(Food):
    def __init__(self):
        pass


class Mushroom(Food):
    def __init__(self):
        pass


class Pizza(Food):
    def __init__(self):
        pass


class Steak(Food):
    def __init__(self):
        pass


class Milk(Food):
    def __init__(self):
        pass
