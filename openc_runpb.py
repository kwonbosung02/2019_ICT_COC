import numpy as np
import tensorflow as tf
import cv2

with tf.gfile.FastGFile('VGG16 Garbage Classifier.pb','rb') as f:
    graph_def = tf.GraphDef()

