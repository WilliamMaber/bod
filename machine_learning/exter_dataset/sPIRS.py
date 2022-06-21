import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/bshmueli/SPIRS"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'SPIRS',url)




def get_data():
    non_sarcastic_path = get_path(dir_fs, 'SPIRS',"SPIRS-non-sarcastic-ids.csv")
    sarcastic_path = get_path(dir_fs, 'SPIRS',"SPIRS-sarcastic-ids.csv")