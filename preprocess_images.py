# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import random
import sys
import numpy as np
from sten import Sten
import os.path
from tqdm.auto import tqdm, trange

NUM_FILES = int(sys.argv[1])

st = Sten(3)
done = []

# +
path = os.getcwd() + '/data/set1'
num_files_set1 = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])

path = os.getcwd() + '/data/set2'
num_files_set2 = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
# -

i = 0
for _ in trange(NUM_FILES, desc='File', leave=True):
    set1File = random.randint(1,num_files_set1)
    set2File = random.randint(1,num_files_set2)
    name = str(set1File) + '.' + str(set2File)
    if name not in done:
        encImg = st.encode("./data/set1/{}.jpg".format(set1File), "./data/set2/{}.jpg".format(set2File), "./encodedArray/{}.npy".format(i))
        decImg = st.decode("./encodedArray/{}.npy".format(i), "./decodedArray/{}.npy".format(i))
        done.append(name)
        i += 1
print(len(done))
