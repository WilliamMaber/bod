import os
from machine_learning.exter_dataset.uitls.download import git_download

url = "https://github.com/Supermaxman/vaccine-lies/tree/master/covid19"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'coVaxLies_v2',url)