url = "https://github.com/isomap/factedit"
import os
from machine_learning.exter_dataset.uitls.decode_data import load_pickle
from machine_learning.exter_dataset.uitls.download import git_download
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'factedit',url)


def get_data():
    pass