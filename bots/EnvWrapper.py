import gym
from gym import spaces

from src.Team import Team
from src.Fight import Fight


class EnvWrapper(gym.Env):
    def __init__(self) -> None:
        super(EnvWrapper, self).__init__()
        self.team1 = Team()
        self.team2 = Team()
        state = self.team1.getState()
        self.action_space = spaces.Discrete(len(state[1]))
        self.observation_space = spaces.Discrete(state[0])

    def step(self, action1, action2):
        self.team1.setState(action1)
        self.team2.setState(action2)

        t1 = 0

        if self.team1.moves == 20:
            f = Fight(self.team1, self.team2)
            t1, _ = f.simulate()
            self.team1.nextTurn()
            self.team2.nextTurn()

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
