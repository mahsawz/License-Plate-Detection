# %%
import os
import numpy as np

# %%
split = (0.8, 0.1, 0.1)
from os import listdir
from os.path import isfile, join

images_0 = np.array([f for f in listdir('./data/0') if isfile(join('./data/0', f))])
images_1 = np.array([f for f in listdir('./data/1') if isfile(join('./data/1', f))])
images_2 = np.array([f for f in listdir('./data/2') if isfile(join('./data/2', f))])

np.random.shuffle(images_0)
np.random.shuffle(images_1)
np.random.shuffle(images_2)

images_0_split = images_0[:int(len(images_0)*split[0])], images_0[int(len(images_0)*split[0]):int(len(images_0)*split[0]) + int(len(images_0)*split[1])], images_0[int(len(images_0)*split[0]) + int(len(images_0)*split[1]):]
images_1_split = images_1[:int(len(images_1)*split[0])], images_1[int(len(images_1)*split[0]):int(len(images_1)*split[0]) + int(len(images_1)*split[1])], images_1[int(len(images_1)*split[0]) + int(len(images_1)*split[1]):]
images_2_split = images_2[:int(len(images_2)*split[0])], images_2[int(len(images_2)*split[0]):int(len(images_2)*split[0]) + int(len(images_2)*split[1])], images_2[int(len(images_2)*split[0]) + int(len(images_2)*split[1]):]
images_split = [images_0_split, images_1_split, images_2_split]

import shutil
for c in range(3):
    for img in images_split[c][0]:
        shutil.copyfile(join(f'./data/{c}', img), join(f'./correct_data/train/{c}', img))
    for img in images_split[c][1]:
        shutil.copyfile(join(f'./data/{c}', img), join(f'./correct_data/validation/{c}', img))
    for img in images_split[c][2]:
        shutil.copyfile(join(f'./data/{c}', img), join(f'./correct_data/test/{c}', img))
# %%
