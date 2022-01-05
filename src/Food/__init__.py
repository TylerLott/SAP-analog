from abc import ABC

from src.State import getFoodState


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
        effect: str = None,
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

    def getEffect(self) -> str:
        return self.effect

    def getTempBuff(self) -> list:
        # [temp_hp, temp_dmg]
        return self.temp_buff

    def getPermBuff(self) -> list:
        # [perm_hp, perm_dmg]
        return self.perm_buff

    def getState(self):
        return getFoodState(self)

    ### Setters ###

    def setCost(self, amt: int) -> None:
        self.cost = amt

    ### Overrides ###

    def __str__(self):
        out_str = "|==============================|\n"
        out_str += "|" + f"{self.__class__.__name__:^30}" + "|\n"
        out_str += "|------------------------------|\n"
        out_str += "|" + f'{"Tmp Health: " + str(self.temp_buff[0]):^30}' + "|\n"
        out_str += "|" + f'{"Tmp Damage: "+ str(self.temp_buff[1]):^30}' + "|\n"
        out_str += "|" + f'{"Perm Health: " + str(self.perm_buff[0]):^30}' + "|\n"
        out_str += "|" + f'{"Perm Damage: "+ str(self.perm_buff[1]):^30}' + "|\n"
        out_str += "|" + f'{"Effect: "+ str(self.effect):^30}' + "|\n"
        out_str += "|" + f'{"Cost: "+ str(self.cost):^30}' + "|\n"
        out_str += "|==============================|\n"

        return out_str

    def __bool__(self):
        return True
