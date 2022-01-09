from src.Team import Team
from src.Fight import Fight
from src.bots.Gauntlet import getGauntlet
from copy import deepcopy
import numpy as np


MAX_DEPTH = 10


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


def minmax(team1, enemies, depth, moves) -> np.array:
    if depth > MAX_DEPTH:
        return 0

    _, p = team1.getState()
    arr = np.zeros(len(p))
    for i in range(len(p)):
        if p[i] == 1:
            team = deepcopy(team1)
            team.setState(i)
            arr[i] = minmax(team, enemies, depth)

    moves.append(np.max(arr))
    return np.max(arr[i])


def run():
    t1 = Team()

    # enemies1 = getGauntlet(1)
    enemies1 = Team()

    round = 1

    while t1.alive:
        moves = [0] * MAX_DEPTH
        best = [-99999] * MAX_DEPTH
        minmax(t1, enemies1, 0, moves, best)
        for i in moves:
            s = t1.setState(i)
            # print(s)
        print(t1.friends)
        f = Fight(t1, enemies1)
        score = f.simulate()
        t1.nextTurn()
        print(f"| Round {round:4} | score: {score:4} |")

        round += 1
        enemies1 = getGauntlet(round)

    print(f"got to round: {round}")
