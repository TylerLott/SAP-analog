from src.Animal.Animals import Animal
from src.Shop.Shop import Shop
from src.Food.Food import Food


class Team:
    """
    This is the class for the Teams
    """

    ### Init ###

    def __init__(self):
        self.round = 1
        self.shop = Shop()
        self.life = 10
        self.money = 10
        self.friends = [None] * 5

    ### Getters ###

    def getFriendCopy(self) -> list:
        temp = self.friends.copy()
        return temp

    def getRound(self) -> int:
        return self.round

    def getLife(self) -> int:
        return self.life

    def getMoney(self) -> int:
        return self.money

    ### Setters ###

    def moveFriend(self, pos1, pos2) -> None:
        self.friends[pos1], self.friends[pos2] = self.friends[pos2], self.friends[pos1]

    def sellFriend(self, friend_pos: int) -> None:
        if self.friends[friend_pos]:
            self.money += self.friends[friend_pos].getLevel()
            self.friends[friend_pos] = None
            # onSell
            # onFriendSell

    def buyFriend(self, shop_pos: int, friend_pos: int) -> None:
        animal = self.shop.checkAnimal(shop_pos)
        if self.money >= animal.getCost():
            if not self.friends[friend_pos]:
                self.money -= animal.getCost()
                self.friends[friend_pos] = self.shop.buyAnimal(shop_pos)
                # onBuy
                # onFriendSummoned
            elif self.friends[friend_pos].__class__ == animal.__class__:
                # TODO: figure out how to combine to keep highest stats
                pass

    def buyFood(self, food: Food, position: int) -> None:
        # onFoodBought
        if self.money >= food.getCost():
            self.money -= food.getCost()
            self.friends[position].setFood(food)
            # onEat

    ### Actions ###

    def endTurn(self) -> None:
        # onEndOfTurn
        pass

    def nextTurn(self) -> None:
        # remove all temp hp
        self.round += 1
        self.shop.nextRound()
        self.money = 10
        # onStartOfTurn - for stuff like the swan

    ### State ###

    def setState(self):
        # convert state to the right move and do that move
        pass

    def getState(self):
        # get animals state, shop state, and possible moves state
        pass

    ### Overrides ###

    def __str__(self):
        pass
        # title
        # friends
        # stats
        # effects
