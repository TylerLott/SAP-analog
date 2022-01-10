from data_collecter.agg_data import run
from src.bots.pytorch_model.CustomNetwork import CustomNetwork
import torch
from torch.utils.data import DataLoader
from datetime import datetime
from torch.utils.tensorboard import SummaryWriter

from src.bots.pytorch_model.Dataset import SAPDataset_train, SAPDataset_valid

# should be batched here
train_loader = DataLoader(
    SAPDataset_train(), batch_size=64, shuffle=True, num_workers=0
)
validation_loader = DataLoader(
    SAPDataset_valid(), batch_size=64, shuffle=True, num_workers=0
)

model = CustomNetwork(888, 69)

loss_fn = torch.nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)


def train_one_epoch(epoch_index, tb_writer):
    running_loss = 0.0
    last_loss = 0.0

    for i, data in enumerate(train_loader):
        input, label = data

        optimizer.zero_grad()

        out = model(input)

        loss = loss_fn(out, label)
        loss.backward()

        optimizer.step()

        running_loss += loss.item()
        if i % 1000 == 999:
            last_loss = running_loss / 1000
            print(f"| batch: {i+1} | loss: {last_loss} |")
            tb_x = epoch_index * len(train_loader) + i + 1
            tb_writer.add_scaler("Loss/train", last_loss, tb_x)
            running_loss = 0.0


def train(epochs=1000):

    time_stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    writer = SummaryWriter(f"./train/custDQN/tensorboard/run_{time_stamp}")

    EPOCHS = epochs
    best_vloss = 1_000_000.0

    for epoch in range(EPOCHS):
        print(f"EPOCH: {epoch+1}")

        model.train(True)
        avg_loss = train_one_epoch(epoch, writer)

        model.train(False)
        running_vloss = 0.0
        for i, vdata in enumerate(validation_loader):
            vinputs, vlabels = vdata
            vout = model(vinputs)
            vloss = loss_fn(vout, vlabels)
            running_vloss += vloss
        avg_vloss = running_vloss / (i + 1)
        print(f"LOSS train {avg_loss} valid {avg_vloss}")
        writer.add_scalars(
            "Training vs. Validation loss",
            {"Training": avg_loss, "Validation": avg_vloss},
            epoch + 1,
        )
        writer.flush()

        if avg_vloss < best_vloss:
            best_vloss = avg_vloss
            model_path = f"./train/custDQN/model_{time_stamp}_{epoch}"
            torch.save(model.state_dict(), model_path)
