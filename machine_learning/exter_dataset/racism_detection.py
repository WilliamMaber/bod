url = "https://github.com/angelamarpaung99/racism-detection"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'racism-detection',url)

def get_data():
    path = get_path(dir_fs, 'racism-detection',"dataset_racism.csv")
    data =  random.choice(CSV(path))
    if data["label"] == "Non_R":
        pass
    else:
        pass
    # tokens, mask, c = tokenizer(data["tweets"] "Text", "unknown", None)