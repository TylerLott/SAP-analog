import gym
from stable_baselines3 import PPO
from EnvWrapper import EnvWrapper


env = EnvWrapper()

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=25000)

obs = env.reset()

while True:
    action, _states = model.predict(obs)
    obs, reward, done, info = env.step(action)
    if done:
        obs = env.reset()
