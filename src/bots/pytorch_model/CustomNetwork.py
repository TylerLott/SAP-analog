import torch as th
from torch import nn


class CustomNetwork(nn.Module):
    def __init__(self, obs_dim, out_dim):
        super(CustomNetwork, self).__init__()

        self.obs_dim = obs_dim
        self.out_dim = out_dim

        # Network

        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.5)

        self.layer1 = nn.Linear(self.obs_dim, 512)
        self.layer2 = nn.Linear(512, 512)
        self.layer3 = nn.Linear(512, 512)
        self.layer4 = nn.Linear(512, 256)
        self.out = nn.Linear(256, self.out_dim)

    def forward(self, obs):
        x = self.layer1(obs)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.relu(x)
        # x = self.dropout(x)
        x = self.layer3(x)
        x = self.relu(x)
        # x = self.dropout(x)
        x = self.layer4(x)
        x = self.relu(x)
        return self.out(x)
