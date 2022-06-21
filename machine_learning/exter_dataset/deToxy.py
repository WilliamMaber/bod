from sysconfig import get_path
from git import Repo
import os
import random
from machine_learning.exter_dataset.uitls.download import git_download
url = "https://github.com/sreyan88/toxicity-detection-in-spoken-utterances"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'deToxy',url)


def get_data():
    train_split = get_path(dir_fs, 'deToxy',"train.csv")
    test_split = get_path(dir_fs, 'deToxy',"test.csv")
    valid_split = get_path(dir_fs, 'deToxy',"valid.csv")
    trigger_test = get_path(dir_fs, 'deToxy',"trigger_test.csv")
    valid_split = get_path(dir_fs, 'deToxy',"trigger_test.csv")
    path = random.choice([valid_split,test_split,train_split,trigger_test])