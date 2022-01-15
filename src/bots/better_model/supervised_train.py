import tensorflow as tf
import numpy as np
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import Sequence
from src.bots.better_model.network import make_dense, make_model
from data_collecter.sequences.create_sequences import create_flat, create_sequences
from random import shuffle


def test():
    dataset = create_sequences()
    shuffle(dataset)
    print(f"sequences: {len(dataset)}")

    train = np.empty(shape=[1, 10, 163])
    label = np.empty(shape=[1, 69])
    for i in dataset:
        train = np.append(train, i[0][np.newaxis, :, :], axis=0)
        label = np.append(label, i[1][np.newaxis, :], axis=0)

    print(train.shape)
    print(label.shape)

    def batch_generator(x, y, batch_size=10):
        indicies = np.arange(len(x))
        batch = []
        while True:
            np.random.shuffle(indicies)
            for i in indicies:
                batch.append(i)
                if len(batch) == batch_size:
                    yield x[batch, :, :40], x[batch, :, 40:45], x[batch, :, 45:94], x[
                        batch, :, 94:
                    ], y[batch]
                    batch = []

    dataset_gen = batch_generator(train, label, batch_size=10)

    model = make_model("test_net")
    loss = CategoricalCrossentropy(from_logits=True)
    opt = Adam(learning_rate=0.00001)

    EPOCHS = 3
    for epoch in range(EPOCHS):
        print(f"Start of epoch {epoch+1}")
        for step, (friends, team, shop, possible, y) in enumerate(dataset_gen):
            with tf.GradientTape() as tape:
                inputs = {
                    "friends": friends,
                    "team": team,
                    "shop": shop,
                    "possible": possible,
                    "memory_state": tf.zeros([friends.shape[0], 256]),
                    "carry_state": tf.zeros([friends.shape[0], 256]),
                }
                out = model(inputs, training=True)
                move_logits = out["action_logits"]
                loss_val = loss(move_logits, y)
            grads = tape.gradient(loss_val, model.trainable_weights)
            capped_gvs = [tf.clip_by_value(grad, -1, 1) for grad in grads]
            opt.apply_gradients(zip(capped_gvs, model.trainable_weights))

            if step % 100 == 0:
                print(
                    f"| Step {step} | Training loss {float(loss_val)} | action {out['action']} | correct_action {list(np.argmax(y, axis=1))} |"
                )
            if (step + 1) % 1000 == 0:
                break


def test_deep():
    dataset = create_flat()

    def batch_generator(x, y, batch_size=10):
        indicies = np.arange(len(x))
        batch = []
        while True:
            np.random.shuffle(indicies)
            for i in indicies:
                batch.append(i)
                if len(batch) == batch_size:
                    yield x[batch, :40], x[batch, 40:45], x[batch, 45:94], x[
                        batch, 94:
                    ], y[batch]
                    batch = []

    dataset_gen = batch_generator(dataset[:, :-69], dataset[:, -69:], batch_size=10)
    model = make_dense("test")
    loss = CategoricalCrossentropy()
    opt = Adam(learning_rate=0.0001)

    model.compile(loss=loss, optimizer=opt, metrics=["accuracy"])

    inputs = {
        "friends": dataset[:, :40],
        "team": dataset[:, 40:45],
        "shop": dataset[:, 45:94],
        "possible": dataset[:, 94:-69],
    }
    outputs = {"action_logits": dataset[:, -69:]}
    model.fit(
        x=inputs,
        y=outputs,
        validation_split=0.1,
        batch_size=64,
        epochs=2000,
        shuffle=True,
        verbose=2,
    )
