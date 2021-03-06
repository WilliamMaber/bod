import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from transformers import BertTokenizer

url = "https://github.com/surge-ai/toxicity"

dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'toxicity',url)




def get_data():
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    toxicity = get_path(dir_fs, 'toxicity',"toxicity_en.csv")
    data = random.choice(CSV(toxicity))
    if data["is_toxic"]== "Toxic":
        boolen_toxicity = True
    elif data["is_toxic"]== "Not Toxic":
        boolen_toxicity = False
    inputs = tokenizer(data["text"], return_tensors="pt")
    return {
        "input":inputs,
        "boolen_toxicity":boolen_toxicity
    }
    