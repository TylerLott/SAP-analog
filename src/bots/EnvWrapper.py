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

        # penalize for bad moves
        _, p = self.team1.getState()
        amt = 1
        if p[move] == 0 and move != 68:
            # more penalty for many moves
            if self.team1.getMovesNum() > 10:
                amt = amt * (self.team1.moves - 10)
            reward -= amt
        else:
            reward += amt

        og = 0
        for i in self.team1.friends:
            if i:
                og += 1

        # Do move
        self.team1.setState(move)

        # fight if end turn action
        if move == 68:
            t2 = getGauntlet(round=self.team1.getRound())
            f = Fight(self.team1, t2)
            res = f.simulate()
            self.team1.nextTurn()

            # reward based on results
            if res == 1:
                reward += 300
                self.won_rounds += 1
            elif res == -1:
                reward -= 20
            # elif res == 0:
            #     reward += 10

        og2 = 0
        for i in self.team1.friends:
            if i:
                og2 += 1

        if og2 > og:
            reward += 5

        # Done
        if self.team1.alive and self.won_rounds < 10:
            done = False
        elif self.team1.alive and self.won_rounds >= 10:
            done = True
            reward += 500
        elif not self.team1.alive:
            done = True
            # reward -= 50

        # Observations
        obs, _ = self.team1.getState()

        info = {}

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
