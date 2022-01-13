from stable_baselines3.common.policies import BasePolicy
from stable_baselines3.common.torch_layers import FlattenExtractor
import torch as th
import gym

from src.bots.pytorch_model.CustomNetwork import CustomNetwork


class CustomPolicy(BasePolicy):
    def __init__(
        self,
        observation_space,
        action_space,
        features_dim,
    ):
        super(CustomPolicy, self).__init__(
            observation_space, action_space, optimizer_class=th.optim.Adam
        )

        self.q_net = CustomNetwork(888, 69)

        self.q_net_target = CustomNetwork(888, 69)
        self.q_net_target.load_state_dict(
            th.load("./train/custDQN/model_20220111_193416_5")
        )
        self.optimizer = th.optim.Adam(self.parameters(), lr=0.00001)

    def forward(self, obs):
        return self.q_net(obs)

    def _predict(self, obs, deterministic=True):
        q_vals = self.forward(obs)
        action = q_vals.argmax(dim=1).reshape(-1)
        return action

    def _get_constructor_parameters(self):
        return super()._get_constructor_parameters()
