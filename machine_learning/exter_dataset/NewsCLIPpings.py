import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://github.com/g-luo/news_clippings"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'news_clippings',url)



def get_data():
    alisoneroman = get_path(dir_fs, 'news_clippings',"data/alisoneroman.csv")

    pass