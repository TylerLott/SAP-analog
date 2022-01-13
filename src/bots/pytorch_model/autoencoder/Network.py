import torch as th
from torch import nn


class Encoder(nn.Module):
    def __init__(self, in_dim, out_dim):
        super(Encoder, self).__init__()

        self.in_dim = in_dim
        self.out_dim = out_dim

        # Network

        self.l1 = nn.Linear(self.in_dim, 128)
        self.l2 = nn.Linear(128, 64)
        self.l3 = nn.Linear(64, 32)
        self.l4 = nn.Linear(32, out_dim)

    def forward(self, obs):
        x = self.l1(obs)
        x = self.l2(x)
        x = self.l3(x)
        return self.l4(x)


class Decoder(nn.Module):
    def __init__(self, in_dim, out_dim):
        super(Decoder, self).__init__()

        self.in_dim = in_dim
        self.out_dim = out_dim

        # Network

        self.l1 = nn.Linear(self.in_dim, 32)
        self.l2 = nn.Linear(32, 64)
        self.l3 = nn.Linear(64, 128)
        self.l4 = nn.Linear(128, out_dim)

    def forward(self, obs):
        x = self.l1(obs)
        x = self.l2(x)
        x = self.l3(x)
        return self.l4(x)


class AutoEncoder(nn.Module):
    def __init__(self, in_dim, compress_dim):
        super(AutoEncoder, self).__init__()

        self.in_dim = in_dim
        self.compress_dim = compress_dim

        self.enc = Encoder(self.in_dim, self.compress_dim)
        self.dec = Decoder(self.compress_dim, self.in_dim)

    def forward(self, obs):
        x = self.enc(obs)
        return self.dec(x)

    def save_enc(self, fp):
        th.save(self.enc, fp)

    def save_dec(self, fp):
        th.save(self.dec, fp)
