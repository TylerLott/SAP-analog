# tf implementation for training A2C model
import tensorflow as tf
from datetime import datetime
from src.bots.transformer.network import make_model
from src.bots.EnvWrapper import EnvWrapper

STORE_PATH = "./train/a2c/tf/"
MODEL_STORE_PATH = "./train/a2c/models/"
CRITIC_LOSS_WEIGHT = 0.5
ACTOR_LOSS_WEIGHT = 1.0
ENTROPY_LOSS_WEIGHT = 0.05
BATCH_SIZE = 64
GAMMA = 0.95


# util functions for loss calc
def critic_loss(discounted_reward, predicted_values):
    return (
        tf.keras.losses.mean_squared_error(discounted_reward, predicted_values)
        * CRITIC_LOSS_WEIGHT
    )


def actor_loss(combined, policy_logits):
    actions = combined[:, 0]
    advantages = combined[:, 1]
    sparse_ce = tf.keras.losses.SparseCategoricalCrossentropy(
        from_logits=True, reduction=tf.keras.losses.Reduction.SUM
    )
    actions = tf.cast(actions, tf.int32)
    policy_loss = sparse_ce(actions, policy_logits, sample_weights=advantages)

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
    animals = state[35:].reshape(1, 5, 7)
    shop_an = state[35:70].reshape(1, 5, 7)
    shop_food = state[70:72].reshape(1, 2)
    team = state[72:77].reshape(1, 5)
    possible = state[77:].reshape(1, 69)

    return {
        "animals": animals,
        "shop_an": shop_an,
        "shop_food": shop_food,
        "team": team,
        "possible": possible,
    }


def format_states(states):
    states = np.array(states)
    animals = state[:, 35:].reshape(-1, 5, 7)
    shop_an = state[:, 35:70].reshape(-1, 5, 7)
    shop_food = state[:, 70:72].reshape(-1, 2)
    team = state[:, 72:77].reshape(-1, 5)
    possible = state[:, 77:].reshape(-1, 69)

    return {
        "animals": animals,
        "shop_an": shop_an,
        "shop_food": shop_food,
        "team": team,
        "possible": possible,
    }


model.compile(optimizer=tf.keras.optimizers.Adam(), loss=[critic_loss, actor_loss])

train_writer = tf.summary.create_file_writer(
    STORE_PATH + f'A2C_transformer_{datetime.now().strftime("%d%m%Y%H%M")}'
)


def train():
    # model
    model = make_model()

    # load weights
    # model.load_weights()

    # env
    env = EnvWrapper()

    # train loop
    num_steps = 10_000_000
    episode_reward_sum = 0
    state = env.reset()
    episode = 1

    for step in range(num_steps):
        rewards = []
        actions = []
        values = []
        states = []
        dones = []
        for _ in range(BATCH_SIZE):
            policy_logits, _ = model(format_state(state))

            action, value = model.action_value(format_state(state))
            new_state, reward, done, _ = env.step(action.numpy()[0])

            actions.append(action)
            values.append(value)
            states.append(state)
            dones.append(done)
            episode_reward_sum += reward

            state = new_state

            if done:
                rewards.append(0.0)
                state = env.reset()
                print(f"Episode: {episode}, reward: {episode_reward_sum}, loss: {loss}")
                with train_writer.as_default():
                    tf.summary.scalar("rewards", episode_reward_sum, episode)
                episode_reward_sum = 0
                episode += 1
            else:
                rewards.append(reward)

        _, next_value = model.action_value(format_state(state))
        discounted_rewards, advantages = discounted_rewards_advantages(
            rewards, dones, values, next_value.numpy()[0]
        )

        combines = np.zeros((len(actions), 2))
        combines[:, 0] = actions
        combines[:, 1] = advantages

        loss = model.train_on_batch(
            format_states(states), [discounted_rewards, combined]
        )

        with train_writer.as_default():
            tf.summary.scalar("tot_loss", np.sum(loss), step)

        if episode % 1000 == 0:
            model.save_weights(
                MODEL_STORE_PATH
                + f"model_ep_{episode}_{datetime.now().strftime('%d%m%Y%H%M')}"
            )
