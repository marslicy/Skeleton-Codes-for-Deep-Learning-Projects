import torch
from torch.utils.data import DataLoader

from infer.inference import Inference


def test(test_loader, infer_obj):
    device = infer_obj.device
    for i, batch in enumerate(test_loader):
        # TODO: 1. resolove the batch: _, _ = batch

        # TODO: 2. move the batch to the device

        with torch.no_grad():
            # TODO: 3. forward pass

            # TODO: 4. calculate evaluation metrics

            pass


if __name__ == "__main__":
    from dataset import MyDataset

    # TODO: create the test dataset
    test_set = MyDataset("data/path", "test")
    test_loader = DataLoader(test_set, batch_size=1, shuffle=False)

    # TODO: create the inference object
    infer_obj = Inference()

    test(test_loader, infer_obj)
