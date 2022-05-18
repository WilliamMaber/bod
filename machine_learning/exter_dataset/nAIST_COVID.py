import os
from git import Repo
url = "https://github.com/sociocom/covid19_dataset"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'nAIST_COVID')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
