import keras
from keras.models import load_model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform
'''
import tensorflow as tf
import cv2
from PIL import Image
import numpy as np
import keras
model = tf.keras.models.load_model('./mobileNet.pb')
video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 224)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 224)

while True:
    _, frame = video.read()

    im = Image.fromarray(frame, 'RGB')
    im = im.resize((224,224))
    img_array = np.array(im)

    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    print(prediction)
    print(np.argmax(prediction))
    cv2.imshow("fr",frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()



import cv2 as cv
prefixesToRemove = ('MultiscaleGridAnchorGenerator/', 'Concatenate/', 'MultipleGridAnchorGenerator/', 'Postprocessor/', 'Preprocessor/map')
cvNet = cv.dnn.readNetFromTensorflow('./mobileNet.pb', './label_map.pbtxt')
'''
import cv2
cv2.dnn.readNetFromTensorflow('mobileNet.pb', 'label_map.pbtxt')
