from src.bots.pytorch_model.autoencoder.Network import AutoEncoder
import torch as th
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from datetime import datetime

from src.bots.pytorch_model.Dataset2 import SAPDataset_train2, SAPDataset_valid2

device = th.device("cuda:0" if th.cuda.is_available() else "cpu")

# should be batched here
train_loader = DataLoader(
    SAPDataset_train2(), batch_size=512, shuffle=True, num_workers=2
)
validation_loader = DataLoader(
    SAPDataset_valid2(), batch_size=512, shuffle=True, num_workers=2
)

model = AutoEncoder(84, 8)
model.to(device)

loss_fn = th.nn.MSELoss()

optimizer = th.optim.Adam(model.parameters(), lr=0.001)


def train_one_epoch(idx, tb_writer):
    running_loss = 0.0
    last_loss = 0.0

    for i, data in enumerate(train_loader):
        f, _, _, _ = data
        f = f[:, :84]
        f = f.to(device)

        optimizer.zero_grad()

        out = model(f)

        loss = loss_fn(out, f)
        loss.backward()

        optimizer.step()

        running_loss += loss.item()

        if i % 10 == 9:
            last_loss = running_loss / 10
            print(f"| batch: {i+1} | loss: {last_loss} |")
            tb_x = idx * len(train_loader) + i + 1
            tb_writer.add_scalar("Loss/train", last_loss, tb_x)
            running_loss = 0.0
    return last_loss


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
            f, _, _, _ = vdata
            f = f[:, :84]
            f = f.to(device)
            vout = model(f)
            vloss = loss_fn(vout, f)

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
            model_path_enc = f"./train/custDQN/autoencoder_enc_{time_stamp}_{epoch}"
            model_path_dec = f"./train/custDQN/autoencoder_dec_{time_stamp}_{epoch}"
            model.save_enc(model_path_enc)
            model.save_dec(model_path_dec)
