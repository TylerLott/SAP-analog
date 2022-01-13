import os
import torch as th

from stable_baselines3 import DQN
from stable_baselines3.common.logger import configure
from stable_baselines3.common.callbacks import EvalCallback
from stable_baselines3.common.monitor import Monitor

from src.bots.EnvWrapper import EnvWrapper
from src.bots.custPolicy import CustomPolicy


def run():
    NUM_TIMESTEPS = int(2e8)
    EVAL_FREQ = 50000
    EVAL_EPISODES = 20
    LOGDIR = "./train/dqn1"

    logger = configure(folder=LOGDIR)

    env = EnvWrapper()
    env = Monitor(env, filename=LOGDIR)

    def lr_schedule(initial, end):
        def func(progress_remaining):
            return initial - ((1 - progress_remaining) * (initial - end))

        return func

    model = DQN(
        CustomPolicy,
        env,
        verbose=1,
        learning_rate=lr_schedule(0.001, 0.000001),
        tensorboard_log="./train/dqn_rl/",
    )

    # model.set_logger(logger)

    eval_callback = EvalCallback(
        env,
        best_model_save_path=LOGDIR,
        log_path=LOGDIR,
        eval_freq=EVAL_FREQ,
        n_eval_episodes=EVAL_EPISODES,
    )

    model.learn(
        total_timesteps=NUM_TIMESTEPS, callback=eval_callback, tb_log_name="first_run"
    )

    model.save(os.path.join(LOGDIR, "final_model"))  # probably never get to this point.

    env.close()
