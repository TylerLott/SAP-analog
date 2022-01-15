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

    friends = dataset[:, :35].reshape((-1, 5, 7))
    shop_an = dataset[:, 35:70].reshape((-1, 5, 7))
    shop_food = dataset[:, 70:72]
    team = dataset[:, 72:77]
    possible = dataset[:, 77:-69]
    labels = dataset[:, -69:]

    model = make_model("test_transformer")
    loss = CategoricalCrossentropy()
    opt = Adam(learning_rate=0.001)

    tensorboard = TensorBoard(
        log_dir="./train/transformer/test_transformer",
        update_freq="batch",
        write_graph=False,
    )
    checkpoint = ModelCheckpoint(
        filepath="/train/transformer/models/best_model",
        monitor="val_loss",
        verbose=0,
        mode="min",
        save_freq="epoch",
        save_weights_only=True,
    )

    model.compile(loss=loss, optimizer=opt, metrics=["accuracy"])

    model.summary()

    inputs = {
        "animals": friends,
        "shop_an": shop_an,
        "shop_food": shop_food,
        "team": team,
        "possible": possible,
    }

    model.fit(
        x=inputs,
        y=labels,
        validation_split=0.1,
        batch_size=64,
        epochs=200,
        shuffle=True,
        callbacks=[tensorboard, checkpoint],
    )
