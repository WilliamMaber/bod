import os
from machine_learning.exter_dataset.uitls.decode_data import list_file
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/kinit-sk/medical-misinformation-dataset"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'mphasis',url)


def get_data():
    mphasis = get_path(dir_fs, 'mphasis',"mphasis/sample_data")
    paths = list_file(mphasis)
    print(paths)
    pass
