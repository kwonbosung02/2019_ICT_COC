'''
import cv2 as cv

cvNet = cv.dnn.readNetFromTensorflow('VGG16 Garbage Classifier.pb', 'label_map.pbtxt')

img = cv.imread('example.jpg')
img = cv.resize(img, dsize=(224, 224), interpolation=cv.INTER_AREA)
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img = cv.cvtColor(img,cv.COLOR_GRAY2RGB)

rows = img.shape[0]
cols = img.shape[1]
cvNet.setInput(cv.dnn.blobFromImage(img, scalefactor=1.0, size=(224, 224), swapRB=True, crop=False))
cvOut = cvNet.forward()

for detection in cvOut[0,0,:,:]:
    score = float(detection[2])
    if score > 0.8:
        left = detection[3] * cols
        top = detection[4] * rows
        right = detection[5] * cols
        bottom = detection[6] * rows
        cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)

cv.imshow('img', img)
cv.waitKey()
'''
'''
import cv2
import numpy as np
from PIL import Image
from keras import models

#Load the saved model
model = models.load_model('VGG16 Garbage Classifier.h5')
video = cv2.VideoCapture(0)

while True:
        _, frame = video.read()

        im = Image.fromarray(frame, 'RGB')

        im = im.resize((224,224))
        img_array = np.array(im)


        img_array = np.expand_dims(img_array, axis=0)

        prediction = int(model.predict(img_array)[0][0])


        if prediction == 0:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print(prediction)
        cv2.imshow("Capturing", frame)
        key=cv2.waitKey(1)
        if key == ord('q'):
                break
video.release()
cv2.destroyAllWindows()
'''
'''
import cv2
import FModel
import numpy as np

model = FModel("model.json","VGG16 Garbage Classifier.h5")
font = cv2.FONT_HERSHEY_SIMPLEX

'''
'''
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.video = cv2.resize(self.video,(224,224))
    def __del__(self):
        self.video.release()
    def get_frame(self):
        _, fr = self.video.read()
        gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        pred = model.predict_e(fr[np.newaxis,:,:,np.newaxis])
        cv2.putText(fr, pred, (10, 10), font, 1, (255, 255, 0), 2)

        _, jpeg = cv2.imencode('.jpg', fr)
        return jpeg.tobytes()
'''
import numpy as np
import cv2
from keras.models import model_from_json

import cv2
import numpy  as np
import tensorflow as tf
from keras.models import model_from_json
from keras.models import load_model
loaded_model = tf.keras.Model('MobileNet.h5')
from keras.preprocessing import image

cam = cv2.VideoCapture(0)
ARG_LIST = ['Cardboard', 'Glass', 'Metal', 'Paper', 'Plastic', 'Trash']



while cam.isOpened():
    ret, frame = cam.read()
    pred = loaded_model.predict(frame[np.newaxis,:,:])
    '''
    frame= cv2.resize(frame,dsize=(299,299), interpolation = cv2.INTER_CUBIC)
    np_image_data = np.asarray(frame)
    np_image_data = cv2.normalize(np_image_data.astype('float'), None, -0.5, .5, cv2.NORM_MINMAX)
    np_final = np.expand_dims(np_image_data,axis=0)
    pred = loaded_model.predict(np_final)
    '''
    print(np.argmax(pred))


    #frame = np.resize ( frame , ( -1 , ( 224 , 224 , 3)))
    '''
    frame = frame[:, :, [2, 1, 0]]  # BGR2RGB

    pred = loaded_model.predict(frame)
    '''
    cv2.imshow('img',frame)

    k = cv2.waitKey(1)

    if k == 27:  # press ESC to exit
        cam.release()
        cv2.destroyAllWindows()
        break
    '''pred = loaded_model.predict(image.img_to_array(frame,dtype=np.uint8))
    cv2.imshow('img',frame)
    k = cv2.waitKey(1)

    if k == 27:  # press ESC to exit
        cam.release()
        cv2.destroyAllWindows()
        break


    # loaded_model._make_predict_function()

with open('model_n.json', "r") as json_file:
    loaded_model_json = json_file.read()
    loaded_model = tf.keras.Model(loaded_model_json)
    loaded_model.load_weights('MobileNet.h5')

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


from keras.models import model_from_json

import cv2
import numpy  as np
import tensorflow as tf
from keras.models import model_from_json

with open('model_n.json', "r") as json_file:
    loaded_model_json = json_file.read()
    loaded_model = tf.keras.Model(loaded_model_json)
    loaded_model.load_weights('VGG16 Garbage Classifier_n.h5')
    #loaded_model._make_predict_function()
    
    

cam = cv2.VideoCapture(0)
ARG_LIST=['Cardboard', 'Glass', 'Metal', 'Paper', 'Plastic', 'Trash']
while cam.isOpened():
    ret, frame = cam.read()

    frame = cv2.resize(frame,(224,224))
    frame = tf.convert_to_tensor(frame, dtype=tf.float32)

    preds = loaded_model.predict(frame,steps=1)
    

    
    print(preds[0])
    print(np.argmax(preds[0]))
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)

    if k == 27:  # press ESC to exit
        cam.release()
        cv2.destroyAllWindows()
        break'''