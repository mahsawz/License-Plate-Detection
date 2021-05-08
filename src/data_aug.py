# %%
import cv2
import os
import numpy as np

# %%
# change lighting of image (original dataset)
from os import listdir
from os.path import isfile, join
images_0 = [f for f in listdir('./data/0') if isfile(join('./data/0', f))]
images_1 = [f for f in listdir('./data/1') if isfile(join('./data/1', f))]
images_2 = [f for f in listdir('./data/2') if isfile(join('./data/2', f))]

all_images = [images_0, images_1, images_2]

for c in range(3):
    for img_file in all_images[c]:
        img = cv2.imread(join(f'./data/{c}', img_file))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        avg_v = np.sum(img[:, :, 2]) / (img.shape[0] * img.shape[1])
        if (avg_v > 90):
            img_aug = np.copy(img)
            img_aug[img_aug[:, :, 2] <= 50, 2] = 0
            img_aug[img_aug[:, :, 2] > 50,
                    2] = img_aug[img_aug[:, :, 2] > 50, 2] - 50
            img_aug = cv2.cvtColor(img_aug, cv2.COLOR_HSV2BGR)
            aug_path = join(f'./data_aug/{c}', f'darker_{img_file}')
            cv2.imwrite(aug_path, img_aug)
        if (avg_v < 160):
            img_aug = np.copy(img)
            img_aug[img_aug[:, :, 2] >= 205, 2] = 255
            img_aug[img_aug[:, :, 2] < 205,
                    2] = img_aug[img_aug[:, :, 2] < 205, 2] + 50
            img_aug = cv2.cvtColor(img_aug, cv2.COLOR_HSV2BGR)
            aug_path = join(f'./data_aug/{c}', f'lighter_{img_file}')
            cv2.imwrite(aug_path, img_aug)

# %%
# change lighting of image (corrected dataset)
images_0 = [f for f in listdir(
    './correct_data/train/0') if isfile(join('./correct_data/train/0', f))]
images_1 = [f for f in listdir(
    './correct_data/train/1') if isfile(join('./correct_data/train/1', f))]
images_2 = [f for f in listdir(
    './correct_data/train/2') if isfile(join('./correct_data/train/2', f))]

all_images = [images_0, images_1, images_2]

for c in range(3):
    for img_file in all_images[c]:
        img = cv2.imread(join(f'./correct_data/train/{c}', img_file))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        avg_v = np.sum(img[:, :, 2]) / (img.shape[0] * img.shape[1])
        if (avg_v > 90):
            img_aug = np.copy(img)
            img_aug[img_aug[:, :, 2] <= 50, 2] = 0
            img_aug[img_aug[:, :, 2] > 50,
                    2] = img_aug[img_aug[:, :, 2] > 50, 2] - 50
            img_aug = cv2.cvtColor(img_aug, cv2.COLOR_HSV2BGR)
            aug_path = join(
                f'./correct_data_aug/train/{c}', f'darker_{img_file}')
            cv2.imwrite(aug_path, img_aug)
        if (avg_v < 160):
            img_aug = np.copy(img)
            img_aug[img_aug[:, :, 2] >= 205, 2] = 255
            img_aug[img_aug[:, :, 2] < 205,
                    2] = img_aug[img_aug[:, :, 2] < 205, 2] + 50
            img_aug = cv2.cvtColor(img_aug, cv2.COLOR_HSV2BGR)
            aug_path = join(
                f'./correct_data_aug/train/{c}', f'lighter_{img_file}')
            cv2.imwrite(aug_path, img_aug)

# %%
