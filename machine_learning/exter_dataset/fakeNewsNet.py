import os
import random
from machine_learning.data_url import load_url
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.service.twitter import tweet_downloader
from machine_learning.service_scrap.modules.retrieval import Memory_Handler
url = "https://github.com/KaiDMML/FakeNewsNet"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'FakeNewsNet',url)



def get_data():
    db = Memory_Handler()
    file = random.choice( ["gossipcop_fake.csv","gossipcop_real.csv","politifact_fake.csv","politifact_real.csv"])
    path  = get_path(dir_fs, 'FakeNewsNet',file)
    data = random.choice(CSV(path))
    tweet_ids = random.choice(data["tweet_ids"].split(" "))
    isfake = "fake" in file
    text = load_url(data["news_url"])
    for tweet_id in tweet_ids:
        text = tweet_downloader(tweet_id)