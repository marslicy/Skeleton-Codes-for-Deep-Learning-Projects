# This file contains a list of configuration dictionaries for the experiments.

config_list = [
    {
        "log": {
            # TODO: set the name of this experiment
            "expriment_name": "template",
            "log_dir": "./logs",
            # log files will be saved in log_dir/expriment_name+timestamp
            # e.g., log_dir/template_2024-01-01_00-00-00
            # model checkpoints will be saved in log_dir/template_2024-01-01_00-00-00/model.pth
        },
        "data": {
            "data_path": "path/to/data",
            # TODO: add any other data related parameters here
        },
        "train": {
            "device": "cuda",
            "val_every_n": 100,
            "print_every_n": 25,
            "lr": 1e-4,
            "batch_size_train": 4,
            "batch_size_val": 8,
            "epochs": 100,
            "early_stopping": 10,
            # TODO: add any other training related parameters here
        },
        "model": {
            # TODO: add any other model related parameters here
        },
    },
    # TODO: add more experiments here
]
