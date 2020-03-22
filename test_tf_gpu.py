import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

print('GPU', tf.test.is_gpu_available())

a = tf.constant(2.)
b = tf.constant(2.)

print(a*b)