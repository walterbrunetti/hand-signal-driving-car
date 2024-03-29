# -*- coding: utf-8 -*-
"""LoadModel_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15qGzjgYnMFmrgRZqVVrVNokrxd69qiWl
"""

import tensorflow as tf
import numpy as np

img_height = 180
img_width = 180

class_names = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']



sunflower_url = "https://assets.megamediaradios.fm/2022/11/ap22312071681283-0d9c328f69a7c7f15320e8750d6ea447532dff66-s1100-c50.jpg"
sunflower_path = tf.keras.utils.get_file('fgdfgdfg4444', origin=sunflower_url)

img = tf.keras.utils.load_img(
    sunflower_path, target_size=(img_height, img_width)
)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

# Option 1
model = tf.saved_model.load("/content/")

#predictions = model.predict(img_array)
predictions = model.__call__(img_array,training=False)
score = tf.nn.softmax(predictions[0])

print(class_names)
print(predictions)

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)

# Option 2

model_2 = tf.keras.models.load_model("/content/op2")

predictions = model_2.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(class_names)
print(predictions)

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)

# Option 3 - Tensorflow lite


TF_MODEL_FILE_PATH = 'model.tflite' # The default path to the saved TensorFlow Lite model

interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)
interpreter.get_signature_list()

classify_lite = interpreter.get_signature_runner('serving_default')
classify_lite

predictions_lite = classify_lite(sequential_1_input=img_array)['outputs']
score_lite = tf.nn.softmax(predictions_lite)


print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score_lite)], 100 * np.max(score_lite))
)

print(np.max(np.abs(predictions - predictions_lite)))