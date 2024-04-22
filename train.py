import os
import time

import torch
from tensorboardX import SummaryWriter
from torch.utils.data import DataLoader

from dataset import MyDataset
from model.net import Net


def train(config):
    model, train_loader, val_loader, logdir = get_model_dataloader_logdir(config)
    save_config(config, logdir)

    writer = SummaryWriter(logdir)

    device = config["train"]["device"]

    model.to(device)
    model.train()

    optimizer = torch.optim.Adam(model.parameters(), lr=config["train"]["lr"])

    # TODO: define the loss function
    loss_fn = None

    loss_print = 0
    best_val_loss = float("inf")
    print_every_n = config["train"]["print_every_n"]
    early_stopping = config["train"]["early_stopping"]
    for epoch in range(config["train"]["epoch"]):
        for i, batch in enumerate(train_loader):
            optimizer.zero_grad()

            # TODO: 1. resolove the batch: _, _ = batch

            # TODO: 2. move the batch to the device

            # TODO: 3. forward pass

            # TODO: 4. calculate the loss
            # loss_curr = loss_fn()
            # loss_print += loss_curr.item()

            # TODO: uncomment the following lines
            # loss_curr.backward()
            optimizer.step()

            if (i + 1) % print_every_n == 0:
                loss_print /= print_every_n

                # TODO: log the loss
                print(f"Epoch: {epoch}, Batch: {i}, Loss: {loss_print}")
                writer.add_scalar(
                    "loss/train",
                    loss_print,
                    epoch * len(train_loader) + i,
                )

                loss_print = 0

            if i == len(train_loader) - 1:
                loss_print = 0

            if (i + 1) % config["train"]["val_every_n"] == 0 or i == len(
                train_loader
            ) - 1:
                val_loss = validation(model, val_loader, loss_fn, device)

                # TODO: log the validation loss
                print("======================================================")
                print(f"Epoch {epoch} | Iter {i} | Val Loss {val_loss}")
                print("======================================================")
                writer.add_scalar(
                    "loss/val",
                    val_loss,
                    epoch * len(train_loader) + i,
                )

                if val_loss < best_val_loss:
                    best_val_loss = val_loss
                    torch.save(model.state_dict(), f"{logdir}/model.pth")
                    early_stopping = config["train"]["early_stopping"]
                else:
                    early_stopping -= 1

                if early_stopping == 0:
                    return  # early stopping


def validation(model, val_loader, loss_fn, device):
    model.eval()
    loss = 0
    with torch.no_grad():
        for i, batch in enumerate(val_loader):
            # TODO: 1. resolove the batch: _, _ = batch

            # TODO: 2. move the batch to the device

            # TODO: 3. forward pass

            # TODO: 4. calculate the loss
            # loss += loss_fn()

            # TODO: May save the output of the model for further analysis
            pass

    model.train()

    return loss / len(val_loader)


def get_model_dataloader_logdir(config):
    # TODO: modify this function to return the model, dataset and expriment_name
    model = Net()

    train_set = MyDataset(config["data"]["data_path"], "train")
    train_loader = DataLoader(
        train_set, batch_size=config["train"]["batch_size_train"], shuffle=True
    )

    val_set = MyDataset(config["data"]["data_path"], "val")
    val_loader = DataLoader(
        val_set, batch_size=config["train"]["batch_size_val"], shuffle=True
    )

    expriment_name = config["expriment_name"] + time.strftime(
        "_%Y-%m-%d_%H-%M-%S", time.localtime()
    )

    logdir = config["log"]["log_dir"]
    logdir = f"{logdir}/{expriment_name}"
    os.makedirs(logdir, exist_ok=True)

    return model, train_loader, val_loader, logdir


def save_config(config, log_dir):
    with open(f"{log_dir}/config.txt", "w") as f:
        f.write(str(config))


if __name__ == "__main__":
    from config import config_list

    for config_dict in config_list:
        train(config_dict)
