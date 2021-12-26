from src.Animal.Animals import Animal
from src.Shop.Shop import Shop


class Team:
    def __init__(self):
        self.round = 1
        self.shop = Shop()
        self.life = 10
        self.money = 10
        self.friends = [None] * 5

    def moveFriend(self, pos1, pos2) -> None:
        self.friends[pos1], self.friends[pos2] = self.friends[pos2], self.friends[pos1]

    def sellFriend(self, friend_pos: int) -> None:
        if self.friends[friend_pos]:
            self.money += self.friends[friend_pos].getLevel()
            self.friends[friend_pos] = None

    def buyFriend(self, friend: Animal, friend_pos: int) -> int:
        if not self.friends[friend_pos]:
            self.money -= friend.getCost()
            self.friends[friend_pos] = friend
        elif self.friends[friend_pos].__class__ == friend.__class__:
            # TODO: figure out how to combine to keep highest stats
            pass

    def buyFood(self, food, position: int):
        pass

    def nextTurn(self):
        pass

    def setState(self):
        pass

    def getState(self):
        pass

    def __str__(self):
        pass
