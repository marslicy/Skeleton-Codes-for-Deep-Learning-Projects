# Skeleton Codes for Deep Learning Projects (Pytorch)
- This repo contains skeleton codes of deep learning projects.
- It may contain bugs or unreasonable designs, which will be fixed or improved when I find them.
- Contain a git precommit config file which is set for black formating (install the precommit use `pre-commit install`).

## Training
- Execute `train.py` directly, using the parameters set in `config.py`.
- You can set multiple groups of parameters in the list of dictionaries in the file.
- Before training it will create a folder `.\logs`(can be changed in `config.py`), and a subfolder with name `expriment_name+timestamp`.
- The config used in this training process will be stored in the subfolder as file `config.txt`
- The best model will be stored in the subfolder as file `model.pth`.
- The training style is leave-one-out validation and contains an early-stopping mechanism.

## Inference
- Implement the Inference class in `./infer/inference.py`
- It will load `model.pth` from the log directory and use the parameters saved in `config.txt` in the same folder.
- Implement `./test.py` to test the model

## Other information
- If the model contains a lot of components, add Python files for these components in the directory`./model`.
- If a customized iterator that is different than the test dataloader is needed, please put these files into the directory `./inference.`
- If some Python scripts are not expected to be committed, rename them with the string `utr_` at the beginning, e.g., `utr_temp.py.`