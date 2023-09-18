import pandas as pd 
import os 
from tqdm import tqdm
file = pd.read_csv("imagenet-100.txt", header=None)

original_train_folder = "ILSVRC/Data/CLS-LOC/train"
original_val_folder = "ILSVRC/Data/CLS-LOC/val_folder"

with open("copy-imagenet100.sh", 'w') as f:
    f.write("mkdir -p image/train\n")
    f.write("mkdir -p image/val\n")
    count = 1
    for i in tqdm(file.iloc[:, 0]):
        print(i)
        
        write_str1 = f"cp -r {original_train_folder}/{i} image/train\n"
        write_str2 = f"cp -r {original_val_folder}/{i} image/val\n"
        f.write(write_str1)
        
        f.write(write_str2)
        f.write(f"""echo "{i} ({count} / {len(file.iloc[:, 0])})"\n""")
        count += 1
        