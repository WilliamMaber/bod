import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/nguyenvo09/EMNLP2020"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'snopes',url)


def get_data():
    path = get_path(dir_fs, 'some_Like_it_Hoax',"dataset/pages_to_read.txt")