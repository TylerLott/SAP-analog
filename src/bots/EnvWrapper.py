import gym
from gym import spaces
import numpy as np

from src.Team import Team
from src.Fight import Fight
from src.bots.Gauntlet import getGauntlet


class EnvWrapper(gym.Env):
    def __init__(self) -> None:
        super(EnvWrapper, self).__init__()
        self.team1 = Team()
        self.won_rounds = 0
        state = self.team1.getState()
        self.action_space = spaces.Discrete(len(state[1]))
        self.observation_space = spaces.Box(
            low=0, high=1, shape=(len(state[0]),), dtype=np.float32
        )

    def step(self, move):

        reward = 0
        done = False
        round = self.team1.round

        # penalize for bad moves
        _, p = self.team1.getState()
        amt = 1
        if p[move] == 0 and move != 68 and self.team1.moves > 10:
            amt = amt * (self.team1.moves - 10)
            reward -= amt
        elif p[move] == 0:
            reward -= 5
        # elif p[move] == 1:
        #     reward += 1

        og = 0
        for i in self.team1.friends:
            if i:
                og += 1

        # Do move
        move_print = self.team1.setState(move)

        # fight if end turn action
        if move == 68:
            reward -= self.team1.money
            t2 = getGauntlet(round=self.team1.getRound())
            f = Fight(self.team1, t2)
            res = f.simulate()

            # reward based on results
            if res == 1:
                reward += 100 * self.team1.getRound()
                self.won_rounds += 1
            elif res == -1:
                reward = reward - 100 + (10 * self.team1.getRound())
                done = True
            elif res == 0:
                reward += 20
            if self.won_rounds > 10:
                done = True

            self.team1.nextTurn()

        if self.team1.moves > 30:
            reward -= 1000
            done = True

        og2 = 0
        for i in self.team1.friends:
            if i:
                og2 += 1

        if og2 > og:
            reward += 5

        # Done
        # if self.team1.alive and self.won_rounds < 10:
        #     done = False
        # elif self.team1.alive and self.won_rounds >= 10:
        #     done = True
        #     reward += 500
        # elif not self.team1.alive:
        #     done = True
        # reward -= 50

        # Observations
        obs, _ = self.team1.getState()

        info = {
            "move": move_print,
            "action_num": move,
            "round": round,
            "num_moves": self.team1.moves,
            "money": self.team1.money,
            "friends": self.team1,
        }

        return obs, reward, done, info

    def reset(self):
        self.team1 = Team()
        self.won_rounds = 0
        s, _ = self.team1.getState()
        return s

    def render(self):
        pass

    def close(self):
        pass
