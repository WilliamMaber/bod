import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


from transformers import BertTokenizer
url = "https://github.com/JasonObeid/Chart2Text"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Chart2Text',url)

def get_data():
    
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    # tokens, mask, c = tokenizer(data["text"], "Text", "unknown", None)
    pass