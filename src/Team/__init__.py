from random import choices
from typing import List
from copy import deepcopy
import numpy as np

from src.Animal import Animal
from src.Animal.Animals import NoneAnimal
from src.Shop import Shop
from src.State import getPossibleMovesState


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
        self.moves = 0

    ### Getters ###

    def getFriendCopy(self) -> List[Animal]:
        """
        public get a copy of the friends array method

        should only be used in fight
        """
        temp = list([deepcopy(i) for i in self.friends])
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

    def getMovesNum(self):
        return self.moves

    ### Setters ###

    def moveFriend(self, pos1, pos2) -> None:
        if (
            self.friends[pos1].__class__ == self.friends[pos2].__class__
            and self.friends[pos1].getLevel() < 3
            and self.friends[pos2].getLevel() < 3
        ):
            self.friends[pos2] += self.friends[pos1]
        else:
            self.friends[pos1], self.friends[pos2] = (
                self.friends[pos2],
                self.friends[pos1],
            )

    def sellFriend(self, friend_pos: int) -> None:
        if self.friends[friend_pos]:
            self.add_money(self.friends[friend_pos].getLevel())
            self.friends[friend_pos].onSell(self.friends, self)
            self.friends[friend_pos] = NoneAnimal()
            for i in range(len(self.friends)):
                if i != friend_pos and self.friends[i]:
                    self.friends[i].onFriendSold(self.friends)

    def buyFriend(self, shop_pos: int, friend_pos: int) -> None:
        if (
            len(self.shop.animals) > shop_pos
            and self.shop.animals[shop_pos]
            and (
                self.friends[friend_pos].__class__
                == self.shop.animals[shop_pos].__class__
                or not self.friends[friend_pos]
            )
        ):

            # to protect against combining animals more than level 3
            if self.friends[friend_pos].getExp() == 6:
                return
            animal = self.shop.checkAnimal(shop_pos)
            if self.money >= animal.getCost():
                animal = self.shop.buyAnimal(shop_pos)
                if not self.friends[friend_pos]:
                    self.money -= animal.getCost()
                    self.friends[friend_pos] = animal
                    self.friends[friend_pos].onBuy(self.friends, self)
                    for i in self.friends:
                        if i != self.friends[friend_pos]:
                            i.onFriendSummoned(self.friends, self.friends[friend_pos])
                            i.onFriendBought(self.friends, self.friends[friend_pos])
                elif self.friends[friend_pos].__class__ == animal.__class__:
                    # iadd is overridden for animal so this works
                    origin_level = self.friends[friend_pos].getLevel()
                    self.friends[friend_pos] += animal
                    self.friends[friend_pos].onBuy(self.friends, self)
                    if self.friends[friend_pos].getLevel() > origin_level:
                        self.friends[friend_pos].onLevelUp(self.friends)

    def buyFood(self, shop_pos: int, position: int) -> None:
        if (
            len(self.shop.items) > shop_pos
            and self.friends[position]
            and self.shop.items[shop_pos]
        ):
            food = self.shop.checkFood(shop_pos)

            if self.money >= food.getCost():

                food = self.shop.buyFood(shop_pos)

                haveCat = 1
                for i in self.friends:
                    if i.__class__.__name__ == "Cat":
                        haveCat += i.getLevel()
                food.perm_buff[0] *= haveCat
                food.perm_buff[1] *= haveCat
                food.temp_buff[0] *= haveCat
                food.temp_buff[1] *= haveCat

                if food.effect == "pill":
                    self.friends[position].onFaint(self.friends, [])
                    for i in self.friends:
                        if i != self.friends[position]:
                            i.onFriendFaint(self.friends[position], self.friends)
                    if len(self.friends) > position + 1:
                        self.friends[position + 1].onFriendAheadFaint(self.friends, [])
                    self.friends[position] = NoneAnimal()

                elif food.effect == "random":
                    food.effect = None
                    friends = []
                    for i in self.friends:
                        if i:
                            friends.append(i)
                    if len(friends) > food.num_animals:
                        friends = choices(friends, k=food.num_animals)
                    for i in friends:
                        food.effect = i.effect
                        i += food
                        i.onEat(self.friends)
                elif food.effect == "buffShop":
                    self.shop.health_modifier += 1
                    self.shop.dmg_modifier += 1
                    for i in self.shop.animals:
                        if i:
                            i.setBaseHp(i.getBaseHp() + 1)
                            i.setBaseDmg(i.getBaseDmg() + 1)
                else:
                    self.money -= food.getCost()
                    origin_level = self.friends[position].getLevel()
                    # iadd override in animal makes this work
                    self.friends[position] += food
                    self.friends[position].onEat(self.friends)
                    if self.friends[position].getLevel() > origin_level:
                        self.friends[position].onLevelUp(self.friends)
                    for i in range(len(self.friends)):
                        if self.friends[i] and i != position:
                            self.friends[i].onFriendEat(self.friends[position])

    def loseLife(self) -> None:
        if self.round <= 3:
            amt = 1
        elif self.round <= 5:
            amt = 2
        else:
            amt = 3
        self.life -= amt
        if self.life <= 0:
            self.alive = False

    def add_money(self, amt: int) -> None:
        self.money += amt

    ### Private ###

    def __onFriendSold(self) -> None:
        # TODO call onfriendsold for all other animals
        pass

    def __onBuy(self) -> None:
        pass
        # TODO run on onFriendSummoned as well

    def __onStartOfTurn(self) -> None:
        for i in self.friends:
            i.onStartOfTurn(self)

    def __resetTemps(self) -> None:
        for i in self.friends:
            i.setTempDmg(0)
            i.setTempHp(0)

    ### Actions ###

    def rollShop(self) -> None:
        if self.money > 0:
            self.shop.roll()
            self.money -= 1

    def endTurn(self) -> None:
        for i in self.friends:
            i.onEndOfTurn(self.friends)

    def nextTurn(self) -> None:
        self.moves = 0
        self.round += 1
        self.shop.setRound(self.round)
        self.money = 10

        self.__resetTemps()
        self.__onStartOfTurn()

    ### State ###

    def setState(self, move: int):
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
        s = ""
        if move == 0:
            s = "roll"
            self.rollShop()

        elif move == 1:
            s = "move 0 => 1"
            self.moveFriend(0, 1)
        elif move == 2:
            s = "move 0 => 2"
            self.moveFriend(0, 2)
        elif move == 3:
            s = "move 0 => 3"
            self.moveFriend(0, 3)
        elif move == 4:
            s = "move 0 => 4"
            self.moveFriend(0, 4)
        elif move == 5:
            s = "move 1 => 0"
            self.moveFriend(1, 0)
        elif move == 6:
            s = "move 1 => 2"
            self.moveFriend(1, 2)
        elif move == 7:
            s = "move 1 => 3"
            self.moveFriend(1, 3)
        elif move == 8:
            s = "move 1 => 4"
            self.moveFriend(1, 4)
        elif move == 9:
            s = "move 2 => 0"
            self.moveFriend(2, 0)
        elif move == 10:
            s = "move 2 => 1"
            self.moveFriend(2, 1)
        elif move == 11:
            s = "move 2 => 3"
            self.moveFriend(2, 3)
        elif move == 12:
            s = "move 2 => 4"
            self.moveFriend(2, 4)
        elif move == 13:
            s = "move 3 => 0"
            self.moveFriend(3, 0)
        elif move == 14:
            s = "move 3 => 1"
            self.moveFriend(3, 1)
        elif move == 15:
            s = "move 3 => 2"
            self.moveFriend(3, 2)
        elif move == 16:
            s = "move 3 => 4"
            self.moveFriend(3, 4)
        elif move == 17:
            s = "move 4 => 1"
            self.moveFriend(4, 0)
        elif move == 18:
            s = "move 4 => 1"
            self.moveFriend(4, 1)
        elif move == 19:
            s = "move 4 => 2"
            self.moveFriend(4, 2)
        elif move == 20:
            s = "move 4 => 3"
            self.moveFriend(4, 3)
        elif move == 21:
            s = "sell 0"
            self.sellFriend(0)
        elif move == 22:
            s = "sell 1"
            self.sellFriend(1)
        elif move == 23:
            s = "sell 2"
            self.sellFriend(2)
        elif move == 24:
            s = "sell 3"
            self.sellFriend(3)
        elif move == 25:
            s = "sell 4"
            self.sellFriend(4)
        elif move == 26:
            s = "buy 0 => 0"
            self.buyFriend(0, 0)
        elif move == 27:
            s = "buy 0 => 1"
            self.buyFriend(0, 1)
        elif move == 28:
            s = "buy 0 => 2"
            self.buyFriend(0, 2)
        elif move == 29:
            s = "buy 0 => 3"
            self.buyFriend(0, 3)
        elif move == 30:
            s = "buy 0 => 4"
            self.buyFriend(0, 4)
        elif move == 31:
            s = "buy 1 => 0"
            self.buyFriend(1, 0)
        elif move == 32:
            s = "buy 1 => 1"
            self.buyFriend(1, 1)
        elif move == 33:
            s = "buy 1 => 2"
            self.buyFriend(1, 2)
        elif move == 34:
            s = "buy 1 => 3"
            self.buyFriend(1, 3)
        elif move == 35:
            s = "buy 1 => 4"
            self.buyFriend(1, 4)
        elif move == 36:
            s = "buy 2 => 0"
            self.buyFriend(2, 0)
        elif move == 37:
            s = "buy 2 => 1"
            self.buyFriend(2, 1)
        elif move == 38:
            s = "buy 2 => 2"
            self.buyFriend(2, 2)
        elif move == 39:
            s = "buy 2 => 3"
            self.buyFriend(2, 3)
        elif move == 40:
            s = "buy 2 => 4"
            self.buyFriend(2, 4)
        elif move == 41:
            s = "buy 3 => 0"
            self.buyFriend(3, 0)
        elif move == 42:
            s = "buy 3 => 1"
            self.buyFriend(3, 1)
        elif move == 43:
            s = "buy 3 => 2"
            self.buyFriend(3, 2)
        elif move == 44:
            s = "buy 3 => 3"
            self.buyFriend(3, 3)
        elif move == 45:
            s = "buy 3 => 4"
            self.buyFriend(3, 4)
        elif move == 46:
            s = "buy 4 => 0"
            self.buyFriend(4, 0)
        elif move == 47:
            s = "buy 4 => 1"
            self.buyFriend(4, 1)
        elif move == 48:
            s = "buy 4 => 2"
            self.buyFriend(4, 2)
        elif move == 49:
            s = "buy 4 => 3"
            self.buyFriend(4, 3)
        elif move == 50:
            s = "buy 4 => 4"
            self.buyFriend(4, 4)
        elif move == 51:
            s = "buy food 0 => 0"
            self.buyFood(0, 0)
        elif move == 52:
            s = "buy food 0 => 1"
            self.buyFood(0, 1)
        elif move == 53:
            s = "buy food 0 => 2"
            self.buyFood(0, 2)
        elif move == 54:
            s = "buy food 0 => 3"
            self.buyFood(0, 3)
        elif move == 55:
            s = "buy food 0 => 4"
            self.buyFood(0, 4)
        elif move == 56:
            s = "buy food 1 => 0"
            self.buyFood(1, 0)
        elif move == 57:
            s = "buy food 1 => 1"
            self.buyFood(1, 1)
        elif move == 58:
            s = "buy food 1 => 2"
            self.buyFood(1, 2)
        elif move == 59:
            s = "buy food 1 => 3"
            self.buyFood(1, 3)
        elif move == 60:
            s = "buy food 1 => 4"
            self.buyFood(1, 4)
        elif move == 61:
            s = "freeze 0"
            self.shop.freezeAnimal(0)
        elif move == 62:
            s = "freeze 1"
            self.shop.freezeAnimal(1)
        elif move == 63:
            s = "freeze 2"
            self.shop.freezeAnimal(2)
        elif move == 64:
            s = "freeze 3"
            self.shop.freezeAnimal(3)
        elif move == 65:
            s = "freeze 4"
            self.shop.freezeAnimal(4)
        elif move == 66:
            s = "freeze food 0"
            self.shop.freezeItem(0)
        elif move == 67:
            s = "freeze food 1"
            self.shop.freezeItem(1)
        elif move == 68:
            s = "end turn"
            self.endTurn()

        self.moves += 1

        return s

    def getState(self):
        """
        Gets Game state

        returns 3 arrays
            - animal team state
            - shop state
            - possible moves
        """
        # Friend State
        friend_state = [i.getState() for i in self.friends]
        friend_state = np.stack(friend_state, axis=0)

        # Shop State
        shop_an, shop_food, shop_freeze = self.shop.getState()

        # Team State
        won_last = 1 if self.wonLast else 0
        # Normalize money by 20
        money = self.getMoney() if self.getMoney() <= 20 else 20

        team_state = np.array(
            [
                money / 20,
                self.getLife() / 10,
                self.getRound() / 20,
                won_last,
                self.moves / 15,
            ]
        )

        possible_moves = np.concatenate(getPossibleMovesState(self))
        friend_state = friend_state.flatten()
        shop_an = shop_an.flatten()
        shop_food = shop_food.flatten()
        shop_freeze = shop_freeze.flatten()
        team_state = team_state.flatten()
        state = np.concatenate(
            (friend_state, shop_an, shop_food, shop_freeze, team_state)
        )

        return state, possible_moves

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

    ### For Tests ###

    def forceAddAnimal(self, position: int, animal: Animal):
        self.friends[position] = animal
