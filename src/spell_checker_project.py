# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 12:49:07 2025
@author: sudha
"""

# spell checker project
import kagglehub
import kagglehub
import os
import re 
import matplotlib.pyplot as plt
from tqdm import tqdm
import json

# Download latest version
path = kagglehub.dataset_download("bittlingmayer/spelling")

print("Path to dataset files:", path)

dir_path = r"C:\Users\sudha\.cache\kagglehub\datasets\bittlingmayer\spelling\versions\2"

# creating consolidated dataset
consolidated_txt = ""

for text_file_name in os.listdir(dir_path):
    if text_file_name == "big":
        txt_file_path = os.path.join(dir_path,text_file_name)
        with open(txt_file_path,"r") as f:
            curr_txt = f.read()
            f.close()
    limiter = "-------------------------"
    consolidated_txt += limiter
    consolidated_txt += curr_txt
    
consolidated_dataset_path = os.path.join(dir_path,"consolidated_txt.txt")
big_txt_path = os.path.join(dir_path,"big.txt")

with open(consolidated_dataset_path,"w") as f:
    f.write(consolidated_txt)
    f.close()

# text cleaning
with open(big_txt_path ,"r") as f:
    
    lines = f.readlines()
    f.close()
    
    
pure_words = []
for line in lines:
    print(line)
    pure_words += re.findall("\w+", line)
    
pattern = "[a-zA-Z]+"
pure_words = re.findall(pattern, big_txt)
pure_words_set = list(set(pure_words))
len(pure_words)

# probablity distribution
word_prob = dict()
for word in pure_words_set:
    word_prob[word] = pure_words.count(word)/len(pure_words)

with open(r"C:\Users\sudha\Desktop\dhanush\Personal DS\NLP/word_prob_json.json","w",encoding="utf-8") as f:
    json.dump(word_prob,f,indent = 2)
    f.close()
