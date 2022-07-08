url =  "https://github.com/mathfather/Hate-Speech-Detection-For-COSC586"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Hate-Speech-Detection-For-COSC586',url)



def get_data():
    join_testset_levelb = get_path(dir_fs, 'Hate-Speech-Detection-For-COSC586',"join_testset_levelb.csv")
    data = random.choice(CSV(join_testset_levelb))
    if data["subtask_b"] == "TIN":
        pass
    elif data["subtask_b"] == "UNT":
        pass
    # tokens, mask, c = tokenizer(data["tweet"] , "Text", "unknown", None)
