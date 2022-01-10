import pandas as pd
from torch.utils.data import Dataset


class SAPDataset_train(Dataset):
    def __init__(self, csv_file, root_dir):
        self.data = 0

    def __len__(self):
        pass

    def __getitem__(self, idx):
        pass


class SAPDataset_valid(Dataset):
    def __init__(self, csv_file, root_dir):
        self.data = 0

    def __len__(self):
        pass

    def __getitem__(self, idx):
        pass
