from src.Animal.Animals import Animal
from src.Shop.Shop import Shop
from src.Food.Food import Food


class Team:
    """
    This is the class for the Teams
    """

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
        if self.money >= friend.getCost():
            if not self.friends[friend_pos]:
                self.money -= friend.getCost()
                self.friends[friend_pos] = friend
            elif self.friends[friend_pos].__class__ == friend.__class__:
                # TODO: figure out how to combine to keep highest stats
                pass

    def buyFood(self, food: Food, position: int):
        if self.money >= food.getCost():
            self.money -= food.getCost()
            self.friends[position].setFood(food)

    def nextTurn(self):
        self.round += 1
        self.shop.nextRound()
        self.money = 10

    def setState(self):
        # convert state to the right move and do that move
        pass

    def getState(self):
        # get animals state, shop state, and possible moves state
        pass

    def __str__(self):
        pass
