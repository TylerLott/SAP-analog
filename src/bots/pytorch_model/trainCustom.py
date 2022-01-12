from src.bots.pytorch_model.CustomNetwork import CustomNetwork
import torch
from torch.utils.data import DataLoader
from datetime import datetime
from torch.utils.tensorboard import SummaryWriter

from src.bots.pytorch_model.Dataset import SAPDataset_train, SAPDataset_valid

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# should be batched here
train_loader = DataLoader(
    SAPDataset_train(), batch_size=512, shuffle=True, num_workers=2
)
validation_loader = DataLoader(
    SAPDataset_valid(), batch_size=512, shuffle=True, num_workers=2
)

model = CustomNetwork(888, 69)
model.to(device)

loss_fn = torch.nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)


def train_one_epoch(epoch_index, tb_writer):
    running_loss = 0.0
    last_loss = 0.0
    train_acc = 0.0

    for i, data in enumerate(train_loader):
        input, label = data
        input = input.to(device)
        label = label.to(device)

        optimizer.zero_grad()

        out = model(input)

        loss = loss_fn(out, label)
        loss.backward()

        optimizer.step()

        probs = torch.softmax(out, dim=1)
        winners = probs.argmax(dim=1)
        label_winners = label.argmax(dim=1)
        correct = winners == label_winners
        train_acc += correct.sum().float() / float(label_winners.size(0))

        running_loss += loss.item()

        if i % 10 == 9:
            last_loss = running_loss / 10
            print(
                f"| batch: {i+1} | loss: {last_loss} | accuracy: {100 * (train_acc / 10):.2f}%"
            )
            tb_x = epoch_index * len(train_loader) + i + 1
            tb_writer.add_scalar("Loss/train", last_loss, tb_x)
            tb_writer.add_scalar("Acc/train", train_acc / 10, tb_x)
            running_loss = 0.0
            train_acc = 0.0
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
        train_vacc = 0.0
        # for i, vdata in enumerate(validation_loader):
        #     vinputs, vlabels = vdata
        #     vinputs = vinputs.to(device)
        #     vlabels = vlabels.to(device)
        #     vout = model(vinputs)
        #     vloss = loss_fn(vout, vlabels)
        #     vprobs = torch.softmax(vout, dim=1)
        #     vwinners = vprobs.argmax(dim=1)
        #     vlabel_winners = vlabels.argmax(dim=1)
        #     correct = vwinners == vlabel_winners
        #     train_vacc += correct.sum().float() / float(vlabel_winners.size(0))
        #     running_vloss += vloss
        # avg_vloss = running_vloss / (i + 1)
        # print(
        #     f"LOSS train {avg_loss} valid {avg_vloss} valid_acc {100 *(train_vacc / i):.2f}%"
        # )
        # writer.add_scalars(
        #     "Training vs. Validation loss",
        #     {"Training": avg_loss, "Validation": avg_vloss},
        #     epoch + 1,
        # )
        # writer.flush()

        # if avg_vloss < best_vloss:
        #     best_vloss = avg_vloss
        model_path = f"./train/custDQN/model_full_{time_stamp}_{epoch}"
        torch.save(model.state_dict(), model_path)
