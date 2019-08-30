import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow

from keras.preprocessing.image import ImageDataGenerator

from keras.applications import VGG16
from keras.layers import Flatten, Dense, Dropout
from keras.models import Sequential
from keras.optimizers import RMSprop, SGD, Adam, Nadam
from keras.regularizers import l1, l2, L1L2
from keras.callbacks import EarlyStopping, ModelCheckpoint


tensorflow.compat.v1.set_random_seed(0)
np.random.seed(0)

path = "./input/split-garbage-dataset"

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range = 20,
    width_shift_range = 0.2,
    horizontal_flip= True,
    vertical_flip= True,
    fill_mode= 'nearest'
)

validataion_datagen = ImageDataGenerator(
    rescale= 1./255
)
test_datagen = ImageDataGenerator(
    rescale=1./255
)


