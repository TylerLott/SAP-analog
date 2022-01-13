import torch as th
from torch import nn
from src.bots.pytorch_model.autoencoder.Network import Encoder


class CustomNetwork3(nn.Module):
    def __init__(self, friends_dim, shop_dim, team_dim, out_dim):
        super(CustomNetwork3, self).__init__()

        self.friends_dim = friends_dim
        self.shop_dim = shop_dim
        self.team_dim = team_dim
        self.out_dim = out_dim

        # Network

        # self.autoencoder = Encoder(420, 8)
        self.autoencoder = th.load("./train/custDQN/autoencoder_enc_20220112_162039_0")
        self.autoencoder.train(False)
        self.relu = nn.ReLU()

        # Branch 3 (team state)
        self.b3_l1 = nn.Linear(self.team_dim, 16)

        # Main
        self.main1 = nn.Linear(139, 512)
        self.main2 = nn.Linear(512, 128)
        self.main3 = nn.Linear(128, 69)

    def forward(self, f, s, t):

        a1 = f[:, :84]
        a2 = f[:, 84:168]
        a3 = f[:, 168:252]
        a4 = f[:, 252:336]
        a5 = f[:, 336:]

        a1 = self.autoencoder(a1)
        a2 = self.autoencoder(a2)
        a3 = self.autoencoder(a3)
        a4 = self.autoencoder(a4)
        a5 = self.autoencoder(a5)

        s1 = s[:, :84]
        s2 = s[:, 84:168]
        s3 = s[:, 168:252]
        s4 = s[:, 252:336]
        s5 = s[:, 336:420]
        sf = s[:, 420:]

        s1 = self.autoencoder(s1)
        s2 = self.autoencoder(s2)
        s3 = self.autoencoder(s3)
        s4 = self.autoencoder(s4)
        s5 = self.autoencoder(s5)

        t = self.branch3(t)

        m = th.cat((a1, a2, a3, a4, a5, s1, s2, s3, s4, s5, sf, t), 1)
        m = self.main1(m)
        m = self.main2(m)

        return self.main3(m)

    def branch3(self, obs):
        return self.b3_l1(obs)
