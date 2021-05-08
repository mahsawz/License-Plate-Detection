# uncomment if want to force run on CPU
# import os
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

import numpy as np
import tensorflow as tf
import tensorflow.keras as K
from tensorflow.keras.applications.xception import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array

print(tf.config.list_physical_devices())

model = None
img_height, img_width = 224, 224


def recall_m(y_true, y_pred):
    K = tf.keras.backend
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall


def precision_m(y_true, y_pred):
    K = tf.keras.backend
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision


def f1_m(y_true, y_pred):
    K = tf.keras.backend
    precision = precision_m(y_true, y_pred)
    recall = recall_m(y_true, y_pred)
    return 2*((precision*recall)/(precision+recall+K.epsilon()))


def init():
    global model
    model = K.models.load_model("model.h5", custom_objects={
                                'f1_m': f1_m, 'precision_m': precision_m, 'recall_m': recall_m})


def predict():
    with open('dataset.txt', 'r') as f:
        images_paths = f.readlines()
    images_paths = [x.replace('\n', '').strip() for x in images_paths]

    images = []
    for ip in images_paths:
        img = load_img(ip, target_size=(img_height, img_width))
        img = img_to_array(img)
        img = preprocess_input(img)
        images.append(img)

    predictions = model.predict(np.array(images))
    prediction_indices = [np.argmax(p) for p in predictions]

    with open('predictions.txt', 'w') as f:
        for p, ip in zip(prediction_indices, images_paths):
            f.write(f'{ip}, {p}\n')


if __name__ == '__main__':
    init()
    predict()
