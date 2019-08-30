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

import sys
from PIL import Image
sys.modules['Image'] = Image

##################################################################
tensorflow.compat.v1.set_random_seed(0)
np.random.seed(0)

path = "./input/split-garbage-dataset"

train = ImageDataGenerator(
    rescale=1./255,
    rotation_range = 20,
    width_shift_range = 0.2,
    horizontal_flip= True,
    vertical_flip= True,
    fill_mode= 'nearest'
)

validataion = ImageDataGenerator(
    rescale= 1./255
)
test = ImageDataGenerator(
    rescale=1./255
)

img_shape = (224, 224, 3)

train_batch_size = 256
val_batch_size =32
##################################################################
train_generator = train.flow_from_directory(
    path+'/train',
    target_size=(img_shape[0], img_shape[1]),
    batch_size= val_batch_size,
    class_mode='categorical',
    shuffle=True
)

validataion_generator = validataion.flow_from_directory(
    path+'/valid',
    target_size=(img_shape[0],img_shape[1]),
    batch_size=val_batch_size,
    class_mode='categorical',
    shuffle=True
)

test_generator = test.flow_from_directory(
    path+'/test',
    target_size=(img_shape[0],img_shape[1]),
    batch_size=val_batch_size,
    class_mode='categorical',
    shuffle=True
)
##################################################################
vgg = VGG16(weights='imagenet',
            include_top=False,
            input_shape=img_shape
)
##################################################################
for layer in vgg.layers[:-3]:
    layer.trainable = False
##################################################################
model = Sequential()
model.add(vgg)

model.add(Flatten())
model.add(Dense(1024,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(6,activation='softmax'))

model.summary()
##################################################################
model.compile(
    loss='categorical_crossentropy',
    optimizer=Nadam(lr=1e-4),
    metrics=['acc']
)

ES = EarlyStopping(
    monitor='val_loss',
    mode='min',
    verbose=1,
    patience=10
)
MC = ModelCheckpoint(
    'VGG16 Garbage Classifier.h5',
    monitor='val_acc',
    mode='max',
    verbose=1,
    save_best_only=True
)



history = model.fit_generator(
    train_generator,
    steps_per_epoch=train_generator.samples/train_generator.batch_size,
    epochs=30,
    validation_data=validataion_generator,
    validation_steps=validataion_generator.samples/validataion_generator.batch_size,
    verbose=0,
    callbacks=[ES, MC],
)

