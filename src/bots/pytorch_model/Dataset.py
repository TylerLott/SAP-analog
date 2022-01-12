import pandas as pd
import numpy as np
import torch
from torch.utils.data import Dataset


class SAPDataset_train(Dataset):
    def __init__(self, csv_file="./data_collecter/full_data/train.csv"):
        self.data = pd.read_csv(csv_file)

    def __len__(self):
        return self.data.shape[0]

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        state = self.data.iloc[idx, 1:-1].to_numpy()
        state = torch.from_numpy(state.astype("float32"))
        moves = np.zeros(69)
        move = self.data.iloc[idx, -1]
        moves[int(move)] = 1
        moves = torch.from_numpy(moves.astype("float32"))

        item = [state, moves]
        return item


class SAPDataset_valid(Dataset):
    def __init__(self, csv_file="./data_collecter/full_data/validation.csv"):
        self.data = pd.read_csv(csv_file)

    def __len__(self):
        return self.data.shape[0]

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        state = self.data.iloc[idx, 1:-1].to_numpy()
        state = torch.from_numpy(state.astype("float32"))
        moves = np.zeros(69)
        move = self.data.iloc[idx, -1]
        moves[int(move)] = 1
        moves = torch.from_numpy(moves.astype("float32"))

        item = [state, moves]
        return item
