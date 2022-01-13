import torch as th
from torch import nn


class CustomNetwork2(nn.Module):
    def __init__(self, friends_dim, shop_dim, team_dim, out_dim):
        super(CustomNetwork2, self).__init__()

        self.friends_dim = friends_dim
        self.shop_dim = shop_dim
        self.team_dim = team_dim
        self.out_dim = out_dim

        # Network

        self.relu = nn.ReLU()

        # Branch 1 (friends state)
        self.b1_l1 = nn.Linear(self.friends_dim, 256)
        self.b1_l2 = nn.Linear(256, 256)
        self.b1_l3 = nn.Linear(256, 128)

        # Branch 2 (shop state)
        self.b2_l1 = nn.Linear(self.shop_dim, 256)
        self.b2_l2 = nn.Linear(256, 256)
        self.b2_l3 = nn.Linear(256, 128)

        # Branch 3 (team state)
        self.b3_l1 = nn.Linear(self.team_dim, 32)

        # Main
        self.main1 = nn.Linear(288, 512)
        self.main2 = nn.Linear(512, 128)
        self.main3 = nn.Linear(128, 69)

    def forward(self, obs):
        f = obs[:, :420]
        s = obs[:, 420:883]
        t = obs[:, 883:]
        f = self.branch1(f)
        s = self.branch2(s)
        t = self.branch3(t)

        m = th.cat((f, s, t), 1)
        m = self.main1(m)
        m = self.main2(m)

        return self.main3(m)

    def branch1(self, obs):
        x = self.b1_l1(obs)
        x = self.b1_l2(x)
        return self.b1_l3(x)

    def branch2(self, obs):
        x = self.b2_l1(obs)
        x = self.b2_l2(x)
        return self.b1_l3(x)

    def branch3(self, obs):
        return self.b3_l1(obs)
