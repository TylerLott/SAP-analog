from src.Animal import Animal
from src.Animal.Animals import NoneAnimal
from src.Shop import Shop


class Team:
    """
    Team Base Class

    This class is responsible for the team array, money management, game round, and lives
    This class also has it's own instance of a shop
    """

    ### Init ###

    def __init__(self):
        self.round = 1
        self.shop = Shop()
        self.life = 10
        self.alive = True
        self.money = 10
        self.friends = [NoneAnimal()] * 5
        self.wonLast = True

    ### Getters ###

    def getFriendCopy(self) -> list:
        """
        public get a copy of the friends array method

        should only be used in fight
        """
        temp = self.friends.copy()
        return temp

    def getRound(self) -> int:
        return self.round

    def getLife(self) -> int:
        return self.life

    def getMoney(self) -> int:
        return self.money

    def getAlive(self) -> bool:
        return self.alive

    def getMoveOrder(self) -> list:
        """
        public get start of fight move order

        kinda shitty code, probably refactor
        """
        team_sob = []

        for i in range(len(self.friends)):
            if len(team_sob) == 0:
                team_sob.append(i)
            else:
                for j in range(len(team_sob)):
                    if self.friends[team_sob[j]].getDmg() < self.friends[i].getDmg():
                        team_sob.insert(j, i)
                        break
                    elif j == len(team_sob) - 1:
                        team_sob.append(i)
        return team_sob

    ### Setters ###

    def moveFriend(self, pos1, pos2) -> None:
        self.friends[pos1], self.friends[pos2] = self.friends[pos2], self.friends[pos1]

    def sellFriend(self, friend_pos: int) -> None:
        if self.friends[friend_pos]:
            self.add_money(self.friends[friend_pos].getLevel())
            self.friends[friend_pos] = None
            # onSell
            # onFriendSell

    def buyFriend(self, shop_pos: int, friend_pos: int) -> None:
        animal = self.shop.checkAnimal(shop_pos)
        friend = self.friends[friend_pos]
        if self.money >= animal.getCost():
            animal = self.shop.buyAnimal(shop_pos)
            if not friend:
                self.money -= animal.getCost()
                friend = animal
                friend.onBuy()
                # onFriendSummoned
            elif friend.__class__ == animal.__class__:
                # iadd is overridden for animal so this works
                origin_level = friend.getLevel()
                friend += animal
                if friend.getLevel() > origin_level:
                    friend.onLevelUp()

    def buyFood(self, shop_pos: int, position: int) -> None:
        food = self.shop.checkFood(shop_pos)
        if self.money >= food.getCost():
            food = self.shop.buyFood(shop_pos)
            self.money -= food.getCost()
            # iadd override in animal makes this work
            self.friends[position] += food
            # onFoodBought

    def loseLife(self, amt: int) -> None:
        self.life -= amt
        if self.life <= 0:
            self.alive = False

    def add_money(self, amt: int) -> None:
        self.money += amt

    ### For Tests ###

    def forceAddAnimal(self, position: int, animal: Animal):
        self.friends[position] = animal

    ### Private ###

    def __onSell(self) -> None:
        pass

    def __onFriendSold(self) -> None:
        pass

    def __onBuy(self) -> None:
        pass
        # run on onFriendSummoned as well

    def __onStartOfTurn(self) -> None:
        for i in self.friends:
            i.onStartOfTurn(self)

    def __resetTemps(self) -> None:
        for i in self.friends:
            i.setTempDmg(0)
            i.setTempHp(0)

    ### Actions ###

    def rollShop(self) -> None:
        if self.money > 1:
            self.shop.roll()
            self.money -= 1

    def endTurn(self) -> None:
        # onEndOfTurn
        pass

    def nextTurn(self) -> None:

        self.round += 1
        self.shop.setRound(self.round)
        self.money = 10

        self.__resetTemps()
        self.__onStartOfTurn()

    ### State ###

    def setState(self, move: list):
        """
        Converts a move state array to the correct move
        Then completes that move

        moves:
        - buy animal
        - sell animal
        - buy food
        - move animals
        - roll
        - end turn
        """
        pass

    def getState(self):
        """
        Gets Game state

        returns 3 arrays
            - animal team state
            - shop state
            - possible moves
        """
        pass

    ### Overrides ###

    def __str__(self):
        """
        For printing cleanly to console
        - top is the first position
        """
        out_str = "|##############################|\n"
        out_str += "|############ TEAM ############|\n"
        out_str += "|##############################|\n"
        out_str += "|==============================|\n"
        out_str += "|" + f'{"Lives: " + str(self.life):^30}' + "|\n"
        out_str += "|" + f'{"Money: " + str(self.money):^30}' + "|\n"
        out_str += "|==============================|\n"
        out_str += "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n"
        for i in self.friends:
            out_str += i.__str__()
        out_str += "|##############################|\n"

        return out_str

    def __bool__(self):
        return self.alive
