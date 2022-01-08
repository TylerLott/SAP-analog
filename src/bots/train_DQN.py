import os
import torch as th

from stable_baselines3 import DQN
from stable_baselines3.common.logger import configure
from stable_baselines3.common.callbacks import EvalCallback
from stable_baselines3.common.monitor import Monitor

from src.bots.EnvWrapper import EnvWrapper


def run():
    NUM_TIMESTEPS = int(2e7)
    EVAL_FREQ = 250000
    EVAL_EPISODES = 100
    LOGDIR = "./train/dqn1"  # moved to zoo afterwards.

    logger = configure(folder=LOGDIR)

    env = EnvWrapper()
    env = Monitor(env, filename=LOGDIR)

    # take mujoco hyperparams (but doubled timesteps_per_actorbatch to cover more steps.)
    policy_kwargs = dict(activation_fn=th.nn.ReLU, net_arch=[512, 256, 128])
    model = DQN(
        "MlpPolicy",
        env,
        verbose=1,
        policy_kwargs=policy_kwargs,
    )

    # model.set_parameters("./train/ppo1/best_model.zip")

    model.set_logger(logger)

    eval_callback = EvalCallback(
        env,
        best_model_save_path=LOGDIR,
        log_path=LOGDIR,
        eval_freq=EVAL_FREQ,
        n_eval_episodes=EVAL_EPISODES,
    )

    model.learn(total_timesteps=NUM_TIMESTEPS, callback=eval_callback)

    model.save(os.path.join(LOGDIR, "final_model"))  # probably never get to this point.

    env.close()
