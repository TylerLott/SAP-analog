from abc import ABC
from src.Food.Effect import Effect
from src.Food.Effect.Effects import NoneEffect


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
        """Constructor method"""
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
        out_str = "|==============================|\n"
        out_str += "|" + f"{self.__class__.__name__:^30}" + "|\n"
        out_str += "|------------------------------|\n"
        out_str += "|" + f'{"Tmp Health: " + str(self.temp_buff[0]):^30}' + "|\n"
        out_str += "|" + f'{"Tmp Damage: "+ str(self.temp_buff[1]):^30}' + "|\n"
        out_str += "|" + f'{"Perm Health: " + str(self.perm_buff[0]):^30}' + "|\n"
        out_str += "|" + f'{"Perm Damage: "+ str(self.perm_buff[1]):^30}' + "|\n"
        out_str += "|" + f'{"Effect: "+ self.getEffect().__name__:^30}' + "|\n"
        out_str += "|" + f'{"Cost: "+ str(self.cost):^30}' + "|\n"
        out_str += "|==============================|\n"

        return out_str
