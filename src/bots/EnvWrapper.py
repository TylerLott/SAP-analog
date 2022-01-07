import gym
from gym import spaces

from src.Team import Team
from src.Fight import Fight


class EnvWrapper(gym.Env):
    def __init__(self) -> None:
        super(EnvWrapper, self).__init__()
        self.team1 = Team()
        state = self.team1.getState()
        self.action_space = spaces.Discrete(len(state[1]))
        self.observation_space = spaces.Discrete(len(state[0]))

    def step(self, action1):

        t1 = 0

        if self.team1.moves == 20:
            t2 = getGauntlet(round=self.team1.getRound())
            f = Fight(self.team1)
            t1, _ = f.simulate()
            self.team1.nextTurn()

        # Done
        if self.team1.alive and self.team2.alive:
            done = False
        else:
            done = True

        # Reward
        reward = t1

        # Observations
        obs = self.team1.getState()

        info = {"otherObs": self.team2.getState()}

        return obs, reward, done, info

    def reset(self):
        self.team1 = Team()
        self.team2 = Team()
        return self.team1.getState(), self.team2.getState()

    def render(self):
        pass

    def close(self):
        pass
