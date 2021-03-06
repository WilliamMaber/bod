import os
import random
from machine_learning.exter_dataset.uitls.decode_data import list_file, load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


from transformers import BertTokenizer
url = "https://github.com/cyang03/CHECKED"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'CHECKED',url)


def get_data():
    
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    real_news = get_path(dir_fs, 'CHECKED', "dataset/real_news")
    fake_news = get_path(dir_fs, 'CHECKED', "dataset/fake_news")
    data = list_file(random.choice([real_news,fake_news]))
    data = load_json(random.choice(data))
    for url in data["video_url"]:
        pass
    url = data["pic_url"]
    data["comment_num"]
    data["repost_num"]
    data["like_num"]
    
    data["text"]
    # tokens, mask, c = tokenizer(data["text"], "Text", "unknown", None)
    
    data["id"]
    
    if data["label"] == "real":
        pass
    else:
        pass
        
    # reposts->text
    # reposts->pic_url
    
    