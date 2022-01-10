import torch as th
from torch import nn


class CustomNetwork(nn.Module):
    def __init__(self, obs_dim, out_dim):
        super(CustomNetwork, self).__init__()

        self.obs_dim = obs_dim
        self.out_dim = out_dim

        # Network

        self.layer1 = nn.Linear(self.obs_dim, 256)
        self.relu1 = nn.ReLU()
        self.layer2 = nn.Linear(256, 512)
        self.relu2 = nn.ReLU()
        self.layer3 = nn.Linear(512, 512)
        self.relu3 = nn.ReLU()
        self.layer4 = nn.Linear(512, 256)
        self.relu4 = nn.ReLU()
        self.layer5 = nn.Linear(256, self.out_dim)
        self.out = nn.Softmax()

    def forward(self, obs):
        x = self.layer1(obs)
        x = self.relu1(x)
        x = self.layer2(x)
        x = self.relu2(x)
        x = self.layer3(x)
        x = self.relu3(x)
        x = self.layer4(x)
        x = self.relu4(x)
        x = self.layer5(x)
        return self.out(x)
