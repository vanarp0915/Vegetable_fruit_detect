import cv2
import numpy as np
from keras_squeezenet import SqueezeNet
from keras.optimizers import Adam
from keras.utils import np_utils
from keras.layers import Activation, Dropout, Convolution2D, GlobalAveragePooling2D
from keras.models import Sequential
import tensorflow as tf
import os

__author__      = "Vanarp0915"

IMG_SAVE_PATH = 'data'
CLASS_MAP = {'Apple':0,'Banana':1,'Bello Pepper':2,'Chilli Pepper':3,'Grapes':4,'Jalepeno':5,'Kiwi':6,'Lemon':7,'Mango':8,'Orange':9,'Paprika':10,'Pear':11,'Pineapple':12,'Pomegranate':13,'Watermelon':14,'Beetroot':15,'Cabbage':16,'Capsicum':17,'Carrot':18,'Cauliflower':19,'Corn':20,'Cucumber':21,'Eggplant':22,'Ginger':23,'Lettuce':24,'Onion':25,'Peas':26,'Potato':27,'Raddish':28,'Soy Beans':29,'Spinach':30,'Sweetcorn':31,'Sweetpotato':32,'Tomato':33,'Turnip':34}
}
NUM_CLASSES = len(CLASS_MAP)
def mapper(val):
    return CLASS_MAP[val]


def get_model():
    model = Sequential([
        SqueezeNet(input_shape=(227, 227, 3), include_top=False),
        Dropout(0.5),
        Convolution2D(NUM_CLASSES, (1, 1), padding='valid'),
        Activation('relu'),
        GlobalAveragePooling2D(),
        Activation('softmax')
    ])
    return model


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

data, labels = zip(*dataset)
labels = list(map(mapper, labels))


# one hot encode the labels
labels = np_utils.to_categorical(labels)

# define the model
model = get_model()
model.compile(
    optimizer=Adam(lr=0.0001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# start training
model.fit(np.array(data), np.array(labels), epochs=10)

# save the model
model.save("FV.h5.h5")

