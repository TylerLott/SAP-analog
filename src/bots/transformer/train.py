import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import tensorflow as tf
import numpy as np
from tensorflow.keras.callbacks import TensorBoard, ModelCheckpoint
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import Sequence
from src.bots.transformer.network import make_model
from data_collecter.sequences.create_sequences import create_for_transform
from random import shuffle


def run():
    dataset = create_for_transform()
    print(f"Rows of data loaded: {len(dataset)}")

    def data_gen(train=True):
        rows = len(dataset)
        if train:
            rows = rows[: len(rows) * 0.9]
        if not train:
            rows = rows[len(rows) * 0.9 :]
        for i in rows:
            inps = {
                "animals": i[:35].reshape(5, 7),
                "shop_an": i[35:70].reshape(5, 7),
                "shop_food": i[70:72],
                "team": i[72:77],
                "possible": i[77:-69],
            }
            outs = {"prob_dist": i[-69:]}
            yield inps, outs

    def get_dataset(data_genny, train=True):
        dataset = tf.data.Dataset.from_generator(
            data_genny,
            output_signature=(
                {
                    "animals": tf.TensorSpec(shape=(5, 7), dtype=tf.int32),
                    "shop_an": tf.TensorSpec(shape=(5, 7), dtype=tf.int32),
                    "shop_food": tf.TensorSpec(shape=(2), dtype=tf.int32),
                    "team": tf.TensorSpec(shape=(5), dtype=tf.float32),
                    "possible": tf.TensorSpec(shape=(69), dtype=tf.float32),
                },
                {"prob_dist": tf.TensorSpec(shape=(69), dtype=tf.float32)},
            ),
        )
        dataset = dataset.batch(64)
        return dataset

    train_dataset = get_dataset(data_gen)
    valid_dataset = get_dataset(data_gen(train=False))

    # friends = dataset[:, :35].reshape((-1, 5, 7))
    # shop_an = dataset[:, 35:70].reshape((-1, 5, 7))
    # shop_food = dataset[:, 70:72]
    # team = dataset[:, 72:77]
    # possible = dataset[:, 77:-69]
    # labels = dataset[:, -69:]

    model = make_model("test_transformer")
    loss = CategoricalCrossentropy()
    opt = Adam(learning_rate=0.0003)

    tensorboard = TensorBoard(
        log_dir="./train/transformer/test_transformer",
        update_freq="batch",
        write_graph=True,
    )

    tensorboard.set_model(model)

    # checkpoint = ModelCheckpoint(
    #     filepath="./train/transformer/models/best_val_loss",
    #     monitor="val_loss",
    #     verbose=0,
    #     mode="min",
    #     save_freq="epoch",
    #     save_weights_only=True,
    # )

    # model.load_weights("./train/transformer/models/best_val_loss")

    model.summary()

    # inputs = {
    #     "animals": friends,
    #     "shop_an": shop_an,
    #     "shop_food": shop_food,
    #     "team": team,
    #     "possible": possible,
    # }

    # model.fit(
    #     x=inputs,
    #     y=labels,
    #     validation_split=0.1,
    #     batch_size=64,
    #     epochs=200,
    #     shuffle=True,
    #     callbacks=[tensorboard, checkpoint],
    # )

    train_loss_res = []
    train_acc_res = []
    valid_loss_res = []
    valid_acc_res = []

    num_epochs = 200

    for epoch in range(num_epochs):

        epoch_loss_avg = tf.keras.metrics.Mean()
        epoch_acc = tf.keras.metrics.CategoricalAccuracy()
        valid_loss_avg = tf.keras.metrics.Mean()
        valid_acc = tf.keras.metrics.CategoricalAccuracy()

        step = 1
        # training loop
        for x, y in iter(train_dataset):
            with tf.GradientTape() as tape:
                out = model(x, training=True)
                loss_val = loss(y["prob_dist"], out["prob_dist"])

            grads = tape.gradient(loss_val, model.trainable_weights)
            opt.apply_gradients(zip(grads, model.trainable_weights))

            epoch_loss_avg.update_state(loss_val)
            epoch_acc.update_state(y["prob_dist"], model(x, training=True)["prob_dist"])

            if step % 20 == 0:
                print(
                    f"Training loss at step {step} / {int(len(dataset)//64)}: {loss_val:.4f}"
                )

            step += 1

        train_loss_res.append(epoch_loss_avg.result())
        train_acc_res.append(epoch_acc.result())

        # valid loop
        for x, y in iter(valid_dataset):
            out = model(x, training=False)
            loss_val = loss(y["prob_dist"], out["prob_dist"])

            valid_loss_avg.update_state(loss_val)
            valid_acc.update_state(
                y["prob_dist"], model(x, training=False)["prob_dist"]
            )

        valid_loss_res.append(valid_loss_avg.result())
        valid_acc_res.append(valid_acc.result())

        print(
            f"Epoch {epoch}: Loss {epoch_loss_avg.result():.3f}, Acc {epoch_acc.result():.3f} -- Validation: Loss {valid_loss_avg.result():.3f}, Acc {valid_acc.result():.3f}"
        )
        if epoch % 5 == 0:
            print("saving weights...")
            fp = f"./train/trainsformer/models/custom_train_vloss_{valid_loss_avg.result()}_epoch_{epoch}"
            model.save_weights(fp)
