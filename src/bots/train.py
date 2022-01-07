import os
import json
import time
import numpy as np
import src.bots.Model as mlp
from src.bots.Model import Model
from src.bots.Rollout import rollout

# Settings
random_seed = 612
population_size = 256
total_tournaments = 500_000
save_freq = 1000


def run():
    def mutate(length, mutation_rate, mutation_sigma):
        # (not used, in case I wanted to do partial mutations)
        # create an additive mutation vector of some size
        mask = np.random.randint(int(1 / mutation_rate), size=length)
        mask = 1 - np.minimum(mask, 1)
        noise = np.random.normal(size=length) * mutation_sigma
        return mask * noise

    # Log results
    logdir = "./train/ga_selfplay"
    if not os.path.exists(logdir):
        os.makedirs(logdir)

    # Create two instances of a feed forward policy we may need later.
    policy_left = Model(mlp.games["SAP_small"])
    policy_right = Model(mlp.games["SAP_small"])
    param_count = policy_left.param_count
    print(
        "Number of parameters of the neural net policy:", param_count
    )  # 273 for slimevolleylite

    # store our population here
    population = (
        np.random.normal(size=(population_size, param_count)) * 0.5
    )  # each row is an agent.

    with open("./train/ga_selfplay/ga_00032000.json") as f:
        data = json.load(f)

        for i in range(population.shape[0]):
            population[i] = data[0]

    winning_streak = [
        0
    ] * population_size  # store the number of wins for this agent (including mutated ones)

    # create the gym environment, and seed it
    np.random.seed(random_seed)
    start_time = time.time()
    history = []
    for tournament in range(1, total_tournaments + 1):

        m, n = np.random.choice(population_size, 2, replace=False)

        policy_left.set_model_params(population[m])
        policy_right.set_model_params(population[n])

        # the match between the mth and nth member of the population
        score, length = rollout(policy_right, policy_left)

        history.append(length)
        # if score is positive, it means policy_right won.
        if score == 0:  # if the game is tied, add noise to the left agent.
            population[m] = policy_left.get_random_model_params()
            population[n] = policy_left.get_random_model_params()
            winning_streak[m] = 0
            winning_streak[n] = 0
        if score > 0:
            population[m] = population[n] + np.random.normal(
                size=param_count
            ) * 0.0001 * np.random.randint(2, size=param_count) * np.random.randint(
                2, size=param_count
            )
            winning_streak[m] = winning_streak[n]
            winning_streak[n] += 1
        if score < 0:
            population[n] = population[m] + np.random.normal(
                size=param_count
            ) * 0.0001 * np.random.randint(2, size=param_count) * np.random.randint(
                2, size=param_count
            )

            winning_streak[n] = winning_streak[m]
            winning_streak[m] += 1

        if tournament % save_freq == 0:
            model_filename = os.path.join(
                logdir, "ga_" + str(tournament).zfill(8) + ".json"
            )
            with open(model_filename, "wt") as out:
                record_holder = np.argmax(winning_streak)
                record = winning_streak[record_holder]
                json.dump(
                    [population[record_holder].tolist(), record],
                    out,
                    sort_keys=True,
                    indent=0,
                    separators=(",", ": "),
                )

        if (tournament) % 500 == 0:
            # each game takes ~.25s
            record_holder = np.argmax(winning_streak)
            record = winning_streak[record_holder]
            end_time = time.time()
            s = f"| game: {tournament:7} | best_winning_streak: {record:5} | mean_duration: {np.mean(history):6.3} | low_duration: {np.min(history):6} | high_duration: {np.max(history):6} | stdev: {np.std(history):5.3} | time_taken: {end_time - start_time:8.6}s |"
            print(s)
            history = []
            start_time = end_time
