from pathlib import Path

import torch


class Inference:
    def __init__(self, model_cls, log_path, device="cuda"):
        log_path = Path(log_path)
        self.model = self.load_model(model_cls, log_path)
        self.device = device

    def load_model(self, model_cls, log_path):
        config_path = str(log_path / "config.txt")
        with open(config_path, "r") as f:
            config_dic = eval(f.read())

        # TODO: create model with model parameters (strored in the config file)
        model = model_cls()
        model.load_state_dict(torch.load(log_path / "model.pth"))

    def __call__(self, x):
        # TODO: add prepcossing and postprocessing
        x = x.to(self.device)
        with torch.no_grad():
            out = self.model(x)

        return out
