import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/snigdhac/StoryComprehension_EMNLP"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'StoryComprehension_EMNLP',url)


def get_data():
    pass