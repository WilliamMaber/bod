from git import Repo
import os
from machine_learning.exter_dataset.uitls.download import git_download

url = "https://github.com/FakeNewsChallenge/fnc-1"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'fnc-1',url)


def get_data():
    pass