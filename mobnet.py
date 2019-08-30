from __future__ import absolute_import, division, print_function
import numpy as np
import tensorflow as tf
from google.protobuf import text_format
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import glob, os, random
from keras.preprocessing import image
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.callbacks import EarlyStopping, ModelCheckpoint


base_path = './input2/Garbage classification/Garbage classification'
img_list = glob.glob(os.path.join(base_path, '*/*.jpg'))



##################################################################
for i, img_path in enumerate(random.sample(img_list, 6)):
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img, dtype=np.uint8)
##################################################################
train = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.1,
    zoom_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True,
    vertical_flip=True,
    validation_split=0.1
)
test = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.1
)
##################################################################
train_generator = train.flow_from_directory(
    base_path,
    target_size=(224, 224),
    batch_size=16,
    class_mode='categorical',
    subset='training',
    seed=0
)

validation_generator = test.flow_from_directory(
    base_path,
    target_size=(224, 224),
    batch_size=16,
    class_mode='categorical',
    subset='validation',
    seed=0
)
##################################################################

IMG_SHAPE = (224,224,3)
base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                               include_top=False,
                                               weights='imagenet')
base_model.trainable = False

model = tf.keras.Sequential([
  base_model,
  keras.layers.GlobalAveragePooling2D(),
  keras.layers.Dense(6, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])

batch_size = 32
epochs = 8
steps_per_epoch = train_generator.n // batch_size
validation_steps = validation_generator.n // batch_size
##################################################################
history = model.fit_generator(
    train_generator,
    steps_per_epoch = steps_per_epoch,
    epochs=epochs,
    workers=4,
    validation_data=validation_generator,
    validation_steps=validation_steps
)
##################################################################
acc = history.history['acc']
val_acc = history.history['val_acc']

loss = history.history['loss']
val_loss = history.history['val_loss']


base_model.trainable = True
print("Number of layers in the base model: ", len(base_model.layers))

fine_tune_at = 100
##################################################################

# Freeze all the layers before the `fine_tune_at` layer
for layer in base_model.layers[:fine_tune_at]:
  layer.trainable =  False

model.compile(loss='binary_crossentropy',
              optimizer = tf.keras.optimizers.RMSprop(lr=2e-5),
              metrics=['accuracy'])
model.summary()

##################################################################

history_fine = model.fit_generator(train_generator,
                                   steps_per_epoch = steps_per_epoch,
                                   epochs=epochs,
                                   workers=4,
                                   validation_data=validation_generator,
                                   validation_steps=validation_steps,
                                   )
model.save('mobileNet.h5')
model.save('mobileNet.pb')
model_json = model.to_json()
with open("model_n.json", "w") as json_file:
    json_file.write(model_json)
############################################

sess = tf.compat.v1.Session()
tf.io.write_graph(sess.graph_def, './', 'label_map.pbtxt')

############################################


import cv2
cam = cv2.VideoCapture(0)
ARG_LIST = ['Cardboard', 'Glass', 'Metal', 'Paper', 'Plastic', 'Trash']
while cam.isOpened():
    ret, frame = cam.read()
    frame = cv2.resize(frame, (224, 224))
    pred = model.predict(np.resize ( frame , ( -1 , ( 224 , 224 , 3))))
    for i in pred:
        if i > 0.7:
            print()
    print(np.argmax(pred[0]))
    print(pred[0])
    print(np.argmax(pred))

    cv2.imshow('img',frame)
    k = cv2.waitKey(1)

    if k == 27:  # press ESC to exit
        cam.release()
        cv2.destroyAllWindows()
        break

'''

cam = cv2.VideoCapture(0)
ARG_LIST = ['Cardboard', 'Glass', 'Metal', 'Paper', 'Plastic', 'Trash']
while cam.isOpened():
    ret, frame = cam.read()

    frame = cv2.resize(frame, (224, 224))
    frame = tf.convert_to_tensor(frame, dtype=tf.float32)

    preds = loaded_model.predict(frame, steps=1)

    print(preds[0])
    print(np.argmax(preds[0]))
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)

    if k == 27:  # press ESC to exit
        cam.release()
        cv2.destroyAllWindows()
        break
        '''
