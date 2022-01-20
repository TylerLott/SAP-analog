# tf implementation for training A2C model
from tqdm import tqdm
import silence_tensorflow.auto
import tensorflow as tf
import numpy as np
from datetime import datetime
from src.bots.transformer.network import TransformerModel
from src.bots.EnvWrapper import EnvWrapper

STORE_PATH = "./train/a2c/tf/"
MODEL_STORE_PATH = "./train/a2c/models/"
CRITIC_LOSS_WEIGHT = 0.5
ACTOR_LOSS_WEIGHT = 1.0
ENTROPY_LOSS_WEIGHT = 0.03
BATCH_SIZE = 64
GAMMA = 0.99


# util functions for loss calc
def critic_loss(discounted_reward, predicted_values):
    h = tf.keras.losses.Huber()
    return h(discounted_reward, predicted_values) * CRITIC_LOSS_WEIGHT


def actor_loss(combined, policy_logits):
    actions = combined[:, 0]
    advantages = combined[:, 1]
    sparse_ce = tf.keras.losses.SparseCategoricalCrossentropy(
        from_logits=True, reduction=tf.keras.losses.Reduction.NONE
    )
    actions = tf.cast(actions, tf.int32)
    policy_loss = sparse_ce(actions, policy_logits, sample_weight=advantages)

    probs = tf.nn.softmax(policy_logits)
    entropy_loss = tf.keras.losses.categorical_crossentropy(probs, probs)

    return policy_loss * ACTOR_LOSS_WEIGHT - entropy_loss * ENTROPY_LOSS_WEIGHT


def discounted_rewards_advantages(rewards, dones, values, next_value):
    discounted_rewards = np.array(rewards + [next_value[0]])

    for t in reversed(range(len(rewards))):
        discounted_rewards[t] = rewards[t] + GAMMA * discounted_rewards[t + 1] * (
            1 - dones[t]
        )
    discounted_rewards = discounted_rewards[:-1]

    advantages = discounted_rewards - np.stack(values)[:, 0]
    return discounted_rewards, advantages


def format_state(state):
    animals = state[:35].reshape(1, 5, 7)
    shop_an = state[35:70].reshape(1, 5, 7)
    shop_food = state[70:72].reshape(1, 2)
    team = state[72:77].reshape(1, 5)
    possible = state[77:].reshape(1, 69)

    return [animals, shop_an, shop_food, team, possible]


def format_states(states):
    states = np.array(states)
    animals = states[:, :35].reshape(-1, 5, 7)
    shop_an = states[:, 35:70].reshape(-1, 5, 7)
    shop_food = states[:, 70:72].reshape(-1, 2)
    team = states[:, 72:77].reshape(-1, 5)
    possible = states[:, 77:].reshape(-1, 69)

    return [animals, shop_an, shop_food, team, possible]


train_writer = tf.summary.create_file_writer(
    STORE_PATH + f'A2C_transformer_{datetime.now().strftime("%d%m%Y%H%M")}'
)


def train():
    # model
    model = TransformerModel()
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.00001),
        loss=[actor_loss, critic_loss],
    )

    # load weights
    model.load_weights("./train/a2c/models/model_ep_5200_190120222301")
    model.trainable = True

    # env
    env = EnvWrapper()

    # train loop
    num_eps = 10_000_000
    episode_reward_sum = 0
    state = env.reset()
    episode = 1
    loss = None

    for step in range(num_eps):
        rewards = []
        actions = []
        values = []
        states = []
        dones = []
        done = False
        while not done:
            policy_logits, _ = model(format_state(state), training=True)

            action, value = model.action_value(format_state(state))
            new_state, reward, done, _ = env.step(action.numpy()[0])

            actions.append(action)
            values.append(value[0])
            states.append(state)
            dones.append(done)
            rewards.append(reward)
            episode_reward_sum += reward

            state = new_state

        _, next_value = model.action_value(format_state(state))
        discounted_rewards, advantages = discounted_rewards_advantages(
            rewards, dones, values, next_value[0]
        )

        combined = np.zeros((len(actions), 2))
        combined[:, 0] = actions
        combined[:, 1] = advantages

        loss = model.train_on_batch(
            format_states(states), [combined, discounted_rewards]
        )
        print(
            f"Episode: {episode}, reward: {episode_reward_sum}, loss: {loss[2]}, num_steps: {len(rewards)}, wins: {env.won_rounds}"
        )
        print("actions:", [int(i) for i in actions])

        with train_writer.as_default():
            tf.summary.scalar("rewards", episode_reward_sum, episode)
        with train_writer.as_default():
            tf.summary.scalar("tot_loss", loss[2], step)
        with train_writer.as_default():
            tf.summary.scalar("actor_loss", loss[0], step)
        with train_writer.as_default():
            tf.summary.scalar("critic_loss", loss[1], step)
        with train_writer.as_default():
            tf.summary.scalar("won_rounds", env.won_rounds, step)

        if episode % 100 == 0:
            print("saving model...")
            model.save_weights(
                MODEL_STORE_PATH
                + f"model_ep_{episode}_{datetime.now().strftime('%d%m%Y%H%M')}"
            )

        state = env.reset()
        episode_reward_sum = 0
        episode += 1
