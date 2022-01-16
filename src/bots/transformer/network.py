import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import (
    Embedding,
    Layer,
    LayerNormalization,
    Dropout,
    Dense,
    Add,
    Concatenate,
    GlobalAveragePooling1D,
    Flatten,
)
from tensorflow.keras import Sequential, Input, Model

# POSITION ENCODING
def get_angles(pos, i, d_model):
    angle_rates = 1 / np.power(10000, (2 * (i // 2)) / np.float32(d_model))
    return pos * angle_rates


def positional_encoding(position, d_model):
    angle_rads = get_angles(
        np.arange(position)[:, np.newaxis], np.arange(d_model)[np.newaxis, :], d_model
    )
    angle_rads[:, 0::2] = np.sin(angle_rads[:, 0::2])
    angle_rads[:, 1::2] = np.cos(angle_rads[:, 1::2])

    pos_encoding = angle_rads[np.newaxis, ...]

    return tf.cast(pos_encoding, dtype=tf.float32)


# ATTENTION
def scaled_dot_product_attention(q, k, v, mask):
    matmul_qk = tf.matmul(q, k, transpose_b=True)
    dk = tf.cast(tf.shape(k)[-1], tf.float32)
    scaled_attention_logits = matmul_qk / tf.math.sqrt(dk)
    if mask is not None:
        scaled_attention_logits += mask * -1e9
    attention_weights = tf.nn.softmax(scaled_attention_logits, axis=-1)
    output = tf.matmul(attention_weights, v)
    return output, attention_weights


# SIMPLE FEED FORWARD
def point_wise_feed_forward_network(d_model, dff):
    return Sequential([Dense(dff, activation="relu"), Dense(d_model)])


# MULTI HEAD ATTENTION
class MultiHeadAttention(Layer):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttention, self).__init__()
        self.num_heads = num_heads
        self.d_model = d_model

        assert d_model % self.num_heads == 0

        self.depth = d_model // self.num_heads

        self.wq = Dense(d_model)
        self.wk = Dense(d_model)
        self.wv = Dense(d_model)

        self.dense = Dense(d_model)

    # method to split the layers into different heads
    def split_heads(self, x, batch_size):
        x = tf.reshape(x, (batch_size, -1, self.num_heads, self.depth))
        return tf.transpose(x, perm=[0, 2, 1, 3])

    def call(self, v, k, q, mask):
        batch_size = tf.shape(q)[0]
        # feed through dense layer
        q = self.wq(q)
        k = self.wk(k)
        v = self.wv(v)

        # split out into the number of heads passed through
        q = self.split_heads(q, batch_size)
        k = self.split_heads(k, batch_size)
        v = self.split_heads(v, batch_size)

        scaled_attention, attention_weights = scaled_dot_product_attention(
            q, k, v, mask
        )

        scaled_attention = tf.transpose(scaled_attention, perm=[0, 2, 1, 3])

        # recombine all of the heads of attention
        concat_attention = tf.reshape(scaled_attention, (batch_size, -1, self.d_model))

        output = self.dense(concat_attention)

        return output, attention_weights


# ENCODER
class EncoderLayer(Layer):
    def __init__(self, d_model, num_heads, dff, rate=0.1):
        super(EncoderLayer, self).__init__()

        self.mha = MultiHeadAttention(d_model, num_heads)
        self.ffn = point_wise_feed_forward_network(d_model, dff)

        self.layernorm1 = LayerNormalization(epsilon=1e-6)
        self.layernorm2 = LayerNormalization(epsilon=1e-6)

        self.dropout1 = Dropout(rate)
        self.dropout2 = Dropout(rate)

    def call(self, x, training, mask):

        # passes x as all inputs to the multihead attention then normalizes
        attn_output, _ = self.mha(x, x, x, mask)
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.layernorm1(x + attn_output)

        # passes the outputs through a feed forward network then normalizes
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output, training=training)
        out2 = self.layernorm2(out1 + ffn_output)

        return out2


class TransformerModel(Model):
    def __init__(self, emb_dim=32, num_heads=2, dropout=0.1):
        super(TransformerModel, self).__init__()

        self.pos_enc = positional_encoding(5, emb_dim)

        # Animal Embeddings (used by shop and friends)
        self.animal_type_emb = Embedding(66, emb_dim)
        self.animal_hp_emb = Embedding(50, emb_dim)
        self.animal_dmg_emb = Embedding(50, emb_dim)
        self.animal_thp_emb = Embedding(50, emb_dim)
        self.animal_tdmg_emb = Embedding(50, emb_dim)
        self.animal_exp_emb = Embedding(6, emb_dim)
        self.animal_effect_emb = Embedding(12, emb_dim)

        self.food_emb = Embedding(18, emb_dim)

        # util layer
        self.add = Add()
        self.avg_pool = GlobalAveragePooling1D()
        self.dropout = Dropout(dropout)
        self.concat = Concatenate()
        self.flatten = Flatten()

        # Encoder layers
        self.encoder1 = EncoderLayer(
            d_model=emb_dim,
            num_heads=num_heads,
            dff=emb_dim * 4,
            rate=dropout,
        )
        self.encoder2 = EncoderLayer(
            d_model=emb_dim,
            num_heads=num_heads,
            dff=emb_dim * 4,
            rate=dropout,
        )

        # Final Dense network

        self.o1 = Dense(512, activation="relu")
        self.o2 = Dense(256, activation="relu")
        self.out = Dense(69, activation="softmax", name="output")

    def call(self, animals, shop_an, shop_food, team, possible):
        an_emb_t = self.animal_type_emb(animals[..., 0])
        an_emb_e = self.animal_effect_emb(animals[..., 1])
        an_emb_ex = self.animal_exp_emb(animals[..., 2])
        an_emb_h = self.animal_hp_emb(animals[..., 3])
        an_emb_d = self.animal_dmg_emb(animals[..., 4])
        an_emb_th = self.animal_thp_emb(animals[..., 5])
        an_emb_td = self.animal_tdmg_emb(animals[..., 6])

        s_an_emb_t = self.animal_type_emb(shop_an[..., 0])
        s_an_emb_e = self.animal_effect_emb(shop_an[..., 1])
        s_an_emb_ex = self.animal_exp_emb(shop_an[..., 2])
        s_an_emb_h = self.animal_hp_emb(shop_an[..., 3])
        s_an_emb_d = self.animal_dmg_emb(shop_an[..., 4])
        s_an_emb_th = self.animal_thp_emb(shop_an[..., 5])
        s_an_emb_td = self.animal_tdmg_emb(shop_an[..., 6])

        s_food_emb_1 = self.food_emb(shop_food[..., 0])
        s_food_emb_2 = self.food_emb(shop_food[..., 1])

        a_x = self.add(
            [
                self.pos_enc,
                an_emb_t,
                an_emb_e,
                an_emb_h,
                an_emb_d,
                an_emb_th,
                an_emb_td,
                an_emb_ex,
            ]
        )
        sa_x = self.add(
            [
                s_an_emb_t,
                s_an_emb_e,
                s_an_emb_h,
                s_an_emb_d,
                s_an_emb_th,
                s_an_emb_td,
                s_an_emb_ex,
            ]
        )

        a_x = self.encoder1(a_x, mask=None)
        a_x = self.encoder2(a_x, mask=None)
        a_x = self.avg_pool(a_x)
        a_x = self.dropout(a_x)
        a_x = self.flatten(a_x)

        sa_x = self.flatten(sa_x)

        mid = self.concat([a_x, sa_x, s_food_emb_1, s_food_emb_2, team, possible])

        out = self.dropout(mid)
        out = self.o1(out)
        out = self.dropout(out)
        out = self.o2(out)
        return self.out(out)


def make_model(name):

    animals = Input(shape=(5, 7))
    shop_an = Input(shape=(5, 7))
    shop_food = Input(shape=(2))
    team = Input(shape=(5))
    possible = Input(shape=(69))

    prob_dist = TransformerModel(emb_dim=32, num_heads=4)(
        animals, shop_an, shop_food, team, possible
    )

    model = Model(
        inputs={
            "animals": animals,
            "shop_an": shop_an,
            "shop_food": shop_food,
            "team": team,
            "possible": possible,
        },
        outputs={"prob_dist": prob_dist},
        name=name,
    )

    return model
