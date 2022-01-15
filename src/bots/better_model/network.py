from distutils.command.config import config
from src.Team import Team
import tensorflow as tf
import tensorflow_probability as tfp
from tensorflow.keras import Sequential, Model, Input
from tensorflow.keras.layers import Dense, LSTM, Flatten, Softmax, Layer


tfd = tfp.distributions


class ScalarEncoder(Layer):
    def __init__(self, output_dim):
        super(ScalarEncoder, self).__init__()
        self.output_dim = output_dim

        self.network = Sequential(
            [
                Dense(
                    self.output_dim,
                    activation="relu",
                    name="ScalarEncoder_dense",
                    kernel_regularizer="l2",
                )
            ]
        )

    def get_config(self):
        config = super().get_config().copy()
        config.update({"output_dim": self.output_dim})
        return config

    def call(self, scalar_feature):
        batch_size = tf.shape(scalar_feature)[0]
        scalar_feature_encoded = self.network(scalar_feature)
        return scalar_feature_encoded


class LSTMCore(Layer):
    def __init__(self, output_dim, internal_size):
        super(LSTMCore, self).__init__()

        self.output_dim = output_dim
        self.internal_size = internal_size

        self.lstm_1 = LSTM(
            self.internal_size,
            name="lstm_core_1",
            return_sequences=True,
            return_state=True,
            kernel_regularizer="l2",
        )

        self.lstm_2 = LSTM(
            self.internal_size,
            name="lstm_core_2",
            return_sequences=True,
            return_state=True,
            kernel_regularizer="l2",
        )

        self.network = Sequential(
            [
                Flatten(),
                Dense(
                    self.output_dim,
                    name="core_dense",
                    activation="relu",
                    kernel_regularizer="l2",
                ),
            ]
        )

    def get_config(self):
        config = super().get_config().copy()
        config.update(
            {"internal_size": self.internal_size, "output_dim": self.output_dim}
        )
        return config

    def call(self, feature_encoded, memory_state, carry_state):
        batch_size = tf.shape(feature_encoded)[0]

        initial_state_1 = (memory_state, carry_state)
        core_output_1, final_mem_state_1, final_carry_state_1 = self.lstm_1(
            feature_encoded, initial_state=initial_state_1
        )

        initial_state_2 = (final_mem_state_1, final_carry_state_1)
        core_output_2, final_mem_state_2, final_carry_state_2 = self.lstm_2(
            core_output_1, initial_state=initial_state_2
        )

        core_output = self.network(core_output_2)

        return core_output, final_mem_state_2, final_carry_state_2


class ActionHead(Layer):
    def __init__(self, output_dim):
        super(ActionHead, self).__init__()

        self.output_dim = output_dim
        self.network = Sequential(
            [
                Dense(self.output_dim, name="action_head", kernel_regularizer="l2"),
                Softmax(),
            ]
        )

    def get_config(self):
        config = super().get_config().copy()
        config.update(
            {
                "output_dim": self.output_dim,
            }
        )
        return config

    def call(self, core_output):
        batch_size = tf.shape(core_output)[0]
        action_logits = self.network(core_output)

        action_dist = tfd.Categorical(probs=action_logits)
        action = action_dist.sample()
        action_type_onehot = tf.one_hot(action, self.output_dim)

        return action_logits, action


class BetaPets(Model):
    def __init__(self, input_size, internal_size):
        super(BetaPets, self).__init__()

        self.input_size = input_size
        self.internal_size = internal_size

        # State Encoders
        self.friend_encoder = ScalarEncoder(output_dim=40)
        self.team_encoder = ScalarEncoder(output_dim=5)
        self.shop_encoder = ScalarEncoder(output_dim=42)
        self.possible_encoder = ScalarEncoder(output_dim=69)

        # core
        self.core = LSTMCore(
            output_dim=self.input_size, internal_size=self.internal_size
        )

        # action head
        self.action_head = ActionHead(output_dim=69)

    def get_config(self):
        config = super().get_config().copy()
        return config

    def call(self, friends, team, shop, possible, memory_state, carry_state):
        batch_size = tf.shape(friends)[0]

        friends_encoded = self.friend_encoder(friends)
        team_encoded = self.team_encoder(team)
        shop_encoded = self.shop_encoder(shop)
        possible_encoded = self.possible_encoder(possible)

        features_encoded = tf.concat(
            [friends_encoded, team_encoded, shop_encoded, possible_encoded], axis=-1
        )

        core_outputs, final_memory_state, final_carry_state = self.core(
            features_encoded, memory_state, carry_state
        )

        action_logits, action = self.action_head(core_outputs)

        return action_logits, final_memory_state, final_carry_state, action


class DeepModel(Model):
    def __init__(self):
        super(DeepModel, self).__init__()

        # State Encoders
        self.friend_encoder = ScalarEncoder(output_dim=256)
        self.team_encoder = ScalarEncoder(output_dim=32)
        self.shop_encoder = ScalarEncoder(output_dim=256)
        self.possible_encoder = ScalarEncoder(output_dim=69)

        self.l1 = Dense(512, activation="relu", kernel_regularizer="l2")
        self.l2 = Dense(256, activation="relu", kernel_regularizer="l2")
        self.l3 = Dense(256, activation="relu", kernel_regularizer="l2")
        self.out = Dense(69, activation="softmax")

    def call(self, friends, team, shop, possible):
        f = self.friend_encoder(friends)
        t = self.team_encoder(team)
        s = self.shop_encoder(shop)
        p = self.possible_encoder(possible)

        args = tf.concat([f, t, s, p], axis=1)

        x = self.l1(args)
        x = self.l2(x)
        x = self.l3(x)
        return self.out(x)


def make_dense(name):
    friends = Input(shape=(40))
    team = Input(shape=(5))
    shop = Input(shape=(49))
    possible = Input(shape=(69))

    action_logits = DeepModel()(friends, team, shop, possible)

    model = Model(
        inputs={
            "friends": friends,
            "team": team,
            "shop": shop,
            "possible": possible,
        },
        outputs={
            "action_logits": action_logits,
        },
        name=name,
    )

    return model


def make_model(name):

    friends = Input(shape=(10, 40))
    team = Input(shape=(10, 5))
    shop = Input(shape=(10, 49))
    possible = Input(shape=(10, 69))
    memory_state = Input(shape=(256), name="mem_in")
    carry_state = Input(shape=(256), name="carry_in")

    action_logits, final_mem_state, final_carry_state, action = BetaPets(
        input_size=156, internal_size=256
    )(friends, team, shop, possible, memory_state, carry_state)

    model = Model(
        inputs={
            "friends": friends,
            "team": team,
            "shop": shop,
            "possible": possible,
            "memory_state": memory_state,
            "carry_state": carry_state,
        },
        outputs={
            "action_logits": action_logits,
            "final_mem_state": final_mem_state,
            "final_carry_state": final_carry_state,
            "action": action,
        },
        name=name,
    )

    return model
