from pathlib import Path

from torch.utils.data import Dataset


class MyDataset(Dataset):
    # TODO: change the name of this class and implement methods
    def __init__(self, data_path, split):
        if split not in ["train", "val", "test"]:
            raise ValueError(
                "split must be either 'train', 'val' or 'test', but got {}".format(
                    split
                )
            )

        super(MyDataset, self).__init__()
        self.data_path = Path(data_path)

    def __len__(self):
        pass

    def __getitem__(self, idx):
        pass

    # TODO: add any other methods here only used within this dataset
