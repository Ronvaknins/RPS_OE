import cv2
import numpy as np
from keras_squeezenet import SqueezeNet
from keras.optimizers import Adam
from keras.utils import np_utils
from keras.layers import Activation, Dropout, Convolution2D, GlobalAveragePooling2D
from keras.models import Sequential
import sys

import tensorflow as tf
import os
import warnings
import logging
warnings.filterwarnings("ignore", message=r"Passing", category=FutureWarning)
warnings.filterwarnings("ignore")
logging.getLogger('tensorflow').disabled = True
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.get_logger().setLevel('ERROR')
IMG_SAVE_PATH = 'image_data'

CLASS_MAP_RPS = {
    "rock": 0,
    "paper": 1,
    "scissors": 2,
    "none": 3
}

CLASS_MAP_OE = {
    "odd": 0,
    "even": 1,
    "none": 2
}

NUM_CLASSES_RPS = len(CLASS_MAP_RPS)
NUM_CLASSES_OE = len(CLASS_MAP_OE)


def mapper_rps(val):
        return CLASS_MAP_RPS[val]

def mapper_oe(val):
    return CLASS_MAP_OE[val]


def get_model(game):
    if game == "rps":
        model = Sequential([
            SqueezeNet(input_shape=(227, 227, 3), include_top=False),
            Dropout(0.5),
            Convolution2D(NUM_CLASSES_RPS, (1, 1), padding='valid'),
            Activation('relu'),
            GlobalAveragePooling2D(),
            Activation('softmax')
        ])
        return model
    else:
        model = Sequential([
            SqueezeNet(input_shape=(227, 227, 3), include_top=False),
            Dropout(0.5),
            Convolution2D(NUM_CLASSES_OE, (1, 1), padding='valid'),
            Activation('relu'),
            GlobalAveragePooling2D(),
            Activation('softmax')
        ])
        return model

def train(game):
    if game == "rps":
        IMG_SAVE_PATH = "image_data//rps"
    else:
        IMG_SAVE_PATH = "image_data//oe"
    # load images from the directory
    dataset = []
    for directory in os.listdir(IMG_SAVE_PATH):
        path = os.path.join(IMG_SAVE_PATH, directory)
        if not os.path.isdir(path):
            continue
        for item in os.listdir(path):
            # to make sure no hidden files get in our way
            if item.startswith("."):
                continue
            img = cv2.imread(os.path.join(path, item))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (227, 227))
            dataset.append([img, directory])
    '''
    dataset = [
        [[...], 'rock'],
        [[...], 'paper'],
        ...
    ]
    '''
    data, labels = zip(*dataset)
    if game == "rps":
        labels = list(map(mapper_rps, labels))
    else:
        labels = list(map(mapper_oe, labels))
    '''
    labels: rock,paper,paper,scissors,rock...
    one hot encoded: [1,0,0], [0,1,0], [0,1,0], [0,0,1], [1,0,0]...
    '''
    # one hot encode the labels
    labels = np_utils.to_categorical(labels)
    # define the model
    model = get_model(game)
    model.compile(
        optimizer=Adam(lr=0.0001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    # start training
    model.fit(np.array(data), np.array(labels), epochs=10)
    # save the model for later use
    if game == "rps":
        model.save("rock-paper-scissors-model.h5")
    else:
        model.save("odd-even-model.h5")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Arguments Error: Format is  train.py {rps(rock paper scissors) or oe(odd even)}.")
        exit(0)
    elif sys.argv[1] == "rps" or sys.argv[1] == "oe":
        train(sys.argv[1])
    else:
        print("Arguments Error: Format is  train.py {rps(rock paper scissors) or oe(odd even)}.")
        exit(0)