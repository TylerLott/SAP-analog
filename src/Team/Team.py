class Team:
    def __init__(self):
        self.health = 10
        self.friends = [None] * 5

    def moveFriend(self, pos1, pos2) -> None:
        self.friends[pos1], self.friends[pos2] = self.friends[pos2], self.friends[pos1]

    def sellFriend(self, position: int) -> int:
        if self.friends[position]:
            self.friends[position] = None
            return 1
        else:
            return -1

    def addFriend(self, friend, position: int) -> int:
        if not self.friends[position]:
            self.friends[position] = friend
            return 1
        else:
            return -1

    def addFood(self, food, position: int):
        pass

    def combineFriend(self, position):
        pass
