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
        self.moves = 0
        state = self.team1.getState()
        self.action_space = spaces.Discrete(len(state[1]))
        self.observation_space = spaces.Box(
            low=0, high=1, shape=(len(state[0]),), dtype=np.float32
        )

    def step(self, move):

        reward = 0
        done = False
        round = self.team1.round

        # _, p = self.team1.getState()
        # if p[move] == 1 and move != 0:
        #     reward += 1

        # fight if end turn action
        if move == 68 or self.moves > 10:
            move_print = self.team1.setState(68)
            t2 = getGauntlet(round=self.team1.getRound())
            f = Fight(self.team1, t2)
            res = f.simulate()

            # reward based on results
            if res >= 0:
                reward += 10
                reward += res
            if res > 0:
                self.won_rounds += 1

            self.team1.nextTurn()
            self.moves = 0

            if res < 0:
                done = True

        else:
            # Do move
            move_print = self.team1.setState(move)
            self.moves += 1

        # Done
        if not self.team1.alive or self.won_rounds >= 10:
            done = True

        # Observations
        obs, p = self.team1.getState()

        info = {
            "move": move_print,
            "action_num": move,
            "round": round,
            "num_moves": self.team1.moves,
            "money": self.team1.money,
            "friends": self.team1,
        }

        return np.concatenate([obs, p]), reward, done, info

    def reset(self):
        self.team1 = Team()
        self.won_rounds = 0
        s, p = self.team1.getState()
        return np.concatenate([s, p])

    def render(self):
        pass

    def close(self):
        pass
