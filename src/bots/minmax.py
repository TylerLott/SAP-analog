from src.Team import Team
from src.Fight import Fight
from src.bots.Gauntlet import getGauntlet
from copy import deepcopy
import numpy as np
import time
import csv
import pandas as pd
import os
import threading
from functools import partial
from multiprocessing import Pool, Process

MAX_DEPTH = 2
DATA_PATH = "./data_collecter/data/data"

# def minmax(team1: Team, enemies: Team, depth, moves, best):

#     if depth >= MAX_DEPTH:
#         return 0
#     _, p = team1.getState()
#     for i in range(len(p)):
#         if p[i] == 1:
#             team = deepcopy(team1)
#             team.setState(i)
#             f = Fight(team, enemies)
#             cur = f.simulate()
#             cur += f.simulate()
#             cur += f.simulate()
#             cur = cur / 3
#             if cur > best[depth]:
#                 next_team = team
#                 best[depth] = cur
#                 moves[depth] = i
#     minmax(next_team, enemies, depth + 1, moves, best)
#     depth += 1


def bestMove(team1, enemies, depth):

    counter = [0]
    _, p = team1.getState()
    best_i = 0
    maxmax = -999999
    for i in range(len(p)):
        if p[i] == 1:
            maxSum = [-1000]
            t = deepcopy(team1)
            t.setState(i)
            adv = getAdvantage(t, enemies)
            DFS(t, enemies, adv, maxSum, depth + 1, counter)
            if adv + maxSum[0] > maxmax:
                best_i = i
                maxmax = adv + maxSum[0]

    return best_i, counter, maxmax


def DFS(team, enemies, sum, maxSum, depth, counter):
    counter[0] += 1
    if depth > MAX_DEPTH:
        maxSum[0] = max(maxSum[0], sum)
        return 0

    _, p = team.getState()
    for i in range(1, len(p)):
        if p[i] == 1:
            t = deepcopy(team)
            t.setState(i)
            adv = getAdvantage(t, enemies)
            DFS(t, enemies, sum + adv, maxSum, depth + 1, counter)


def getAdvantage(team, enemies):
    f = Fight(team, enemies)
    a = f.simulate()
    a += f.simulate()
    a += f.simulate()
    return a / 3


def run():
    print(f"Starting process {os.getpid()}")
    data_file = f"{DATA_PATH}_{os.getpid()}.csv"
    while True:
        t1 = Team()

        # enemies1 = getGauntlet(1)
        enemies1 = Team()

        round = 1
        wins = 0
        while t1.alive and wins < 10:

            for i in range(7):
                # start_time = time.time()
                move, count, m = bestMove(t1, enemies1, 0)

                state, _ = t1.getState()
                data = np.append(state, move)
                pd.DataFrame(data.reshape(-1, len(data))).to_csv(
                    data_file, mode="a", index=False, header=False
                )

                s = t1.setState(move)
                # print(
                #     f"| Move {i:3}: {s:15} | Moves Checked: {count[0]:8} | Estimated Advantage: {m:10.2f} | time taken: {time.time() - start_time:4.2f}s | money: {t1.money:2} |"
                # )

            enemies1 = getGauntlet(round)
            f = Fight(t1, enemies1)
            score = f.simulate()
            if score > 0:
                wins += 1
            t1.nextTurn()
            # print(f"| Round {round:4} | score: {score:4} | win number: {wins} |")

            round += 1

        # print(t1)
        # print(f"| got to round: {round} | number of wins: {wins} |")


def multi_run():
    proc = []
    for i in range(24):
        t = Process(target=run)
        proc.append(t)
    for i in proc:
        i.start()
