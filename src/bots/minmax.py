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
DATA_PATH = "./data_collecter/games/"

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
            if i != 68:
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
            if i != 68:
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
    game = 0
    while True:
        t1 = Team()

        # enemies1 = getGauntlet(1)
        enemies1 = Team()

        round = 1
        wins = 0
        ties = 0
        move_hist = None

        while t1.alive and wins < 10:
            old_adv = -10000

            for i in range(10):
                # start_time = time.time()
                next_enemies = getGauntlet(round)
                move, numMovesChecked, maxAdv = bestMove(t1, next_enemies, 0)

                state, _ = t1.getState()

                if move == 68 or (t1.money == 0 and maxAdv <= old_adv):
                    break

                if type(move_hist) != np.ndarray:
                    move_hist = np.expand_dims(np.append(state, move), axis=0)
                else:
                    move_hist = np.append(
                        move_hist,
                        np.expand_dims(np.append(state, move), axis=0),
                        axis=0,
                    )
                # data = np.append(state, move)
                # pd.DataFrame(data.reshape(-1, len(data))).to_csv(
                #     data_file, mode="a", index=False, header=False
                # )

                s = t1.setState(move)

                # print(
                #     f"| Move {i+1:3}: {s:15} | Moves Checked: {numMovesChecked[0]:8} | Estimated Advantage: {maxAdv:10.2f} | time taken: {time.time() - start_time:4.2f}s | money: {t1.money:2} |"
                # )
                old_adv = maxAdv

            if move != 68:
                state, _ = t1.getState()
                move = 68
                t1.setState(68)
                move_hist = np.append(
                    move_hist, np.expand_dims(np.append(state, move), axis=0), axis=0
                )

            enemies1 = getGauntlet(round)
            f = Fight(t1, enemies1)
            score = f.simulate()
            if score > 0:
                wins += 1
            if score == 0:
                ties += 1
            t1.nextTurn()
            # print(f"| Round {round:4} | score: {score:4} | win number: {wins} |")

            # if round > 15:
            #     print("got past round 15")
            # if wins > 6:
            #     print(f"I won at round: {round}")
            # if not t1.alive:
            #     print(f"| got to round {round} and lost | {wins} wins | {ties} ties |")

            round += 1

        if wins > 6:
            data_file = (
                f"{DATA_PATH}/game_{game}_{os.getpid()}_round_{round}_wins_{wins}.csv"
            )
            np.savetxt(data_file, move_hist, delimiter=",")
            print(f"game {game} saved")
        game += 1
        # print(f"| got to round: {round} | number of wins: {wins} |")


def multi_run(processes):
    proc = []
    for i in range(processes):
        t = Process(target=run)
        proc.append(t)
    for i in proc:
        i.start()
