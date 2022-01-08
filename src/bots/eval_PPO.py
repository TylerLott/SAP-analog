import os
import torch as th

from stable_baselines3 import PPO
from stable_baselines3.common.logger import configure
from stable_baselines3.common.callbacks import EvalCallback
from stable_baselines3.common.monitor import Monitor

from src.bots.EnvWrapper import EnvWrapper


def run():

    env = EnvWrapper()

    # take mujoco hyperparams (but doubled timesteps_per_actorbatch to cover more steps.)
    policy_kwargs = dict(activation_fn=th.nn.ReLU, net_arch=[128, 32, 512, 512])
    model = PPO(
        "MlpPolicy",
        env,
        verbose=1,
        batch_size=512,
        n_steps=4096,
        n_epochs=10,
        policy_kwargs=policy_kwargs,
        learning_rate=0.00001
        # ent_coef=0.01,
    )

    model.set_parameters("./train/ppo1/best_model.zip")
    done = False

    obs = env.reset()
    episode_move = 1

    while not done:
        move, _ = model.predict(obs)
        obs, reward, done, info = env.step(move)
        s = f'| ep_move: {episode_move: 3} | move: {info["move"]:20} | action_num: {info["action_num"]:5} | num_moves: {info["num_moves"]:5} | money: {info["money"]:5} | round: {info["round"]:5} | reward: {reward:10}|'
        print(s)
        episode_move += 1
    # print(info["friends"])
