import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV, de_zip 
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from transformers import BertTokenizer

url = "https://github.com/HannahKirk/Hatemoji"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Hatemoji',url)
de_zip(dir_fs,'Hatemoji',"data/rotoedit.tar.bz2")
de_zip(dir_fs,'Hatemoji',"data/webedit.tar.bz2")

def get_data():
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    if random.choice([True,False]):
        # HatemojiCheck
        HatemojiBuild_test = get_path(dir_fs, 'Hatemoji',"HatemojiBuild/test.csv")
        HatemojiBuild_train = get_path(dir_fs, 'Hatemoji',"HatemojiBuild/train.csv")
        HatemojiBuild_validation = get_path(dir_fs, 'Hatemoji',"HatemojiBuild/validation.csv")
        path = random.choices([HatemojiBuild_test,HatemojiBuild_train,HatemojiBuild_validation])
        data = random.choices(CSV(path))
        if data["target"] == "":
            pass
        if data["functionality"] == "":
            pass
        if data["set"] == "":
            pass
        if data["label_gold"] == "":
            pass
        if data["unrealistic_flags"] == "":
            pass
        if data["included_in_test_suite"] == "":
            pass
        
        inputs = tokenizer(data["text"], return_tensors="pt")
    else:
        # HatemojiBuild
        HatemojiCheck_test = get_path(dir_fs, 'Hatemoji',"HatemojiCheck/test.csv")
        data = random.choices(CSV(HatemojiCheck_test))
        data["matched_text"]

    