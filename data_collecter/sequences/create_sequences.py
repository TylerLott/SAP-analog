import glob
import numpy as np
from collections import deque


def create_sequences(
    seq_len: int = 10,
    data_dir: str = "./data_collecter/games_norm/",
    verbose: int = 0,
):
    DATA_DIR = data_dir
    SEQ_LENGTH = seq_len

    all_files = glob.glob(DATA_DIR + "*.csv")

    seq_data = []

    for filename in all_files:
        data = np.loadtxt(filename, delimiter=",")
        obs, move = data[:, :-1], data[:, -1]
        move_one_hot = np.zeros((move.size, 69))
        move_one_hot[np.arange(move.size), move.astype(np.int32)] = 1

        hot_pad = np.zeros((SEQ_LENGTH - 1, move_one_hot.shape[-1]))
        obs_pad = np.zeros((SEQ_LENGTH - 1, obs.shape[-1]))

        move_one_hot = np.insert(move_one_hot, 0, hot_pad, axis=0)
        obs = np.insert(obs, 0, obs_pad, axis=0)

        data_comb = np.append(obs, move_one_hot, axis=1)
        print(data_comb.shape)

        prev_states = deque(maxlen=SEQ_LENGTH)

        for i in data_comb:
            prev_states.append([n for n in i[:-69]])
            if len(prev_states) == SEQ_LENGTH:
                seq_data.append([np.array(prev_states), i[-69:]])

    if verbose == 1:
        print(f"Generated {len(seq_data)} sequences")
    return seq_data


def create_flat(data_dir: str = "./data_collecter/games/"):
    DATA_DIR = data_dir

    all_files = glob.glob(DATA_DIR + "*.csv")

    seq_data = np.empty(shape=[1, 232])

    for filename in all_files:
        data = np.loadtxt(filename, delimiter=",")
        obs, move = data[:, :-1], data[:, -1]
        move_one_hot = np.zeros((move.size, 69))
        move_one_hot[np.arange(move.size), move.astype(np.int32)] = 1

        data_comb = np.append(obs, move_one_hot, axis=1)
        seq_data = np.append(seq_data, data_comb, axis=0)
        print(seq_data.shape)

    return seq_data


def create_for_transform(data_dir: str = "./data_collecter/games/"):
    DATA_DIR = data_dir

    all_files = glob.glob(DATA_DIR + "*.csv")

    a = "a"
    print(f"Reading data from {len(all_files)} games...")

    for filename in all_files:
        data = np.loadtxt(filename, delimiter=",")

        obs, move = data[:, :-1], data[:, -1]
        move_one_hot = np.zeros((move.size, 69))
        move_one_hot[np.arange(move.size), move.astype(np.int32)] = 1

        data_comb = np.append(obs, move_one_hot, axis=1)
        if a == "a":
            seq_data = data_comb
            a = "b"
        else:
            seq_data = np.append(seq_data, data_comb, axis=0)

    print(f"Data read completed")
    return seq_data
