import tensorflow as tf
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.callbacks import Adam
from .ModifiedTensorboard import ModifiedTensorBoard
from collections import deque

import time

### Constants ###
MODEL_NAME = "test"
REPLAY_MEMORY_SIZE = 50_000


class DQNAgent:
    def __init__(self):
        self.model = self.createModel()

        self.target_model = self.createModel()
        self.target_model.set_weights(self.model.get_weights())

        self.replay_memory = deque(maxlen=REPLAY_MEMORY_SIZE)
        self.tensorboard = ModifiedTensorBoard(
            log_dir=f"logs/{MODEL_NAME}-{int(time.time())}"
        )
        self.target_update_counter = 0

    def createModel(self):
        model = Sequential()
        model.add(Dense(256, activation="relu"))
        model.add(Dense(512, activation="relu"))
        model.add(Dense(512, activation="relu"))
        model.add(Dropout(0.2))
        model.add(Dense(512, activation="relu"))
        model.add(Dense(77))
