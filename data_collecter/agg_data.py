import glob
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def run():
    DATA_DIR = "./data_collecter/data/"

    all_files = glob.glob(DATA_DIR + "*.csv")

    li = []

    old = "a"

    for filename in all_files:

        big_df = pd.read_csv(filename).to_numpy()

        print("processing file:", filename.split("\\")[-1])
        print(f"found {big_df.shape[0]} records")

        if type(old) == str:
            old = big_df
        else:
            old = np.append(old, big_df, axis=0)

    print(old.shape)

    actual_df = pd.DataFrame(old)
    print("actual:", actual_df.shape[0])
    print("len:", actual_df.shape[-1])

    no_na = actual_df.dropna()
    print("no_na:", no_na.shape[0])

    sub = actual_df.columns[0:-1]
    no_dup_state = actual_df.drop_duplicates(subset=sub)
    print("no_dup_state:", no_dup_state.shape[0])

    moves = no_dup_state[no_dup_state.columns[-1]]
    sns.distplot(moves)
    plt.show()
